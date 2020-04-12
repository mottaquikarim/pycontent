# Basic EDA (Exploratory Data Analysis)

### Import Libraries & Load Data

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
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_clean_simple.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

**For simplicity's sake**, we edited the Genre, Language, and Country columns such that each movie only has one value for each. **This compromises the statistical integrity, but our analysis is only for learning the code. No one's making investment decisions off this info!**

## Summary & Descriptive Statistics

We'll start by defining some basic stats terms. When speaking about data, a **population** encompasses the *entire* set of items you're interested in, while a **sample** consists of a subset of those items. This is analagous to the difference between all the movies ever made (population) and the movies in our OMDb dataset (sample). Obtaining data on complete populations usually isn't feasible, so most statistical analyses are based on samples.

The heart of every quantitative analysis lies in the data's **descriptive statistics.** Descriptive statistics briefly summarize the data to help understand its makeup and organization.

## Describing Data in Pandas

In a Pandas dataframe, each row represents an item in your sample space, and each column is a variable representing some numerical or categorical characteristic of the items. Thus, each column will have its own set of descriptive statistics. Below is a quick overview of Pandas Series methods that return basic descriptive statistics for each column, or variable...

* **`.describe(include=np.object)`** -- returns count, mean, standard deviation, min, max, & IQR (interquartile range)
    * *only includes numerical columns by default*

^^ We'll define most of these individually below in the context of some of the OMDb variables!

### Averages

* **`s.mean()`** -- the simple average; 
    * *Downside is that it's greatly affected by outliers in the data!*
* **`s.median()`** -- in a lineup of ordinal data, the median is the middle number or category
* **`s.mode()`** -- the number or category that occurs most often in the dataset
    * Notice that even if this only returns one value, it returns a Series object

```python
imdb_ratings = movies['imdbRating']

mean_imdb = imdb_ratings.mean()
median_imdb = imdb_ratings.median()
mode_imdb = imdb_ratings.mode()

print(f'''
MEAN: {mean_imdb}, 
type = {type(mean_imdb)}

MEDIAN: {median_imdb}, 
type = {type(median_imdb)}''')

print(f'''
MODE: {mode_imdb}, 
type = {type(mode_imdb)}''')
```

### Ranges

* **`s.min()`** -- minimum; smallest value in the variable's data
* **`s.max()`** -- maximum; largest value in the variable's data
* *range* -- max value minus the min value
* **`s.quantile(q=0.5)`** -- return value at the given quantile q, where 0 <= q <= 1

Most often, people speak of "quartiles" which divide the data into 4 equal parts, each containing 25% of the data. As you can see below, the 2nd quartile is always the median.

<img src="https://www.mathsisfun.com/data/images/quartiles-a.svg" style="margin: 0 auto;"/>

People use the **IQR (Interquartile Range)** to describe the middle two quartiles of data. You calculate by taking the difference between the 3rd quartile and the 1st quartile. It's more useful than the regular range *because it excludes outliers*, which can skew your analysis.

Examine how quartiles overlap with other key statistical measures within the context of the `imdbRating` variable:

```python
imdbRating_quantiles = movies['imdbRating'].quantile(q=[0, 0.25, 0.5, 0.75, 1])
imdbRating_quantiles
```

Here we construct a dataframe to label these values contextually:

```python
imdb_quartiles = pd.DataFrame(index=['Min', '1st Quartile', '2nd Quartile (aka Median)', '3rd Quartile', 'Max'])
imdb_quartiles['Quantile'] = imdbRating_quantiles.index.values
imdb_quartiles['Value per imdbRating'] = imdbRating_quantiles.values
imdb_quartiles
```

Finally, we calculate the IQR:

```python
imdb_iqr = imdb_ratings.quantile(0.75) - imdb_ratings.quantile(0.25)
print(f'imdbRating IQR = {imdb_iqr}')
```

### Relative Frequency

We already know about using `s.value_counts()` to obtain a count of each unique value within a Series object, but did you know that we can also get percentages from it? This method has a parameter called `normalize`, which is set to `False` by default. However, when you set it to `True`...

**`s.value_counts(normalize=True)`** -- returns percentages that represent each unique value's relative frequency within the data

Take a look at the percentage of movies made by each of the top 10 directors

```python
movies['Director'].value_counts(normalize=True).nlargest(10)
```

### Practice with Basic Descriptive Stats

#### 1) What's the longest movie?

```python

```

#### 2) What's the IQR of Metascore?

```python

```

#### 3) What's the percent difference between the average critic rating and the average audience rating (i.e. Rotten Tomatoes and imdbRating)? 

```python

```

#### 4) What country has produced the most movies?

```python

```

#### 5) What span of years do the movies in our sample cover?

```python

```

## Grouping Data in Pandas

In Pandas, groupby statements are similar to pivot tables in that they allow us to segment our population to a specific subset. 

**`df.groupby(by=None, sort=True,)`** -- return a `Groupby object`

For example, if we want to know the average movie length by country of production, a groupby statement would make this task much more straightforward. To understand how a groupby statement works, break it down like this:

**Split**: Separate our DataFrame by a specific attribute, in this case, `Country`. Now each unique `Country` value represents a group of movies.

**Apply**: For the movies within each Country group, find the mean of their `Runtime` values. 

**Combine**: Put our DataFrame back together and return an *aggregated* metric corresponding to each group. In this case, we would end up with the average movie Runtime for each unique Country.

<img src="http://i.imgur.com/yjNkiwL.png" style="margin: 0 auto; width:60%"/>

This is the code for the above example:

```python
movies.groupby('Country')['Runtime'].mean()
```

### More Groupby Examples

* Which 15 languages are rated highest on average by critics?

```python
movies.groupby('Language')['Rotten Tomatoes'].mean().sort_values(ascending=False).iloc[:15]
```

* What proportion of movies made in each year of the 1980s did each genre make up?

```python
movies[movies['Year'].between(1980, 1989)].groupby('Year')['Genre'].value_counts(normalize=True)
```

* Within a sample of 100 movies, how many movies were made in each Country?

```python
sample1 = movies.sample(100)
sample1

sample1.groupby('Country')['Year'].value_counts(normalize=True)
```

* More...

```python
sample1.groupby('Language')['Runtime'].max()
```

```python
sample1.groupby('Genre')['imdbVotes'].min()
```

## Functions Featured

* **`.describe(include=np.object)`** -- returns count, mean, standard deviation, min, max, & IQR (interquartile range)
    * *only includes numerical columns by default*
* **`s.mean()`** -- the simple average; 
    * *Downside is that it's greatly affected by outliers in the data!*
* **`s.median()`** -- in a lineup of ordinal data, the median is the middle number or category
* **`s.mode()`** -- the number or category that occurs most often in the dataset
* **`s.min()`** -- minimum; smallest value in the variable's data
* **`s.max()`** -- maximum; largest value in the variable's data
* *range* -- max value minus the min value
* **`s.quantile(q=0.5)`** -- return value at the given quantile q, where 0 <= q <= 1
* *IQR (Interquartile Range)* -- (3rd quartile minus 1st quartile)
* **`s.value_counts(normalize=False, sort=True, ascending=False, dropna=True)`** -- return a Series containing counts -- or, if normalize=True, relative frequencies -- of unique values


