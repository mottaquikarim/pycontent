# (EDA)

## Objectives

>>* basic stats concepts
	>>* distributions
	>>* measures of central tendency
	>>* 
	>>* dropping vs. filling nulls
>>* groupby
>>* basic descriptive stats
    >>* sampling
    >>* correlation
    >>* relative frequencies with groupby
    >>* tbd



### Import

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

print('import successful')
```

Load the data with `imdbID` as the index and make a copy.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_eda.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

## Dropping vs. Filling Null Values

explain how correlation doesn't work if vars are not identically distributed

>>Some common options include:
* Drop the whole column if it has a small percentage of non-null data,  e.g. We dropped the `Box Office` column from the original dataframe for this reason. 
* Drop all rows with data missing in ANY of the variables.
* Drop all rows with missing data only in a specific column or set of columns vital to your analysis.
* Replace null values with the mean for numerical data
* Replace null values with the frequency for categorical data. 
* Replace null values with some other piece of default data.


>>"Drop the data:
Drop the whole row (line #2)
Drop the whole column (the same as line #2 but with axis = 1)
Replace the data:
Replace NaN with the mean (numerical data) (line #8)
Replace NaN with the frequency (categorical data) (line #14)
Replace with another function (here we can use a function with np.vectorize() or the .apply() method)" -- Pyariksha Tiluk *"Python & pandas: serving data cleaning realness. You better wrangle!"**

## Basic Stats

>> Measures of central tendency
>> Measures of spread
>> What is a distribution?
>> Simple test?

Min: The smallest value in the column
Max: The largest value in the column
Quartile: A quartile is one fourth of our data
First quartile: This is the bottom most 25 percent
Median: The middle value. (Line all values biggest to smallest - median is the middle!) Also the 50th percentile
Third quartile: This the the top 75 percentile of our data

<img src="../images/quartiles.png" style="margin: 0 auto; float: right;"/>






## Groupby

>> .agg()

Grouby statements are particularly useful for a subsection-of-interest analysis. Specifically, zooming in on one condition, and determining relevant statstics.


Split: Separate our DataFrame by a specific attribute, for example, group by Color
Combine: Put our DataFrame back together and return some aggregated metric, such as the sum, count, or max.

`df.groupby(by=None, axis=0, level=None, as_index: bool = True, sort: bool = True, group_keys: bool = True, squeeze: bool = False, observed: bool = False)`


<img src="../images/split-apply-combine.png" style="margin: 0 auto; float: right;"/>

How the split-apply-combine chain of operations works
How to decompose the split-apply-combine chain into steps
How methods of a Pandas GroupBy object can be placed into different categories based on their intent and result


1. **Aggregation** methods (aka reduction methods) "consolidate many data points into an aggregated statistic about those data points. An example is to take the sum, mean, or median of 10 numbers, where the result is just a single number."
2. **Filter** methods "come back to you with a subset of the original DataFrame. This most commonly means using .filter() to drop entire groups based on some comparative statistic about that group and its sub-table. It also makes sense to include under this definition a number of methods that exclude particular rows from each group."
3. **Transformation** "methods return a DataFrame with the same shape and indices as the original, but with different values. With both aggregation and filter methods, the resulting DataFrame will commonly be smaller in size than the input DataFrame. This is not true of a transformation, which transforms individual values themselves but retains the shape of the original DataFrame."
4. **Meta** "methods are less concerned with the original object on which you called .groupby(), and more focused on giving you high-level information such as the number of groups and indices of those groups."
5. **Plotting** "methods mimic the API of plotting for a Pandas Series or DataFrame, but typically break the output into multiple subplots."



## Functions Featured

* **`.describe(include=np.object)`** -- return count, mean, standard deviation, min, max, & interquartile range (IQR); only includes numerical columns by default*
* **`s.value_counts()`** -- returns numerical frequency of each unique value in the Series
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
* **`df.sample(n=10)`** - randomly select n rows of a DataFrame
* **`s.cumsum()`** -- cummulative sum
* **`s.comprod()`** -- cumulative product
* **`s.cummin()`** -- cumulative minimum
