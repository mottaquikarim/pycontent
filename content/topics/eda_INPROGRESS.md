# EDA (Exploratory Data Analysis)

## Objectives

>>* Exploding
>>* Joining/Merging 
* Basic Descriptive Statistics
* Groupby Statements
* Key Takeaways

### Import Libraries & Load Data

```python
import pandas as pd
import numpy as np
from scipy import stats
print('import successful')
```

Load the data with `imdbID` as the index and make a copy.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_eda.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

## Exploding Condensed Data

You'll notice that some columns contain more than one value per row. For instance, a movie can be tagged as multiple genres. This limits us in that we cannot analyze movies in terms of unique genres. To fix this, we need to "explode" out the genre data so that a single record/row only equates one movie with one genre. In this format, if a movie is tagged as more than one genre, it will need to have a separate record/row for each of its genres. 

Take a look at this sample "Before & After" data:

*BEFORE EXPLODING*

| movie_id | Genre |
---------|-------|
| m1 | Drama, Action |
| m2 | Comedy |
| m3 | Crime, Comedy |

*AFTER EXPLODING*

| movie_id | Genre |
---------|-------|
| m1 | Drama |
| m1 | Action |
| m2 | Comedy |
| m3 | Crime |
| m3 | Comedy |


To do this with pandas, follow these **3 steps**: 

1. Create a new df and *reset the index* so that `imdbID` is a regular column instead of the index.
2. Each record in the genre column is a single string, in which multiple genres are separated by commas. Transform each record into a list.

```python
# 1.
movie_genres = movies['Genre'].copy().reset_index()
# 2.
movie_genres['Genre'] = movie_genres['Genre'].str.split(', ')

movie_genres.head()
```

3. Pass 'Genre' to the `.explode()` function, and set `ignore_index=True` so that the index gets reset.

```python
# 3.
movie_genres = movie_genres.explode('Genre', ignore_index=True)

movie_genres.head()
```

Take note of the movie IDs and see how their data got spread out after we applied `.explode()`. 

Next, we'll repeat this for `Languages`, `Countries`, and `Actors`. Afterwards, we'll drop all the columns we exploded from the main dataframe to keep it uncluttered.

```python
# Languages
movie_languages = movies['Language'].copy().reset_index()
movie_languages['Language'] = movie_languages['Language'].str.split(', ')
movie_languages = movie_languages.explode('Language', ignore_index=True)

# Countries
movie_countries = movies['Country'].copy().reset_index()
movie_countries['Country'] = movie_countries['Country'].str.split(', ')
movie_countries = movie_countries.explode('Country', ignore_index=True)

# Actors
movies.rename(mapper={'Actors': 'Actor'}, axis=1, inplace=True)
movie_actors = movies['Actor'].copy().reset_index()
movie_actors['Actor'] = movie_actors['Actor'].str.split(', ')
movie_actors = movie_actors.explode('Actor', ignore_index=True)

# Drop cols
movies.drop(columns=['Genre', 'Language', 'Country', 'Actor'], inplace=True)
```

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

<img src="https://github.com/mottaquikarim/pycontent/blob/master/content/images/quartiles.png?raw=true" style="margin: 0 auto;"/>

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









