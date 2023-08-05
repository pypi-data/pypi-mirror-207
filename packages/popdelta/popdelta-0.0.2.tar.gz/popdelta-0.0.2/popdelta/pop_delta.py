# pylint: disable=c-extension-no-member, arguments-differ, W0401, W0614
"""The PopDelta operator allows to automatically discover fundamental patterns/drivers in your data.
You can use it to characterize a single population (market basket analysis), or to find the differences
between two populations"""

from typing import List

import pandas as pd
import warnings

from .pop_delta1 import PopDelta1
from .pop_delta2 import PopDelta2
from .hot_encoder import HotEncoder

class PopDelta():
    """
    The class implementing PopDelta. It first bins and hot-encodes the data and then
    based on the type of PopDelta runs fpgrowth on 1 or 2 streams.
    """
    def __init__(self, target, num_bins, string_attributes):  # pylint: disable=unused-argument
        self.target = target if target != "" else None
        self.has_target = self.target is not None
        self.max_len = 3
        self._pop_delta = None
        self._encoder = None
        self._encoded_left = None
        self._encoded_right = None
        self._batch = None
        self._DEFAULT_CHUNK_SIZE = 10**4
        self._encoder = HotEncoder(self.target, string_attributes, num_bins)

    def _select_use_case(self, batches):
        self.max_len = min(self.max_len, len(batches[0].columns))
        if len(batches) == 1:
            pop_delta = PopDelta1(self)
        else:
            # len(batches) == 2
            pop_delta = PopDelta2(self)
        return pop_delta

    def _select_max_len(self, batches):
        """
        Select Itemset max length based on the default parameter and
        the input dataframe.
        """
        if len(batches) == 1:
            max_len = min(len(batches[0].columns), self.max_len)
        elif batches[0] is not None and batches[1] is not None:
            max_len = min(len(batches[0].columns), self.max_len)
        elif batches[0] is not None:
            max_len = min(len(batches[0].columns), self.max_len)
        else:  # batches[1] is not None:
            max_len = min(len(batches[1].columns), self.max_len)

        return max_len

    def _hot_encode(self, batches):
        """
        Hot-Encodes the binned input dataframe's columns to make it
        compatible with itemset mining. If two dataframes are given
        as input,  they are first vertically appended, then hot-encoded,
        and finally vertically split again.

        This ensures consistency of the columns.

        Args:
            batches List[pd.DataFrame]: Binned Dataframes

        Returns:
            batches List[pd.DataFrame]: Hot-Encoded Dataframes
        """


        if len(batches) == 1:
            # single batch
            encoded_batch, hot_encoder_warnings = self._encoder.process_batch(batches)
            batches = [encoded_batch]
        elif batches[0] is not None and batches[1] is not None:
            # both batches are good
            stacked_batch = [batches[0].append(batches[1])]
            encoded_batch, hot_encoder_warnings = self._encoder.process_batch(stacked_batch)
            batches = [encoded_batch[:len(batches[0])], encoded_batch[len(batches[0]):]]
        elif batches[0] is not None:
            # left batch is good, right batch is empty
            left_batch, hot_encoder_warnings = self._encoder.process_batch([batches[0]])
            batches = [left_batch, pd.DataFrame(columns=left_batch.columns)]
        else:
            # right batch is good, left batch is empty
            right_batch, hot_encoder_warnings = self._encoder.process_batch([batches[1]])
            batches = [pd.DataFrame(columns=right_batch.columns), right_batch]

        return batches

    def _one_chunks_generator(self, df1, chunk_size):
        df1 = df1.copy(deep=True).sample(frac=1)
        num_chunks_df1 = len(df1) // chunk_size + (1 if len(df1) % chunk_size != 0 else 0)

        for i in range(num_chunks_df1):
            start = i * chunk_size
            end = (i + 1) * chunk_size
            self.INPUT_SCALING_FACTORS = [end / len(df1)]

            chunk1 = df1.iloc[start:end] if i < num_chunks_df1 else None

            yield chunk1

    def _two_chunks_generator(self, df1, df2, chunk_size):
        df1 = df1.sample(frac=1).copy(deep=True)
        df2 = df2.sample(frac=1).copy(deep=True)

        num_chunks_df1 = len(df1) // chunk_size + (1 if len(df1) % chunk_size != 0 else 0)
        num_chunks_df2 = len(df2) // chunk_size + (1 if len(df2) % chunk_size != 0 else 0)

        for i in range(max(num_chunks_df1, num_chunks_df2)):
            start = i * chunk_size
            end = (i + 1) * chunk_size
            self.INPUT_SCALING_FACTORS = [end / len(df1), end / len(df2)]

            chunk1 = df1.iloc[start:end] if i < num_chunks_df1 else None
            chunk2 = df2.iloc[start:end] if i < num_chunks_df2 else None

            yield [chunk1, chunk2]



    def process_batch(self, batches: List[pd.DataFrame], progressive=False) -> pd.DataFrame:
        warnings.filterwarnings('ignore')

        if len(batches) == 1 & progressive == True:
            chunks_generator = self._one_chunks_generator(df1=batches[0], chunk_size=self._DEFAULT_CHUNK_SIZE)
        elif len(batches) == 2 & progressive == True:
            chunks_generator = self._two_chunks_generator(df1=batches[0], df2=batches[1], chunk_size=self._DEFAULT_CHUNK_SIZE)
        else:
            chunks_generator = [[b.copy(deep=True) for b in batches]]
            self.INPUT_SCALING_FACTORS = [1. for b in batches]



        for chunks in chunks_generator:
            encoded_batches = self._hot_encode(chunks)
            scaling_factors = self.INPUT_SCALING_FACTORS
            if self._pop_delta is None:
                self.max_len = self._select_max_len(chunks)
                self._pop_delta = self._select_use_case(encoded_batches)

            for result in self._pop_delta.process_batch(encoded_batches, scaling_factors):
                yield result


__all__ = ['PopDelta']
