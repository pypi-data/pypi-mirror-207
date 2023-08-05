PopDelta is a data mining library for Python, developed to process and analyze Pandas Dataframes, interchangeably referred to as Populations. The primary objective of PopDelta is to identify underlying patterns within the data. This library is suitable for characterizing frequent patterns in a single dataframe or comparing differences between two dataframes, which proves useful for tasks such as contrasting customer groups or analyzing values' temporal shifts through cohort comparisons.

Possible applications for PopDelta:

Discerning frequent co-occurring patterns within a single dataset.
Detecting patterns that differentiate purchasing customers from non-purchasing ones.

Note: PopDelta was formerly called KDA (Key Driver Analysis).

# Installation

To install PopDelta, execute the following pip command:

`pip install popdelta`

# Usage

PopDelta incorporates built-in utilities for data cleaning, including handling missing data, rectifying data inconsistencies, and implementing One-Hot Encoding.

PopDelta initialization parameters are: 1) `target`: the attribute utilized to "weight" the discovered data patterns, in the absence of a target, patterns will be “weighted” only based on their frequencies (row counts “a la” vanilla frequent itemset). 2) `num_bins`: bins for discretizing numerical attributes, and 3) `string_attributes`: a list of attributes that should be forced to string type (useful for ordinal attributes encoded in numerical format).

After initializing PopDelta, the object can be used to iterate through the generator returned from the _process_batch_ function. This function requires two parameters: 1) `batches`: a list containing one, or two depending on the use case, dataframes for comparison purposes, and 2) `progressive`: a Boolean flag indicating whether the data should be processed progressively in chunks (recommended for datasets exceeding 10000 rows).

The user can compare datasets with not perfectly overlapping columns, as long as that intersection is not empty.

# Example

The expected usage and input are as follows (you can find more examples in the examples.ipynb notebook:

```
Import pandas as pd
from popdelta.pop_delta import PopDelta

pd.set_option('mode.use_inf_as_na', True)
df = pd.read_csv("messy_dataset.csv")


over_40 = df[df[“age] > 40]
under_40 = df[df[“age] <= 40]

popDeltaW2 = PopDelta(target=”age”, num_bins=3, string_attributes=[])

for result in popDeltaW2.process_batch([over_40, under_40]):
display(result)

```

In this example, PopDelta is utilized to analyze two datasets: `over_40` and `under_40`. The target variable for weighting is `age`, with `3` bins for discretizing numerical attributes and no predefined string attributes (applicable for ordinal attributes encoded as numerics).
