# pylint: disable=c-extension-no-member, arguments-differ
"""Hot Encoding Operator"""

from typing import List
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype, is_categorical_dtype
import numpy as np

class HotEncoder():
    """"Operator that implements One-hot-encoding"""

    def __init__(self, target, string_attributes, num_bins):  # pylint: disable=unused-argument
        """
        Args:
            description (dict): protobuff input message
        """
        self._target = target
        self._max_cardinality = 20
        self._string_attributes = set(string_attributes)
        self._columns_to_drop = []
        self._bins = {}
        self._num_bins = num_bins
        self._columns_to_bin = []
        self._binary_columns = []
        self._non_binary_columns = []
        self._initialized = False
        self._warnings = []
        self._dropped_rows = 0

    def reset(self):
        self._columns_to_drop = []
        self._binary_columns = []
        self._non_binary_columns = []
        self._initialized = False

    def detect_columns_issues(self, df):
        """
        detect high cardinality, constant and binary columns
        """
        for col_name, column_values in df.items():
            unique_values = set(column_values.value_counts(dropna=False).index)
            num_unique = len(unique_values)
            # high cardinal columns
            if num_unique > self._max_cardinality:
                if is_numeric_dtype(df[col_name]) or is_datetime64_any_dtype(df[col_name]):
                    self._columns_to_bin.append(col_name)
                else:
                    self._columns_to_drop.append(col_name)
                    msg = f'Column {col_name} dropped because it has a high cardinality (>100).'
                    self._warnings.append(msg)
            if is_categorical_dtype(df[col_name]):
                self._columns_to_drop.append(col_name)
                msg = f'Column {col_name} dropped because it is a categorical column.'
                self._warnings.append(msg)
            # constant columns
            elif num_unique == 1:
                self._columns_to_drop.append(col_name)
            # null columns
            elif column_values.isna().all():
                self._columns_to_drop.append(col_name)
            # boolean columns
            elif (unique_values == {0, 1}) and (unique_values == {0.0, 1.0}) and (unique_values == {True, False}) and (col_name not in self._string_attributes):
                self._binary_columns.append(col_name)
        self._non_binary_columns = list(set(df.columns) - set(self._columns_to_drop) - set(self._binary_columns))

    # pylint: disable=cell-var-from-loop
    def process_batch(self, batches: List[pd.DataFrame]) -> pd.DataFrame:
        """
        Hot-encode input batch

        Args:
            batches (List[pd.DataFrame]): input batch

        Returns:
            pd.DataFrame: hot-encoded dataframe
        """

        def get_int_bin_val(col_name):
            # convert from age_1.0 to age_1

            att, bin_val = col_name.rsplit("_", 1)
            if bin_val == "nan":
                return col_name
            return "_".join([att, bin_val[:-2]])

        df = batches[0]
        # display(df)
        # print(df["age"])

        # remove target variable
        if self._target is not None:
            nrows = len(df)
            df.dropna(subset=[self._target], inplace=True)  # dropping rows which are nan on target
            self._dropped_rows += nrows - len(df)
            if self._dropped_rows != 0:
                msg = "Some rows dropped because they contained NaN values in the target column"
                self._warnings.append(msg)
            self._target_values = df[self._target].values
            df.drop(self._target, axis=1, inplace=True)

        if not self._initialized:
            self.detect_columns_issues(df)

        # drop high cardinality, constant or problematic columns
        df = df.drop(self._columns_to_drop, axis=1)

        # bin numerical columns
        for col_name in self._columns_to_bin:
            # first iteration - create bins
            if not self._initialized:
                df[col_name], labels = pd.cut(df[col_name], bins=self._num_bins, labels=None, retbins=True)
                self._bins[col_name] = labels
            else:
                # second iteration - use bins
                df[col_name] = pd.cut(df[col_name], bins=self._bins[col_name], labels=False)
            df[col_name] = df[col_name].astype(str)
        self._initialized = True

        if df.empty:
            print("No compatible attribute to analyze in the input dataframes. Please select other attributes.")


        # drop first element of binary columns
        df.fillna("nan", inplace=True)
        df = pd.get_dummies(df, columns=self._binary_columns, drop_first=True, dummy_na=True)
        df = pd.get_dummies(df, columns=self._non_binary_columns, dummy_na=True)

        df.columns = [get_int_bin_val(col_name) for col_name in df.columns if col_name not in self._binary_columns]

        # add back the target column
        if self._target is not None:
            df[self._target] = self._target_values

        return df, self._warnings


__all__ = ['HotEncoder']
