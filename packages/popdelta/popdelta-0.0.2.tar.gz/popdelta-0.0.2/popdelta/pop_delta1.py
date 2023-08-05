"""One Population Key Driver Analysis Class (NWPopDelta1/WPopDelta1)"""
import numpy as np

from .format_ouput import format_nwpopdelta1, format_wpopdelta1
from .miner import Miner


class PopDelta1:
    """"
    The operator implementing PopDelta1 (PopDelta 1 population).

    This operator works both without (NWPopDelta1) and with a target (WPopDelta1)
    column, where NW=non-weighted (without target) and W=weighted (with
    target)

    1) NWPopDelta1 reduces to a frequent itemset operator, where the counts
    are the number of rows an itemset is found in the input dataframe.
    Additional metrics are computed once the output is formatted.

    2) WPopDelta1 is a variation of frequent itemset operator, where the
    counts are the number of rows an itemset is found in the input
    dataframe weighted by the target column. As in the case of NWPopDelta1,
    additional fields are when the output is formatted.

    3) After the first exploratory batch has been used, PopDelta1 will perform
    lookups on the selected itemsets for all the sucessive batches.
    """

    def __init__(self, popdelta_status):
        self.pop_delta_status = popdelta_status
        self.target = popdelta_status.target
        self.has_target = popdelta_status.has_target
        self.weighted = self.target is not None
        self.max_len = popdelta_status.max_len
        self._initialized = False
        self.cumulative = None
        self.nw_count_left = 0
        self.w_count_left = 0

    def reset(self):
        """
        Reset Operator
        """
        self.initialized = False
        self.nw_count_left = 0
        self.w_count_left = 0

    def update_statistics(self, batch, weight_vector):
        """
        Update counters about the rows/weights that have been processed.

        Args:
            batch (pd.DataFrame): current batch
            weight_vector (np.array): current weights vector
        """

        self.nw_count_left += len(batch)
        if self.weighted:
            self.w_count_left += np.sum(weight_vector)

    def format_output(self):
        """
        Format PopDelta1 output for the front-end
        """

        if self.cumulative.empty:
            return self.cumulative

        if not self.weighted:
            return format_nwpopdelta1(df=self.cumulative,
                                 nw_sum_left=self.nw_count_left,
                                 scaling_factors=self._scaling_factors)

        return format_wpopdelta1(df=self.cumulative,
                            nw_sum_left=self.nw_count_left,
                            w_sum_left=self.w_count_left,
                            scaling_factors=self._scaling_factors)

    def process_batch(self, batches, scaling_factors):
        """
        Process Batch for PopDelta1:

        1) Separate the dataframe from the weight vector (if applies)
        2) Find optimal supports and incrementally stream the results
        3) Once the optimal support is found, mine the whole first batch
        and all the other subsequent batches from the input streams
        4) Cumulate the past results with the ones obtained from the current
        batch
        5) Format the batches for the output

        Args:
        batches ([pd.DataFrame]): list of batches (one) from the input stream
        Yields:
        output [pd.DataFrame]: results from the PopDelta1
        """

        batch = batches[0]
        miner = Miner(self.target, self.max_len)
        batch, weight_vector = miner.extract_weight_vector(batch)
        self._scaling_factors = scaling_factors

        if not self._initialized:
            for result in miner.find_support(batch, weight_vector):
                self.cumulative, self.nw_count_left, self.w_count_left = result
                output = self.format_output()
                if not output.empty:
                    yield output
            self._initialized = True
        else:
            if not self.has_target:
                weight_vector = None
            self.update_statistics(batch, weight_vector)
            batch_result = miner.lookup_itemset(itemsets=self.cumulative.index,
                                                df=batch,
                                                weight_vector=weight_vector,
                                                non_weighted=True,
                                                weighted=self.weighted)

            self.cumulative = self.cumulative.append(batch_result).groupby(level=0, sort=False).sum()
            output = self.format_output()
            if not output.empty:
                yield output
            return
