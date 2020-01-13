# Data Wrangling I

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.

## Objectives

* Document metadata based on common standards
* Add, drop, & rename columns 
* Sort the data
* Count & drop duplicate rows
* Count & drop rows with null values
* Filter the data

>>* Find & replace data
>>* Reformat
>>* Normalize 

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
* **Language**
* **Country**
* **Awards**: # of nominations and # of wins for one or more types of awards
* **Poster**: Amazon-hosted image url for the poster of the movie
* **Ratings**: Series containing ratings from multiple sources (e.g. Rotten Tomatoes)
* **Metascore**: Metacritic rating from critics
* **imdbRating**: Crowd-sourced audience rating from IMDb
* **imdbVotes**: Number of user ratings from IMDb
* **imdbID**: Unique movie ID from IMDb
* **Type**: Content category ==(e.g. movie, tv, etc.)==
* **DVD**: Date the movie was released to DVD
* **BoxOffice**: Box office earnings in US dollars
* **Production**: Production company
* **Website**: URL
* **Response**: Boolean stored as string, indicates whether the API response was valid
* **Internet Movie Database**: Crowd-sourced audience rating from IMDb out of 10
* **Rotten Tomatoes**: Rotten Tomatoes rating from critics 
* **Metacritic**: Metacritic rating from critics
* **totalSeasons**: Number of seasons, if applicable

## The Broad Strokes: Big Picture Organization

As a first step, you'll want to familiarize yourself with the data and organize it at a high-level. Check off the big ticket items - get rid of any excess data, set a custom index, give the columns more apropos names, sort the data, etc.. This makes handling the lower-level tasks (i.e. reformatting the data within a specific column) much easier.

Let's get to it. Import your libraries:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Load the data and make a copy:

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb_5000.csv')
movies = omdb_orig.copy()
print('data loaded successfully')
```

We'll also set "imdbID" as the custom index like we did in the last section.

```python
movies.set_index('imdbID', inplace=True)
```

### Add, Drop, & Rename Columns

Adding a column to the data is just like declaring a variable:

```python
movies['Average Rating'] = pd.Series() # can add actual Series data as long as it's the same length
movies.iloc[57:59]
```

Here are all the column names in the original data:

```python
print(f'BEFORE: \n{movies.columns}')
```


```python
print(f'BEFORE: \n{movies.columns}')
movies.rename(columns={'Internet Movie Database': 'IMDb', 'Genre': 'Genres', 'Language': 'Languages', 'Writer': 'Writers'}, inplace=True)
print('\nAFTER:')
movies.iloc[20]
```

```python

```

```python

```

```python

```

### Sorting

You can sort a Series or dataframe by different ==ELEMENTS== and specs with the `.sort_values()` method. Its general syntax and default parameter arguments (where applicable) are as follows:

`.sort_values(by, axis=0, ascending=False, inplace=False, na_position=last)`

The `by` parameter takes one or more columns from the dataframe. The method will sort by the first column passed, then the second, and so on. Since a Series is effectively a single column, the `by` parameter isn't required when sorting a Series object.

If you're sorting based on multiple columns, you have the option to specify the order in which to sort each column. Let's say you pass in `by=[col1, col2], ascending=[True, False`. This would sort the rows based on the values in col1 in **ascending** order, THEN sort by the values in col2 in **descending** order. If you only pass one argument to ascending, it will sort all the columns passed to `by` in that order.

If any of the columns you pass to the `by` parameter contain null values, you can choose whether to place those rows `first` or `last` using the `na_position` parameter.

For our movies dataset, it makes logical sense to sort the movies in order of most to least popular or well-known. We have three different movie ratings sources which can serve as a measure of that for us - IMDb, Rotten Tomatoes, & Metacritic. (The "Ratings" column is an aggregate of these, and the "Internet Movie Database" column is a duplicate of "imdbRating.") Which should we use then? If you take a look at `movies.info()`...

```python
movies.info()
```

...you'll see that IMDb has the most the non-null values


Above, are the 
```python
movies.sort_values(by=['imdbRating', 'Title'], ascending=False, inplace=True, na_position=True)
movies.head(3)
```



### Drop Duplicates
* remove duplicate imdbIDs
    * remove duplicates based on a certain col

* `df.duplicated([subset, keep])` -- Return boolean Series denoting duplicate rows

When finding dups, you can choose to consider a `subset` of columns or check whether entire rows are the same across all columns. The `keep` param denotes the occurrence which should be marked as duplicate. You can choose `first` or `last`, but the default is `first`. In other words:

* first : All duplicates except their first occurrence will be marked as True
* last : All duplicates except their last occurrence will be marked as True

**Count the number of dups**

Shows number of Trues and Falses; number of Trues is how many dups there are

```python
movies.duplicated().sum()
```

```python
movies.duplicated().value_counts()
```

whole row vs. dup titles 

```python
movies.duplicated(['Title']).value_counts()
```

**Return a new df of rows containing dups**

```python
dup_rows = movies[movies.duplicated()]

print(len(dup_rows))
dup_rows.head(5)
```

**Drop duplicates**

* `drop_duplicates([subset, keep, inplace])` -- returns DataFrame with duplicate rows removed, optionally only considering certain columns.

```python
print('ROWS BEFORE:', len(movies))

movies = movies.drop_duplicates()

print('ROWS AFTER:', len(movies))
```

Note: If you run this cell more than once, the before and after lengths will be equal because you already dropped the dups.



```python

```

### Organizing Cols

* rename cols (imdb, genres, languages)
* add / drop cols

### Remove Non-Movies

* filter out Type == video series
    * unique / nunique
    * value_counts()
    * pd.isnull / pd.notnull



## Filtering

...?

>>OUTLINE

* dropna
    * or fillna w. mean


* replace (production companies?)
* append single row vs. concat multiple rows
* merge
* update
    * single value
    * remove "min" from Runtime and cast to int so that you can do math

* iterate through Genres and separate strings to list
    * then do via .apply()
