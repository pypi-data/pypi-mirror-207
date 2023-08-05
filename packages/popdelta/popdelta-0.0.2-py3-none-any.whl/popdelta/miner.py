"""Support class to mine itemsets from dataframes using fpgrowth or lookups"""
from collections import defaultdict

from fim import fpgrowth
import pandas as pd
import numpy as np


class Miner():
    """
    Miner class that provide access to FIS mining and lookup functionalities
    """

    def __init__(self, target, max_len):
        self._target = target
        self._max_len = max_len
        self._has_target = self._target is not None

        self._max_itemest_per_batch = 1 * 10 ** 4
        self._lookup_query_step = 1000

    def extract_weight_vector(self, df):
        """
        Separates weight vector from dataframe using target column and remove it from the dataframe

        Returns:
            [df]: original dataframe without target columns
            [weight_vector]: weights_vector
        """

        if self._has_target:
            weight_vector = df[self._target].values
            df.drop(self._target, axis=1, inplace=True)
        else:
            weight_vector = np.ones(len(df), dtype=np.int_)

        if set(weight_vector) == {0}:
            raise DavosException(f'Target vector {self._target} can not be constant-zero vector.')
        return df.astype(bool), weight_vector

    def get_transactions(self, df, weight_vector):
        """
        Format hot-ecoded matrix in  transaction map {transaction : weight}
        Returns:
            [transactions]: transaction map
        """

        def to_transaction(row):
            return tuple(sorted(df.columns[row.values == 1]))

        transactions = pd.DataFrame()
        transactions["transaction"] = df.apply(to_transaction, axis=1)
        transactions["weight_vector"] = weight_vector

        return transactions

    def find_support(self, df, weight_vector):
        """
        Learning from the data which is a good support to analyze the input data.
        Args:
            df [pd.DataFrame]: first batch from input stream
        Yields: iterator
            batch_itemset [pd.DataFrame]: mined itemsets
            nw_count [int]: number of processed rows
            w_count [float]: sum of the target column
        """

        def support_found(batch_itemset):
            return len(batch_itemset) > self._max_itemest_per_batch

        if df is None or df.empty:
            if self._target:
                yield pd.DataFrame(columns=["w_count", "nw_count"]), 0, 0
                return

            yield pd.DataFrame(columns=["nw_count"]), 0, 0
            return

        transactions = self.get_transactions(df, weight_vector)

        # logarithmic progression of supports level to test out for the PopDelta's first batch
        supports = [88, 78, 69, 61, 53, 47, 42, 37, 35, 32, 28, 25, 22, 20, 17, 15, 13, 10, 7, 5, 3, 1]
        len_supports = len(supports)
        for ix, support in enumerate(supports):

            # incremental exploration
            upper_bound = max(500, int((ix / len_supports) * len(transactions)))
            partial_transactions = transactions[: upper_bound]
            partial_df = df[: upper_bound]
            partial_weight_vector = weight_vector[: upper_bound]

            batch_itemset = self.mine_batch(df=partial_df,
                                            weight_vector=partial_weight_vector,
                                            transactions=partial_transactions,
                                            support=support,
                                            max_len=self._max_len)

            nw_count, w_count = len(partial_transactions), sum(partial_weight_vector)
            yield batch_itemset, nw_count, w_count
            if support_found(batch_itemset):
                nw_count, w_count = len(transactions), sum(transactions["weight_vector"])
                batch_itemset = self.mine_batch(df=df,
                                                weight_vector=weight_vector,
                                                transactions=transactions,
                                                support=support,
                                                max_len=self._max_len)

                self._support = support
                yield batch_itemset, nw_count, w_count
                return

    def mine_batch(self, df, weight_vector, transactions, support, max_len):
        """
        Find Itemsets within the first batch in the input stream.
        If a weight is provided, then It will perform two parallel FIS search
        and lookups to fill the gaps beween missing itemsets.

        Returns:
            result [pd.DataFrame]: mined itemsets counts
        """

        def scale_weights(transactions):
            max_weight = transactions["weight_vector"].max()
            multiplier = (np.iinfo(np.int32).max / (len(transactions) * max_weight))
            transactions["weight_vector"] = (transactions["weight_vector"] * multiplier).round().astype(np.int32)
            return transactions

        transactions = transactions.groupby(by="transaction", as_index=False).sum()
        if self._target is not None:
            pos_transactions = transactions[transactions["weight_vector"] > 0]
            pos_itemsets = set()
            if len(pos_transactions) > 0:
                pos_transactions = scale_weights(pos_transactions)
                pos_result = self.fpgrowth_wrapper(pos_transactions, support, max_len, "w_count")
                pos_itemsets = set(pos_result.index.values)

            neg_transactions = transactions[transactions["weight_vector"] < 0]
            neg_itemsets = set()
            if len(neg_transactions) > 0:
                neg_transactions["weight_vector"] *= -1
                neg_transactions = scale_weights(neg_transactions)
                neg_result = self.fpgrowth_wrapper(neg_transactions, support, max_len, "w_count")
                neg_itemsets = set(neg_result.index.values)

            itemset = list(pos_itemsets.union(neg_itemsets))

            result = self.lookup_itemset(np.array(itemset, dtype=tuple), df,
                                         weight_vector=weight_vector, non_weighted=True,
                                         weighted=True)
        else:
            result = self.fpgrowth_wrapper(transactions, support, max_len, "nw_count")

        return result

    def fpgrowth_wrapper(self, transactions, support, max_len, colname):
        """
        pyFIM library wrapper

        Args:
            transactions (dict): transaction-weight map
            support (int): minimum support to mine
            max_len (int): max itemset driver length

        Returns:
            [np.array]: array of itemsets-count tuples
        """
        transactions = dict(transactions.values)
        transactions[("DUMMY_TRANSACTION",)] = 1  # dummy entry to avoid 100 support

        itemset = fpgrowth(transactions,
                           target="s",
                           supp=support,
                           zmax=max_len)
        result = pd.DataFrame(itemset, columns=["itemset", colname])
        result["itemset"] = result["itemset"].apply(lambda x: tuple(sorted(x)))
        result = result.set_index("itemset").astype({colname: float})

        if ("DUMMY_TRANSACTION",) in result.index:
            result.drop(index=("DUMMY_TRANSACTION",), inplace=True)

        return result

    def lookup_itemset(self, itemsets, df, weight_vector, non_weighted, weighted, query_step=1000):
        """
        Directly query batch to find itemsets frequencies.


        Args:
            itemsets (list): list of itemset to lookup on the dataframe df
            df (pd.DataFrame): Dataframe on which the lookup needs to be perfomed
            weight_vector (np.array): array to weight the transactions
            non_weighted (bool): is this a NWPopDelta ?
            query_step (int, optional): Number of itemsets to lookup at each iteration. Defaults to 1000.

        Returns:
            result [pd.DataFrame]:
        """
        # weighted = weight_vector is not None

        if non_weighted and weighted:
            result = pd.DataFrame(columns=["w_count", "nw_count"])
        elif non_weighted:
            result = pd.DataFrame(columns=["nw_count"])
        elif weighted:
            result = pd.DataFrame(columns=["w_count"])

        if df is None or df.empty:
            result["itemsets"] = itemsets
            result = result.set_index("itemsets")
            result = result.fillna(0)
            return result
        if itemsets.size == 0:
            return result

        df["zero"] = False

        colname_map = defaultdict(lambda: -1)
        colname_map.update({item: ix for ix, item in enumerate(df.columns)})

        lengths = np.vectorize(len)(itemsets)

        nw_lookups_count, w_lookups_count, new_index = [], [], []

        for lower_bound in range(0, len(itemsets), query_step):
            upper_bound = lower_bound + query_step
            step_itemsets = itemsets[lower_bound: upper_bound]
            step_lengths = lengths[lower_bound: upper_bound]
            for k in range(1, self._max_len + 1):
                equi_length_itemsets = step_itemsets[step_lengths == k]
                new_index += equi_length_itemsets.tolist()
                step_itemsets_ix = [[colname_map[item] for item in itemset] for itemset in equi_length_itemsets]

                if step_itemsets_ix:
                    binary_lookups_matrix = np.all(df.values[:, step_itemsets_ix], axis=2)

                    if non_weighted:
                        nw_lookups_count += list(np.sum(binary_lookups_matrix, axis=0).reshape(-1))
                    if weighted:
                        w_lookups_count += list(np.dot(weight_vector, binary_lookups_matrix).reshape(-1))

        if non_weighted:
            result["nw_count"] = nw_lookups_count
            result["nw_count"] = result["nw_count"].astype(int)
        if weighted:
            result["w_count"] = w_lookups_count
            result["w_count"] = result["w_count"].astype(float)
        result.index = new_index
        result.index.name = "itemset"

        return result

    def cumulate_result(self, old, new):
        """Update cumulative itemset result dataframe using the current batch results"""

        old = old.append(new).groupby(by="itemset", sort=False).sum()
        return old
