# Data Wrangling

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.

## Objectives

* Document metadata based on common standards
* Renaming & reorganizing columns
* Filtering
* Sorting
* Handling duplicate rows

## Data Dictionaries

Our complete movies dataset contains a *lot* more movie metadata from the [OMDb API](http://www.omdbapi.com/). When you work with a large dataset, you should always include a `data dictionary`, or a list of variable definitions, alongside your notebook. It can serve as a contextual overview of the variables in the dataset as well as share information about how certain variables are formatted. If you're looking to study a dataset yourself, the data dictionary can also give you high-level ideas for what you might want to analyze and how.

Below is a data dictionary for the *unaltered OMDb data*. (We've left the definitions for a few self-explanatory variables blank.) If it seems disorganized and convoluted... that's because it is! The fields and formats here are the original ones obtained straight from the OMDB API. 

**5788 records x 29 columns**

* **Title**
* **Year**: Year the movie was made
* **Rated**: MPAA content rating (e.g. PG, NC17, R, etc.)
* **Released**: Date the movie was released to theaters
* **Runtime**: How long in number of minutes 
* **Genre**: One or more genres that describe the movie* 
* **Director**
* **Writer**
* **Actors**
* **Plot**
* **Language**: Audio languages available for movie (might exclude sub-title language availability)
* **Country**: Country/countries that produced the movie 
* **Awards**: # of nominations and # of wins for one or more types of awards
* **Poster**: Amazon-hosted image url for the poster of the movie
* **Ratings**: Series containing ratings from multiple sources (e.g. Rotten Tomatoes)
* **Metascore**: Metacritic rating from critics (from 0.0-100.0)
* **imdbRating**: Crowd-sourced audience rating from IMDb (from 0.0-10.0)
* **imdbVotes**: Number of user ratings from IMDb
* **imdbID**: Unique movie ID from IMDb
* **Type**: Content category ==(e.g. movie, tv, etc.)==
* **DVD**: Date the movie was released to DVD
* **BoxOffice**: Box office earnings in US dollars
* **Production**: Production company
* **Website**: URL
* **Response**: Boolean stored as string, indicates whether the API response was valid
* **Internet Movie Database**: Crowd-sourced audience rating from IMDb (from 0.0-10.0)
* **Rotten Tomatoes**: Rotten Tomatoes rating from critics (from 0-100%)
* **Metacritic**: Metacritic rating from critics (from 0.0-100.0)
* **totalSeasons**: Number of seasons, if applicable

## The Broad Strokes: Big Picture Organization

As a first step, you'll want to familiarize yourself with the data and organize it at a high-level. Check off the big ticket items - get rid of any excess data, set a custom index, give the columns more apropos names, sort the data, etc.. This makes handling the lower-level tasks (i.e. reformatting the data within a specific column) much easier.

Let's get to it. Import your libraries:

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

print('import successful')
```

Now, load the data and make a copy. We'll also set "imdbID" as the custom index like we did in the last section, but this time we'll do it by passing it into `.read_csv()`'s `index_col` parameter.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb_4500.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

Preview the data:

```python
movies.iloc[25:50]
```

## Renaming Columns

Here's a summary of the amount and type of data available per column:

```python
movies.info()
```

A lot of these movies are tagged under multiple genres and are available in multiple languages. We'll rename those columns to reflect this. 

*`df.rename(columns={'old_name': 'new_ name'}, inplace=False)`*

>>**NOTE!** Many Pandas functions have an `inplace` parameter that allows you to specify whether you want the function to change the object without having to reassign the output to a variable. The default argument is usually False.

```python
movies.rename(columns={'Genre': 'Genres', 'Language': 'Languages'}, inplace=True)
movies.columns
```

## Sorting

More popular and/or well-known movies should have the most thorough data, so we should sort by highest to lowest rating. `imdbRating` offers the most complete set of rating data for this sample of movies, so sort by `imdbRating` first. This also conveniently aligns better with our index, since we're using `imdbID` as a unique identifier.

1. You can use `.sort_values()` on both dataframes and Series objects. For dataframes, the `by` parameter takes one or more columns. It will sort by the first column passed, then the second, and so on. (Since a Series is effectively a single column, the `by` parameter isn't required when sorting a Series object.) Since multiple movies probably share the same rating, let's add `Title` as a second level to the sorting specs. 

*`.sort_values(by, ascending=False, inplace=False, na_position='last')`*

```python
movies.sort_values(by=['imdbRating', 'Title'], ascending=False, inplace=True, na_position='last')
```

2. If you're sorting based on multiple columns, you have the option to specify the order in which to sort each column. Let's say you pass in `by=[col1, col2], ascending=[True, False]`. This would sort the rows based on the values in col1 in **ascending** order, THEN sort by the values in col2 in **descending** order. We want `imdbRating` highest to lowest, then `Titles` alphabetically, so we'll pass the default argument of `False` to `ascending`.

3. Again, we set `inplace` to `True`.

4. If any of the columns you pass to the `by` parameter contain null values, you can choose whether to place those rows `'first'` or `'last'` using the `na_position` parameter.

Run this cell to see the results of our sort:

```python
movies.head()
```

## Filtering

Often, you will want to filter an object based on one or more conditions. To return a view of that object containing only the rows that meet your condition or conditions, you place your conditional inside the `object[]` notation. 

For instance, let's say you want to find out if your favorite movie is in this sample. You probably don't know its imdbID off-hand, so you can use an **exact match** filter to find all movies with that title.

```python
movies[movies['Title'] == 'The Intouchables']
```

You have extra flexibility for columns containing strings. Pandas extends certain methods for string data types to these Series objects. For example, this returns all the movies that contain "Avengers" in the title:

```python
movies[movies.Title.str.contains('Avengers')]
```

### Remove TV Shows from Movie Data

Right now, filtering can help us remove TV shows from our movie data. The `Type` and `totalSeasons` columns hint that multiple types of audiovisual content exist in this dataset.

*First*, we'll use `.nunique()` to look at the number of unique values in the `Type` column to see what the categories in this OMDb dataset are. *Then*, we'll count the instances of each unique category in `Type` by applying the `.value_counts()` method.

```python
print(movies['Type'].nunique())
movies['Type'].value_counts()
```

As you can see, From this, we see that there are 31 rows categorized as "series". **(We'll refer to them as TV shows to avoid confusion with Pandas Series objects!)**

Similarly, `.unique()` will show us all the unique values `totalSeasons`. Unless the only non-null value is 0, we can infer that rows with some number of seasons are TV shows, not movies. Then, `.count()` can tell us how many rows contain one of these non-null values for the `totalSeasons` column.

```python
print(movies['totalSeasons'].unique())
movies['totalSeasons'].count()
```
Hmmm... the results from our investigation of the `Type` column suggest that there are 31 TV shows, while the results from `totalSeasons` suggest that there are only 27 TV shows. Let's use filters to look at these specific rows.

1. `non_movies`: The first filtered dataframe should include rows where `Type` equals `'series'`.

```python
non_movies = movies[movies['Type'] == 'series']
len(non_movies)
```

2. `has_seasons`: The second dataframe should include all rows containing non-null data for `totalSeasons`. 

We can find this by passing this column to `pd.notnull()`. This function returns the Series, replacing each value with a boolean indicating whether or not the value is null, or `NaN`. (In the case of `pd.notnull()`, `True` refers to non-null values, while `False` refers to null values.) By passing this into the filter syntax for the `movies` dataframe, we get a version of `movies` that the filter returns only the rows that have non-null values in the `totalSeasons` column.

**NOTE!** The converse of `pd.notnull()` is of course `pd.isnull()`.

```python
has_seasons = movies[pd.notnull(movies['totalSeasons'])]
len(has_seasons)
```

Printing out the lengths of `non_movies` and `has_seasons` confirms that we wrote the filters correctly. They match the counts we got above: 31 and 27 respectively.

So where's the difference coming from? If we look at `.info()` for `non_movies`, you'll see that 4 of the rows where `Type` is `'series'` have `NaN` values in the `totalSeasons` column. As such, we can safely assume that the `non_movies` dataframe contains all the TV shows in our original `movies` dataframe. 

```python
non_movies.info()
```

## Dropping Rows & Columns

Now that we've identified and isolated all the TV shows, we should drop those rows.

*`df.drop(labels=None, columns=None, inplace=False)`*

Since they're rows, we pass the indeces from the `non_movies` dataframe as `labels` keyword argument and set `axis = 0`. Afterwards, we can use `.value_counts()` on the `Type` column again to check that there are no TV shows in the `movies` dataframe anymore.

```python
non_movie_ids = list(non_movies.index)
movies.drop(labels=non_movie_ids, axis=0, inplace=True)

movies['Type'].value_counts()
```

While we're at it, let's drop all the columns we're sure we won't need from this point on. We simply pass those to the `column` parameter of `.drop()` and use `.columns` to check our work.

```python
movies.drop(columns=['Type', 'totalSeasons', 'Ratings', 'DVD', 'Awards', 'Internet Movie Database', 'BoxOffice', 'Production', 'Poster', 'Website', 'Response'], inplace=True)
movies.columns
```

Alternatively, there is a way we can simultaneously drop certain columns and reorder the columns that remain. It's essentially another filter.

```python
# REORDERING COLS
movies = movies.copy()
movies = movies[['Title', 'Year', 'Genres', 'imdbRating', 'imdbVotes', 'Rotten Tomatoes', 'Metascore', 'Country', 'Languages', 'Runtime', 'Director',
       'Writer', 'Actors', 'Plot']]
movies.columns
```

## Counting & Dropping Duplicate Values

Having duplicate movies can alter our analysis of the dataset. The `.duplicated()` method returns a dataframe of booleans indicating whether each row is a duplicate (i.e. `True`) or not. Chaining the `.sum()` method to `.duplicated()` further summarizes this by returning the count of the `True` rows.

*`.duplicated(subset=None)`*

When finding/counting dups, you can choose to consider a `subset` of columns or check whether entire rows are the same across all columns. That gives us some flexibility for how we want to define "duplicate" in the context of our dataset and analysis. Below are the counts for 3 different definitions of "duplicate" in the context of our data:

1. `num_dup_rows`: row with the same values for all columns
2. `num_dup_titles`: rows with the same Title
3. `num_dup_title_yr`: rows with the same Title and Year combination

```python
num_dup_rows = movies.duplicated().sum()
num_dup_titles = movies.duplicated(subset=['Title']).sum()
num_dup_title_yr = movies.duplicated(subset=['Title', 'Year']).sum()

print(f'''
{num_dup_rows}
{num_dup_titles}
{num_dup_title_yr}
''')
```

The counts for the first and third definition of "duplicate" are nearly the same. We can start by employing the `.drop_duplicates()` method to drop fully duplicated rows.

*`.drop_duplicates(subset=None, inplace=False)`*

```python
print('# Dup Rows Before:', num_dup_rows)
movies.drop_duplicates(inplace=True)
print('# Dup Rows After:', movies.duplicated().sum())
```

>>**Note!**: If you run this cell more than once, the before and after lengths will be equal because you already dropped the dups.

Let's look at that extra duplicate for Title/Year:

```python
movies[movies.duplicated(subset=['Title', 'Year'])]
```

It's "The Cave", 2019. So let's look at all the rows where `Title` is "The Cave":

```python
movies[movies.Title == 'The Cave']
```

As expected, there are two rows with this Title/Year combination. The version with an id of `'tt8726180'` has less data, so let's drop that one. We can use a conditional to check whether that id is still in the dataframe after we try to drop it.

```python
print('tt8726180' in movies.index)
movies.drop('tt8726180', inplace=True) # it infers axis=0 here
'tt8726180' in movies.index
```

## Functions Featured

Functions featured include (in order of appearance):
* `.rename(columns={'old_name': 'new_ name'}, inplace=False)`
* `df.sort_values(by=[col1, col2, etc.], ascending=False, inplace=False)`
* `Series.str.contains()`
* `.nunique()`
* `.value_counts()`
* `.unique()`
* `.count()`
* `pd.notnull()`
* `df.drop(labels=None, columns=None, inplace=False)`
* `.duplicated(subset=None, keep='first')`
* `.sum()`
* `.drop_duplicates(subset=None, keep='first', inplace=False)`


## 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

*TBD*
