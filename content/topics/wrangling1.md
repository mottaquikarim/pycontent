# Data Wrangling I - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

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

Similarly, 

```python
print(movies['totalSeasons'].count())
movies['totalSeasons'].value_counts()
```

```python
non_movies = movies[movies['Type'] == 'series']
has_seasons = movies[pd.notnull(movies['totalSeasons'])]

print(len(non_movies), len(has_seasons))
```

```python
non_movies.info()
```

As you can see, 4 of these have `nan` values. # 4 have nan values, meaning `non_movies` includes all the rows that are in `has_seasons` so dropping non_movies suffices

## Dropping Rows & Columns

```python
non_movie_ids = list(non_movies.index)
movies.drop(labels=non_movie_ids,axis=0,inplace=True)

movies['Type'].value_counts() # check
```

```python
movies.drop(columns=['Type', 'totalSeasons', 'Ratings', 'DVD', 'Awards', 'Internet Movie Database', 'BoxOffice', 'Production', 'Poster', 'Website', 'Response'], inplace=True)
movies.columns
```

```python
# REORDERING COLS
movies = movies.copy()
# get rid of Released, IMDb, Metacritic
movies = movies[['Title', 'Year', 'Genres', 'imdbRating', 'imdbVotes', 'Rotten Tomatoes', 'Metascore', 'Country', 'Languages', 'Runtime', 'Director',
       'Writer', 'Actors', 'Plot']]
movies.columns
```

## DUPLICATES
 
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

```python
print('# Dup Rows Before:', num_dup_rows)
movies.drop_duplicates(inplace=True)
print('# Dup Rows After:', movies.duplicated().sum())
```

```python
movies[movies.duplicated(subset=['Title', 'Year'])]
```

```python
movies[movies.Title == 'The Cave']
```

```python
print('tt8726180' in movies.index)
movies.drop('tt8726180', inplace=True) # it infers axis=0 here
'tt8726180' in movies.index
```

```python
dup_titles = movies[movies.duplicated(subset=['Title'])]
len(dup_titles)
```

## Key Takeaways

>>* Functions featured include (in order of appearance):
    >>* `.rename(columns={'old_name': 'new_ name'}, inplace=False)`
    >>* `df.sort_values(by=[col1, col2, etc.], ascending=False, inplace=False)`
    >>* `Series.str.contains()`
    >>* `.nunique()`
    >>* `.value_counts()`
    >>* `.count()`
    >>* `pd.notnull()`
    >>* `df.drop(columns, inplace=False)`
    >>* `.()`
    >>* `.()`
    >>* `.()`
    >>* `.()`
    >>* `.()`
    >>* `.()`
    >>* `.()`
    >>* `.()`