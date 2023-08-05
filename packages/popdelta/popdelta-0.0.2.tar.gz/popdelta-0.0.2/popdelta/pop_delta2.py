"""Two Population Key Driver Analysis Class (NWPopDelta2/WPopDelta2)"""

import numpy as np
from itertools import zip_longest

from .format_ouput import format_nwpopdelta2, format_wpopdelta2
from .miner import Miner


class PopDelta2:
    """"
    Class implementing PopDelta2 (PopDelta 2 populations).

    This operator works both without (NWPopDelta2) and with a target (WPopDelta2)
    column (where NW=non-weighted (without target) and W=weighted (with
    target))

    1) NWPopDelta2 reduces to a DIFF operator, where the counts are the number
    of rows an itemset is found in the input dataframes LEFT and RIGHT.
    Given that the itemsets mined in LEFT and RIGHT are likely not
    identical we use lookups to get counts of those itemsets.

    2) WPopDelta2 is a weighted DIFF operator, where the counts are the number
    of rows an itemset is found in the input dataframea LEFT and RIGHT
    weighted by the target columns. As in the case of NWPopDelta2, additional
    fields are computed when the output is formatted. As in the previous
    case the itemsets found in LEFT and RIGHT are unlikely to be
    identical: we use lookups to get the counts for those itemsets.

    3) After the first exploratory batch has been used, PopDelta2 will perform
    lookups on the selected itemsets for all the sucessive batches.
    """

    def __init__(self, popdelta_status):
        self.popdelta_status = popdelta_status
        self.target = popdelta_status.target
        self.has_target = popdelta_status.has_target
        self.weighted = self.target is not None
        self.max_len = popdelta_status.max_len
        self._initialized = False
        self.cumulative = None

        self.nw_count_left = 0
        self.w_count_left = 0
        self.nw_count_right = 0
        self.w_count_right = 0

    def reset(self):
        self._initialized = False
        self.nw_count_left = 0
        self.w_count_left = 0
        self.nw_count_right = 0
        self.w_count_right = 0

    def _update_statistics(self):
        """
        Update counters about the rows/weights that have been processed.
        """

        self.nw_count_left += len(self.left_batch)
        self.nw_count_right += len(self.right_batch)
        if self.weighted:
            self.w_count_left += np.sum(self.left_weight_vector)
            self.w_count_right += np.sum(self.right_weight_vector)

    def _join_batch_result(self, left_result, right_result, left_miner, right_miner):
        """
        Join the results from the current batches, if it is the first
        iteration perform lookups to ensure the results are consistent across
        the two result batches.

        Args:
        left_result (pd.DataFrame): mined itemsets from the current
        left batch right_result (pd.DataFrame): mined itemsets from the
                                                current right batch

        Returns: result: joined results from current batches
        """

        if not self._initialized:

            def augment(augmentee, augmentor, miner, batch, weight_vector, result):
                """
                Lookup itemsets from missing itemsets list
                """
                missing = np.array(list(augmentor.difference(augmentee)), dtype=tuple)
                found = miner.lookup_itemset(missing, batch, weight_vector=weight_vector,
                                             non_weighted=True, weighted=self.weighted)
                augmented_result = result.append(found)
                augmented_result.index.name = "itemset"
                return augmented_result

            # compute itemsets from the two sides
            left_itemsets = set(left_result.index.values)
            right_itemsets = set(right_result.index.values)

            # lookup on a partial version of the data
            left_batch = self.left_batch[:self.nw_count_left]
            right_batch = self.right_batch[:self.nw_count_right]

            if self.has_target:
                left_weight_vector = self.left_weight_vector[:self.nw_count_left]
                right_weight_vector = self.right_weight_vector[:self.nw_count_right]
            else:
                left_weight_vector = None
                right_weight_vector = None

            left_result = augment(left_itemsets, right_itemsets, left_miner,
                                  left_batch, left_weight_vector, left_result)

            right_result = augment(right_itemsets, left_itemsets, right_miner,
                                   right_batch, right_weight_vector, right_result)

        # join results from the two sides
        result = left_result.join(right_result, how="outer", lsuffix="_left", rsuffix="_right")
        return result

    def _cumulate_results(self, result, dummy):
        if dummy is None:
            self.cumulative = self.cumulative.append(result).groupby(level=0, sort=False).sum()

        else:
            result.columns = [col_name + dummy for col_name in result.columns]
            type_cast = {col_name: int if "nw" in col_name.split("_") else float for col_name in result.columns}
            cumulated = self.cumulative[result.columns].append(result).astype(type_cast)
            self.cumulative[result.columns] = cumulated.groupby(level=0, sort=False) \
                                                       .sum() \
                                                       .set_index((self.cumulative.index))

    def format_output(self):
        """
        Format PopDelta2 output for the front-end
        """

        if self.cumulative.empty:
            return self.cumulative

        if not self.weighted:
            return format_nwpopdelta2(df=self.cumulative,
                                 nw_sum_left=self.nw_count_left,
                                 nw_sum_right=self.nw_count_right,
                                 scaling_factors=self._scaling_factors)

        return format_wpopdelta2(df=self.cumulative,
                            nw_sum_left=self.nw_count_left,
                            nw_sum_right=self.nw_count_right,
                            w_sum_left=self.w_count_left,
                            w_sum_right=self.w_count_right,
                            scaling_factors=self._scaling_factors)

    def process_batch(self, batches, scaling_factors):
        """
        Process Batch for PopDelta2:

        1) Separate the dataframe from the weight vector (if applies)
        2) Find optimal supports and incrementally stream the results
        3) Once the optimal support is found, mine the whole first batches
        and all the other subsequent batches from the input streams
        4) Cumulate the past results with the ones obtained from the current
        batch
        5) Format the batches for the output

        Args:
        batches ([pd.DataFrame]): list of batches (two) from the input stream
        Yields:
        output [pd.DataFrame]: results from the PopDelta2
        """

        left_miner = Miner(self.target, self.max_len)
        right_miner = Miner(self.target, self.max_len)
        self.left_batch, self.left_weight_vector = left_miner.extract_weight_vector(batches[0])
        self.right_batch, self.right_weight_vector = right_miner.extract_weight_vector(batches[1])
        self._scaling_factors = scaling_factors

        if not self._initialized:
            left_iterator = left_miner.find_support(self.left_batch, self.left_weight_vector)
            right_iterator = right_miner.find_support(self.right_batch, self.right_weight_vector)

            for left_iter_result, right_iter_result in zip_longest(left_iterator, right_iterator):
                if left_iter_result is not None:
                    left_result, self.nw_count_left, self.w_count_left = left_iter_result
                if right_iter_result is not None:
                    right_result, self.nw_count_right, self.w_count_right = right_iter_result

                self.cumulative = self._join_batch_result(left_result, right_result, left_miner, right_miner)
                output = self.format_output()

                if not output.empty:
                    yield output
            self._initialized = True
        else:
            self._update_statistics()
            if not self.left_batch.empty:
                left_result = left_miner.lookup_itemset(itemsets=self.cumulative.index,
                                                        df=self.left_batch,
                                                        weight_vector=self.left_weight_vector,
                                                        non_weighted=True,
                                                        weighted=self.weighted)
            if not self.right_batch.empty:
                right_result = right_miner.lookup_itemset(itemsets=self.cumulative.index,
                                                          df=self.right_batch,
                                                          weight_vector=self.right_weight_vector,
                                                          non_weighted=True,
                                                          weighted=self.weighted)

            if not self.left_batch.empty and not self.right_batch.empty:
                batch_result = self._join_batch_result(left_result, right_result, left_miner, right_miner)
                self._cumulate_results(batch_result, dummy=None)
            elif not self.left_batch.empty and self.right_batch.empty:
                self._cumulate_results(left_result, dummy="_left")
            elif self.left_batch.empty and not self.right_batch.empty:
                self._cumulate_results(right_result, dummy="_right")

            output = self.format_output()
            if not output.empty:
                yield output
            return
