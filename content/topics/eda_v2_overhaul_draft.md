# (EDA)

## Objectives

>>https://git.generalassemb.ly/mashaelalzaid/Titanic_lab
>>https://git.generalassemb.ly/A-bdullah/Pandas-Labs/blob/master/Titanic-Lab-solution2.ipynb

>>* basic stats concepts
	>>* qualities of variables (randomness & independence)
	>>* distributions
	>>* measures of central tendency
	>>* ways to handle null values and why choosing the right one is important
>>* groupby
	>> .agg()
	>> df.groupby('column').agg(['count', 'mean', 'max', 'min'])
	>> <img src="http://i.imgur.com/yjNkiwL.png" style="margin: 0 auto; width:60%"/>
>>* basic descriptive stats
	>>word frequency in the plot col?
	>>* binning (i.e. .cut())
    >>* sampling
    >>* correlation
    >>* relative frequencies with groupby / .value_counts()
    	>>* https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6





## Basic Stats

https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html

>>
>> population vs. sample
>> descriptive statistics
>> What is a distribution?
	>> A histogram can often add visual context to these measures. Histograms visualize the data's **probability distribution**, which is a function showing how often the values for a variable occur within the population or sample.

>> Measures of Central Tendency
>> Measures of Variability (Spread)
>> Measuring Asymmetry
	>> skewness important bc stats requires vars to be 
>>Measuring Frequency
>> Simple test?

## Summary & Descriptive Statistics

We'll start by defining some basic stats terms. When speaking about data, a **population** encompasses the *entire* set of items you're interested in, while a **sample** consists of a subset of those items. This is analagous to the difference between all the movies ever made (population) and the movies in our OMDb dataset (sample). Obtaining data on complete populations usually isn't feasible, so most statistical analyses are based on samples.

The heart of every quantitative analysis lies in the data's **descriptive statistics.** Descriptive statistics briefly summarize the data to help understand its makeup and organization. **Histograms** often accompany descriptive statistics to help provide visual context about the measure's relation to the dataset as a whole. 

<!--<img src="https://plot.ly/static/img/literacy/fig5.gif" style="margin: 0 auto; width:60%"/>

*Image from Plotly: https://help.plot.ly/histogram/#what-is-a-histogram*-->

Generally speaking, histograms represent "how frequently or infrequently certain values occur in a given set of data." In other words, they visualize the **distribution** of the data.




### Variability

Measures of variability quantify how dispersed the values in the dataset are, usually relative to their mean. 

The most basic measures of this are **variance**, **standard devitation**, and the **coefficient of variation**.

<img src="https://365datascience.com/wp-content/uploads/2018/09/image7.jpg"/>


* **`s.var()`** -- variance measures the spread of the data by 
* **`s.std()`** -- standard deviation

sample variance quantifies the spread of the data. It shows numerically how far the data points are from the mean.  the unit of measurement is squared. 

The sample standard deviation is another measure of data spread. It’s connected to the sample variance, as standard deviation, 𝑠, is the positive square root of the sample variance. The standard deviation is often more convenient than the variance because it has the same unit as the data points.


the coefficient of variation has its edge over standard deviation when it comes to comparing data. coefficient of variation. It is equal to the standard deviation, divided by the mean. good for comparing bc it is unit agnostic

`scipy.stats.variation(a[, axis, nan_policy])` -- compute the coefficient of variation, the ratio of the biased standard deviation to the mean

`s.value_counts(self, normalize=False, sort=True, ascending=False, bins=None, dropna=True)` -- return a Series containing counts -- or, if normalize=True, relative frequencies -- of unique values
	* when bins=n, instead of counting unique values, group them into n half-open bins (similar to pd.cut())
`movies['Year'].value_counts(bins=10)`
^^ can you specify to bin Year into decades (i.e. discrete intervals of 10 years)
`titanic['Fare'].value_counts(bins=7)`



## Groupby


>>https://chrisalbon.com/python/data_wrangling/pandas_apply_operations_to_groups/
>>https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
https://realpython.com/pandas-groupby/#how-pandas-groupby-works


.groupby() multiple cols
.groups
>> .groupby(). <stat>()
>> .groupby().agg()
>> grouping by BINS for continuous variables
>> .groupby()

Grouby statements are particularly useful for a subsection-of-interest analysis. Specifically, zooming in on one condition, and determining relevant statstics.



`df.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys: bool = True, squeeze: bool = False, observed: bool = False)`
>>https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby
by mapping, function, label, or list of labels
Used to determine the groups for the groupby. 
If by is a function, it’s called on each value of the object’s index. 
If a dict or Series is passed, the Series or dict VALUES will be used to determine the groups (the Series’ values are first aligned; see .align() method). 
If an ndarray is passed, the values are used as-is determine the groups. 
A label or list of labels may be passed to group by the columns in self. Notice that a tuple is interpreted as a (single) key.

1. Split a table into groups based on a specific attribute (e.g. Language)
2. Apply some operations to each of those smaller tables
3. Combine the results

It can be difficult to inspect movies.groupby('Genre') because it does virtually none of these things until you do something with the resulting object. 

<img src="../images/split-apply-combine.png" style="margin: 0 auto; float: right;"/>

"How the split-apply-combine chain of operations works
How to decompose the split-apply-combine chain into steps
How methods of a Pandas GroupBy object can be placed into different categories based on their intent and result" -- RealPython


>>Aggregation:
	>>df.groupby('column').agg(['count', 'mean', 'max', 'min'])
	>>df.groupby('')


**Aggregation** calculate some summary statistics for each group
**Meta** focuses on obtaining information about the resultant groups as opposed to the original dataframe





## Grouping Data in Pandas


```python

```



```python

```



```python

```



```python

```



## Correlation




>>> x.corr(y)                     # Pearson's r
0.7586402890911867
>>> y.corr(x)
0.7586402890911869
>>> x.corr(y, method='spearman')  # Spearman's rho
0.9757575757575757
>>> x.corr(y, method='kendall')   # Kendall's tau


## Functions Featured

* **`.describe(include=np.object)`** -- return count, mean, standard deviation, min, max, & interquartile range (IQR); only includes numerical columns by default*
* **`s.value_counts()`** -- returns numerical frequency of each unique value in the Series
* **`s.mean()`** -- mean
* **`s.median()`** -- median
* **`s.min()`** -- minimum
* **`s.max()`** -- maximum
* **`scipy.stats.iqr()`** -- interquartile range
 **`s.quantile(q=0.5)`** -- return value at the given quantile q, where 0 <= q <= 1.
    * Can pass multiple values for q to return a Series of quantiles
* **`df.rank(na_option='keep', )`** -- rank each 
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




