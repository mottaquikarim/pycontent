# EDA (Exploratory Data Analysis): Part 1

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

In Pandas, groupby statements are similar to pivot tables in that they allow us to segment our population to a specific subset. For example, if we want to know the average movie length by country of production, a groupby statement would make this task much more straightforward. To understand how a groupby statement works, we'll break it down.

### Breaking Down GroupBy Statements

**1. Split**:

**`df.groupby(by=None, sort=True)`** -- return a **GroupBy** object

First, use `.groupby()` to separate our dataframe into groups by a specific attribute. The resultant GroupBy object can be thought of as a **collection of groups.** 

```python
gb = movies.groupby('Country')
gb
```

Printing out `g` above only shows the user the GroupBy object as an abstraction. To get a little more information, access the GroupBy object's `.groups` attribute. This will show you the name of each group and a corresponding subset of rows (referenced by their index labels) from the original dataframe. In our example, you'll see that each unique `Country` represents a subset of movies.

```python
gb.groups
```

Notice the structure of the dict above. What if you wanted to return the movies in a certain group as their own independent dataframe? You'd access the dict key to obtain the group of index labels. You'd then use this group of index labels to filter out your desired rows from the original dataframe. That's what happens behind the scenes if you use the built-in `GroupBy.get_group()` method.

```python
argentina = gb.get_group('Argentina')
argentina
```

**2. Apply**: 

The reason we broke the dataframe into groups was to apply some function or calculation to each group. In our case, we want to know the average Runtime for the movies in each group.

We just saw above how to manually get each group as its own dataframe. If we wanted, we could manually calculate the average Runtime for each Country's movies.

Here's the result for Argentina's movies:

```python
argentina = argentina['Runtime'].mean()
```

And Australia... 

```python
australia = gb.get_group('Australia')['Runtime'].mean()
```

**3. Combine**: 

Finally, we would combine those results into a Series summarizing the Average Movie Runtime for each country. 

```python
avg_runtimes = {'Argentina': argentina, 'Australia': australia}
runtime_by_country = pd.Series(data=avg_runtimes, name='Average Movie Runtime')
runtime_by_country
```

GroupBy objects eliminate the need to do this manually. If we put the whole groupby statement together, it will do all of these steps for us at once:

*Notice that, by default, the data is sorted on the group names.*

```python
movies.groupby('Country')['Runtime'].mean()
```

### More Groupby Examples

* Which 15 languages are rated highest on average by critics?

```python
movies.groupby('Language')['Rotten Tomatoes'].mean().sort_values(ascending=False).iloc[:15]
```

* For each year of the 1980s, what was the genre distribution of movies made (in percentages)?

```python
movies[movies['Year'].between(1980, 1989)].groupby('Year')['Genre'].value_counts(normalize=True)
```

* Which genre got the fewest votes on IMDb as a group? 

```python
movies.groupby('Genre')['imdbVotes'].sum().sort_values()
```

* Within a sample of 100 movies, how many movies were made in each Country?

```python
sample100 = movies.sample(100)

sample100.groupby('Country')['Year'].value_counts()
```

* What is the longest movie runtime for each language group?

```python
movies.groupby('Language')['Runtime'].max().sort_values(ascending=False)
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
* **`df.groupby(by=None, sort=True)`** -- return a `Groupby object`
* **`gb.groups`** -- from a GroupBy object, returns the group names and a collection of each group's elements 
* **`gb.get_group(<group_name>)`** -- returns the elements of a specific group in a GroupBy object as a new dataframe object