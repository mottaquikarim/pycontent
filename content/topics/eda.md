# Basic EDA (Exploratory Data Analysis)

## Objectives



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

## Summary & Descriptive Statistics

We'll start by defining some basic stats terms. When speaking about data, a **population** encompasses the *entire* set of items you're interested in, while a **sample** consists of a subset of those items. This is analagous to the difference between all the movies ever made (population) and the movies in our OMDb dataset (sample). Obtaining data on complete populations usually isn't feasible, so most statistical analyses are based on samples.

The heart of every quantitative analysis lies in the data's **descriptive statistics.** Descriptive statistics briefly summarize the data to help understand its makeup and organization. **Histograms** often accompany descriptive statistics to help provide visual context about the measure's relation to the dataset as a whole. 

<img src="https://plot.ly/static/img/literacy/fig5.gif" style="margin: 0 auto;"/>
*Image from Plotly: https://help.plot.ly/histogram/#what-is-a-histogram*

Generally speaking, histograms represent "how frequently or infrequently certain values occur in a given set of data." In other words, they visualize the **distribution** of the data.

## Describing Data in Pandas

In a Pandas dataframe, each row represents an item in your sample space, and each column is a variable representing some numerical or categorical characteristic of the items. Thus, each column will have its own set of descriptive statistics. Below is a quick overview of Pandas Series methods that return basic descriptive statistics for each column, or variable.

**Measures of Central Tendency** i.e. Where's the middle of the data?

* **`s.mean()`** -- the simple average; 
    * *Downside is that it's greatly affected by outliers in the data!*
* **`s.median()`** -- in a lineup of ordinal data, the median is the middle number or category
* **`s.mode()`** -- the number or category that occurs most often in the dataset

**Measures of Variability** i.e. How spread out are the values, or how far away are they from the average?

* **`s.min()`** -- minimum; smallest value in the variable's data
* **`s.max()`** -- maximum; largest value in the variable's data
* **`s.quantile(q=0.5)`** -- return value at the given quantile q, where 0 < q < 1.

<img src="../images/quartiles.png" style="margin: 0 auto;"/>

```python

labels = ['min', 'Q1', 'Q2/Median', 'Q3', 'max']
quantiles = {
    'min': imdb_min,

    '' 
    
}
movies['imdbRating'].quantile(q=[0.25, 0.5, 0.75])

```


IQR: Interquartile range
    -- useful because it excludes outliers, which can skew your analysis



* **`s.quantile(x)`** -- quantile
* **`ss.iqr()`** -- interquartile range

**Measures of Frequency**

* **`s.value_counts()`** -- returns numerical frequency of each unique value in the Series
* **`s.mode()`** -- the number or category that occurs most often in the dataset



>>Analyzing data usually focuses on 