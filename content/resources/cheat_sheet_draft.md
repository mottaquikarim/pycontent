>>https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ne.html#pandas.DataFrame.ne
^^ finding intersection or its complement?

>>categorical data
https://www.datacamp.com/community/tutorials/categorical-data#exploration


>>TESTING FUNCTIONS https://pandas.pydata.org/pandas-docs/stable/reference/general_utility_functions.html#testing-functions

## EDA

`obj.sample(n=None, frac=None, replace=False, weights=None, axis=None)`:

weightsstr or ndarray-like, optional
Default ‘None’ results in equal probability weighting. If passed a Series, will align with target object on index. Index values in weights not found in sampled object will be ignored and index values in sampled object not in weights will be assigned weights of zero. If called on a DataFrame, will accept the name of a column when axis = 0. Unless weights are a Series, weights must be same length as axis being sampled. If weights do not sum to 1, they will be normalized to sum to 1. Missing values in the weights column will be treated as zero. Infinite values not allowed.


relative frequencies
https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6






## Statistics

* **`s.round(n)`** -- round each value to n decimal places
* **`s.value_counts()`** -- 
* **`s.mean()`** -- mean
* **`s.median()`** -- median
* **`s.min()`** -- minimum
* **`s.max()`** -- maximum
* **`s.quantile(x)`** -- quantile
* **`s.var()`** -- variance
* **`s.std()`** -- standard deviation
* **`s.mad()`** -- mean absolute variation
* **`s.skew()`** -- skewness of distribution
* **`s.sem()`** -- unbiased standard error of the mean
* **`s.kurt()`** -- kurtosis
* **`s.cov()`** -- covariance
* **`s.corr()`** -- Pearson Correlation coefficent
* **`s.autocorr()`** -- autocorelation
* **`df.sample(frac = 0.5)`** - randomly select a fraction of rows of a DataFrame
* **`df.sample(n=10)`** -- randomly select n rows of a DataFrame
* **`s.cumsum()`** -- cummulative sum
* **`s.comprod()`** -- cumulative product
* **`s.cummin()`** -- cumulative minimum


* **`df.pct_change(self[, periods, …])`** -- % change between the current and a prior element.

* **`df.quantile(q, axis, ...)`** -- Return values at the given quantile over requested axis.

* **`df.rank(self[, axis])`** -- Compute numerical data ranks (1 through n) along axis.
`get_dummies(data[, prefix, prefix_sep, …])`: Convert categorical variable into dummy/indicator variables.
`factorize(values, sort, na_sentinel, …)`: Encode the object as an enumerated type or categorical variable.
`cut(x, bins, right[, labels])`: Bin values into discrete intervals.
`qcut(x, q[, labels])`: Quantile-based discretization function.


## Grouping




## Reshaping & Transposing


## Window
>>https://pandas.pydata.org/pandas-docs/stable/reference/window.html

Rolling objects are returned by .rolling calls: pandas.DataFrame.rolling(), pandas.Series.rolling(), etc. Expanding objects are returned by .expanding calls: pandas.DataFrame.expanding(), pandas.Series.expanding(), etc. EWM objects are returned by .ewm calls: pandas.DataFrame.ewm(), pandas.Series.ewm(), etc.


## Grouping

df.groupby(by=None, axis=0, level=None, as_index: bool = True, sort: bool = True, group_keys: bool = True, squeeze: bool = False, observed: bool = False)


## Reshaping, Pivoting, Melting, Unstacking, & Transposing
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#reshaping-sorting-transposing

`df.transpose()`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose

## Join




## Merge


https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html#pandas.merge

