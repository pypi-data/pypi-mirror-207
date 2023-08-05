# pylint: disable=W0612, W0613
"""
Support functions to augment the PopDelta results to support
all the different use cases.

Acronyms Glossary:
* NW = non-weighted (frequencies)
* W = weighted (frequencies weighted by the target columns)
* NWPopDelta1 = non-weighted PopDelta on 1 population (without target)
* WPopDelta1 = weighted PopDelta on 1 population (with target)
* NWPopDelta2 = non-weighted PopDelta on 2 population (without target)
* WPopDelta2 = weighted PopDelta on 2 population (with target)
"""

from copy import deepcopy
import itertools
import pandas as pd

from .settings import *  # noqa: F401, F403, pylint: disable=wildcard-import


def explode_itemsets(df):
    """
    Explodes input dataframe 3 itemset columns to six expanded columns.
    If an itemset has length smaller than 3, the entries in that column will be NA.

    From the form:
    itemsets1_bin-value1|itemsets2_bin-value2|itemsets3_bin-value3|metric1|...|metric-nth
    to:
    itemset1|bin-value1|itemset2|bin-value1|itemset1|bin-value1|metric1|...|metric-nth

    or more concretly, from
    age_2|weight_3|height_0|mean|...|impact
    to:
    age|2|weight|3|height|0|mean|...|impact

    Args:
        df ([pd.DataFrane]):  input dataframe which itemset column is going to be exploded
    """
    def explode(itemset):
        itemset = map(lambda item: item.rsplit("_", 1), itemset)
        return list(itertools.chain.from_iterable(itemset))

    exploded_colname = ["item1", "value1", "item2", "value2", "item3", "value3"]
    dummy = [0] * 6  # in case the max len itemset is < 3 this forces the df to 6 columns
    itemsets = [explode(itemset) for itemset in df.index.values]
    itemsets.append(dummy)
    exploded_df = pd.DataFrame(itemsets, columns=exploded_colname)[:-1]
    exploded_df.index = df.index
    exploded_df[df.columns] = df
    exploded_df[["item1", "item2", "item3"]] = exploded_df[["item1", "item2", "item3"]].astype(str)

    exploded_df[["value1", "value2", "value3"]] = exploded_df[["value1", "value2", "value3"]]#.astype(float) \
                                                                                             #.astype(dtype="Int64")
    return exploded_df


def format_nwpopdelta1(df, nw_sum_left, scaling_factors):
    """
    Add to the result dataframe the metrics related to NWPopDelta1,
    non-weighted, without target, PopDelta with 1 population.

    Given Fields:
    * nw_sum_left: non-weighted sum, aka number of rows, form left dataframe  (from fpgrowth)
    """

    inter_df = deepcopy(df)
    inter_df = inter_df.rename(columns={"nw_count": ABSOLUTE_LEFT}).astype(float)

    # scaling results on the whole dataset
    nw_sum_left *= scaling_factors[0]
    inter_df[[ABSOLUTE_LEFT]] *= scaling_factors[0]

    inter_df[[ABSOLUTE_LEFT]].fillna(0, inplace=True)
    inter_df[RELATIVE_LEFT] = inter_df[ABSOLUTE_LEFT] / nw_sum_left

    inter_df[LENGTH] = inter_df.index.map(len)
    inter_df = explode_itemsets(inter_df)
    result = inter_df.sort_values(by=ABSOLUTE_LEFT, ascending=False)

    return result


def format_wpopdelta1(df, nw_sum_left, w_sum_left, scaling_factors):
    """
    Add to the result dataframe the metrics related to WPopDelta1,
    weighted (with target) PopDelta with 1 population.

    Given Fields:
    * w_sum_left: non-weighted sum, aka number of rows, form left dataframe  (from fpgrowth)
    * nw_sum_left: non-weighted sum, aka number of rows, form left dataframe  (from lookup)
    """

    nw_sum_left = scaling_factors[0] * nw_sum_left
    w_sum_left = scaling_factors[0] * w_sum_left

    inter_df = deepcopy(df)
    inter_df = inter_df.rename(columns={"w_count": CUMULATIVE_LEFT,
                                        "nw_count": ABSOLUTE_LEFT}).astype(float)

    # scaling results on the whole dataset
    nw_sum_left *= scaling_factors[0]
    w_sum_left *= scaling_factors[0]
    inter_df[[CUMULATIVE_LEFT, ABSOLUTE_LEFT]] *= scaling_factors[0]

    inter_df[[CUMULATIVE_LEFT, ABSOLUTE_LEFT]].fillna(0, inplace=True)

    # compute metrics
    inter_df[RELATIVE_LEFT] = inter_df[ABSOLUTE_LEFT] / nw_sum_left
    inter_df[AVERAGE_LEFT] = inter_df[CUMULATIVE_LEFT] / inter_df[ABSOLUTE_LEFT]
    inter_df[CONTRIBUTION_LEFT] = inter_df[CUMULATIVE_LEFT] / w_sum_left
    inter_df[DIFFERENCE_GLOABL_AVERAGE] = inter_df[AVERAGE_LEFT] - (w_sum_left / nw_sum_left)

    inter_df[LENGTH] = inter_df.index.map(len)
    inter_df = explode_itemsets(inter_df)
    result = inter_df.sort_values(by=DIFFERENCE_GLOABL_AVERAGE, ascending=False)

    return result


def format_nwpopdelta2(df, nw_sum_left, nw_sum_right, scaling_factors):
    """
    Add to the result dataframe the metrics related to NWPopDelta2,
    non-weighted (without target) PopDelta with 2 population.

    Given Fields:
    * nw_sum_left: non-weighted sum, aka number of rows, form left dataframe (from fpgrowth)
    * nw_sum_right: non-weighted sum, aka number of rows, form right dataframe  (from fpgrowth)
    """

    inter_df = deepcopy(df)
    inter_df = df.rename(columns={"nw_count_left": ABSOLUTE_LEFT,
                                  "nw_count_right": ABSOLUTE_RIGHT}).astype(float)

    # scaling results on the whole dataset
    nw_sum_left *= scaling_factors[0]
    nw_sum_right *= scaling_factors[1]
    inter_df[ABSOLUTE_LEFT] *= scaling_factors[0]
    inter_df[ABSOLUTE_RIGHT] *= scaling_factors[1]

    inter_df[[ABSOLUTE_LEFT, ABSOLUTE_RIGHT]].fillna(0, inplace=True)

    # compute metrics
    inter_df[ABSOLUTE_DIFFERENCE] = inter_df[ABSOLUTE_LEFT] - inter_df[ABSOLUTE_RIGHT]
    inter_df[ABSOLUTE_RATIO_LR] = inter_df[ABSOLUTE_LEFT] / inter_df[ABSOLUTE_RIGHT]
    inter_df[ABSOLUTE_RATIO_RL] = inter_df[ABSOLUTE_RIGHT] / inter_df[ABSOLUTE_LEFT]

    inter_df[RELATIVE_LEFT] = inter_df[ABSOLUTE_LEFT] / nw_sum_left
    inter_df[RELATIVE_RIGHT] = inter_df[ABSOLUTE_RIGHT] / nw_sum_right
    inter_df[RELATIVE_DIFFERENCE] = inter_df[RELATIVE_LEFT] - inter_df[RELATIVE_RIGHT]
    inter_df[RELATIVE_RATIO_LR] = inter_df[RELATIVE_LEFT] / inter_df[RELATIVE_RIGHT]
    inter_df[RELATIVE_RATIO_RL] = inter_df[RELATIVE_RIGHT] / inter_df[RELATIVE_LEFT]

    inter_df = risk_ratio(inter_df, ABSOLUTE_LEFT, ABSOLUTE_RIGHT, nw_sum_left, nw_sum_right)

    inter_df[LENGTH] = inter_df.index.map(len)
    inter_df = explode_itemsets(inter_df)
    result = inter_df.sort_values(by=RISK_RATIO_LR, ascending=False)

    return result


def format_wpopdelta2(df, nw_sum_left, nw_sum_right, w_sum_left, w_sum_right, scaling_factors):
    """
    Add to the result dataframe the metrics related to WPopDelta2,
    weighted (with target) PopDelta with 2 population.

    Given Fields:
    * w_count_left: sum of the weight vector form left dataframe (from fpgrowth)
    * w_count_right: sum of the weight vector from right dataframe (from fpgrowth)
    * nw_count_left: non-weighted sum, aka number of rows, form left dataframe (from lookup)
    * nw_count_right: non-weighted sum, aka number of rows, form right dataframe (from lookup)
    """

    inter_df = deepcopy(df)
    inter_df = inter_df.rename(columns={"w_count_left": CUMULATIVE_LEFT,
                                        "nw_count_left": ABSOLUTE_LEFT,
                                        "w_count_right": CUMULATIVE_RIGHT,
                                        "nw_count_right": ABSOLUTE_RIGHT}).astype(float)

    # scaling results on the whole dataset
    nw_sum_left *= scaling_factors[0]
    nw_sum_right *= scaling_factors[1]
    w_sum_left *= scaling_factors[0]
    w_sum_right *= scaling_factors[1]
    inter_df[[ABSOLUTE_LEFT, CUMULATIVE_LEFT]] *= scaling_factors[0]
    inter_df[[ABSOLUTE_RIGHT, CUMULATIVE_RIGHT]] *= scaling_factors[1]

    inter_df[[ABSOLUTE_LEFT, ABSOLUTE_RIGHT, CUMULATIVE_LEFT, CUMULATIVE_RIGHT]].fillna(0, inplace=True)

    # compute metrics
    inter_df[ABSOLUTE_DIFFERENCE] = inter_df[ABSOLUTE_LEFT] - inter_df[ABSOLUTE_RIGHT]
    inter_df[ABSOLUTE_RATIO_LR] = inter_df[ABSOLUTE_LEFT] / inter_df[ABSOLUTE_RIGHT]
    inter_df[ABSOLUTE_RATIO_RL] = inter_df[ABSOLUTE_RIGHT] / inter_df[ABSOLUTE_LEFT]

    inter_df[RELATIVE_LEFT] = inter_df[ABSOLUTE_LEFT] / nw_sum_left
    inter_df[RELATIVE_RIGHT] = inter_df[ABSOLUTE_RIGHT] / nw_sum_right
    inter_df[RELATIVE_DIFFERENCE] = inter_df[RELATIVE_LEFT] - inter_df[RELATIVE_RIGHT]
    inter_df[RELATIVE_RATIO_LR] = inter_df[RELATIVE_LEFT] / inter_df[RELATIVE_RIGHT]
    inter_df[RELATIVE_RATIO_RL] = inter_df[RELATIVE_RIGHT] / inter_df[RELATIVE_LEFT]

    inter_df[CUMULATIVE_DIFFERENCE] = inter_df[CUMULATIVE_LEFT] - inter_df[CUMULATIVE_RIGHT]
    inter_df[CUMULATIVE_RATIO_LR] = inter_df[CUMULATIVE_LEFT] / inter_df[CUMULATIVE_RIGHT]
    inter_df[CUMULATIVE_RATIO_RL] = inter_df[CUMULATIVE_RIGHT] / inter_df[CUMULATIVE_LEFT]

    inter_df[AVERAGE_LEFT] = inter_df[CUMULATIVE_LEFT] / inter_df[ABSOLUTE_LEFT]
    inter_df[AVERAGE_RIGHT] = inter_df[CUMULATIVE_RIGHT] / inter_df[ABSOLUTE_RIGHT]
    inter_df[AVERAGE_DIFFERENCE] = inter_df[AVERAGE_LEFT] - inter_df[AVERAGE_RIGHT]
    inter_df[AVERAGE_RATIO_LR] = inter_df[AVERAGE_LEFT] / inter_df[AVERAGE_RIGHT]
    inter_df[AVERAGE_RATIO_RL] = inter_df[AVERAGE_RIGHT] / inter_df[AVERAGE_LEFT]

    inter_df[CONTRIBUTION_LEFT] = inter_df[CUMULATIVE_LEFT] / w_sum_left
    inter_df[CONTRIBUTION_RIGHT] = inter_df[CUMULATIVE_RIGHT] / w_sum_right
    inter_df[CONTRIBUTION_DIFFERENCE] = inter_df[CONTRIBUTION_LEFT] - inter_df[CONTRIBUTION_RIGHT]
    inter_df[CONTRIBUTION_RATIO_LR] = inter_df[CONTRIBUTION_LEFT] / inter_df[CONTRIBUTION_RIGHT]
    inter_df[CONTRIBUTION_RATIO_RL] = inter_df[CONTRIBUTION_RIGHT] / inter_df[CONTRIBUTION_LEFT]

    inter_df = risk_ratio(inter_df, CUMULATIVE_LEFT, CUMULATIVE_RIGHT, w_sum_left, w_sum_right)

    inter_df[LENGTH] = inter_df.index.map(len)
    inter_df = explode_itemsets(inter_df)
    result = inter_df.sort_values(by=RISK_RATIO_LR, ascending=False)

    return result


def risk_ratio(df, left_colname, right_colname, sum_left, sum_right):
    """Compute Risk Ratio for PopDelta2 (PopDelta 2 Populations)
    For reference: https://cs.stanford.edu/~matei/papers/2019/vldb_macrobase_diff.pdf (page 4)

    1) Prob that a row will be in the A relation vs. the B relation, if it has an attribute vs. if it does not
        * risk_ratio_a_b = P(A|Itemset) / P(A|~Itemset)

    2) Prob that a row will be in the B relation vs. the A relation, if it has an attribute vs. if it does not
        * risk_ratio_b_a = P(B|Itemset) / P(B|~Itemset)
    """

    # risk ratio a over b
    num1 = df[left_colname] / (df[left_colname] + df[right_colname])
    den1_num = sum_left - df[left_colname]
    den1_den = (sum_left - df[left_colname]) + (sum_right - df[right_colname])
    den1 = den1_num / den1_den
    df[RISK_RATIO_LR] = num1 / den1

    # risk ratio b over a
    num2 = df[right_colname] / (df[right_colname] + df[left_colname])
    den2_num = sum_right - df[right_colname]
    den2_den = (sum_right - df[right_colname]) + (sum_left - df[left_colname])
    den2 = den2_num / den2_den
    df[RISK_RATIO_RL] = num2 / den2

    # df["max_risk_ratio"] = np.max(df[["risk_ratio_a_b", "risk_ratio_b_a"]].values, axis=1)

    return df
