# Data Wrangling I

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.

## Objectives

>>* Document metadata based on common standards
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

### Add, Drop, & Rename Columns

Here are all the column names in the original data:

```python
print(f'BEFORE: \n{movies.columns}')
```

Adding a column to the data is just like declaring a variable: `movies['Average Rating'] = <series_data>`

>>can add actual Series data as long as it's the same length

```python
movies.rename(columns={'Genre': 'Genres', 'Language': 'Languages'}, inplace=True)
movies.columns
```

>>SORTING

```python
movies.sort_values(by=['imdbRating', 'Title'], ascending=False, inplace=True, na_position='last')
```

>>FILTERING (removing non-movies)

    >>what's your fave movie?
    `movies[movies.Title.str.contains('Nosferatu')]`
    `.isin()`
    `Title ==`

```python
print(movies['Type'].nunique())
movies['Type'].value_counts()
```

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

>>DROPPING ROWS/COLS

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

>> DUPLICATES
 
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

>> MAP() List to Str
>> Genre, Language, Country

```python
missing_genre = movies[pd.isnull(movies['Genres'])]
print(movies['Genres'].isnull().sum())
missing_genre
```

```python
genre_updates = {
    'tt8026554': 'Drama',
    'tt6215446': 'Comedy, Horror', # Ghost Light
    'tt10084752': 'Documentary'
}

for imdbID, genre in genre_updates.items():
    movies.loc[imdbID, 'Genres'] = genre

print(movies['Genres'].isnull().sum())
```

```python
temp_genre = movies['Genres'].copy()
```


```python
temp_genre = temp_genre.map(lambda x: x.split(','))
temp_genre
```


```python
movies['Genres'] = temp_genre
movies['Genres']
```

    >>Country
    >>Languages

>>Reformat Str to Numbers

>>CONVERT DATATYPE (Year to Int)

```python
year = movies['Year']
type(year[0])
```

```python
movies['Year'] = pd.to_numeric(year)
```

```python
silent_films = movies[movies['Year'] < 1927].copy()
silent_films
```


```python
silent_list = list(silent_films.index)

for film in silent_list:
    movies.loc[film, 'Languages'] = 'Silent'
```


```python
silent_films = movies[movies['Year'] < 1927].copy()
silent_films
```

>>Scale imdbRating to match Metascore

```python
movies[movies.imdbRating.isnull()]
```

```python
"""
test = movies['imdbRating']*10
test
"""

movies['imdbRating'] = movies['imdbRating'].map(lambda x: x*10)
movies.head()
```

>>Reformat Runtime 

```python
missing_runtime = movies[pd.isnull(movies['Runtime'])]

print(len(movies))
len(missing_runtime)
```

```python
movies.dropna(subset=['Runtime'], inplace=True)
```

```python
missing_runtime = movies[pd.isnull(movies['Runtime'])]

print(len(movies))
len(missing_runtime)
```

```python
temp_runtime = movies['Runtime'].copy()
temp_runtime.head(3)
```

```python
def runtime_reformat(row):
    """remove min from str and convert field to int"""
    try:
        split_row = row.split(' ')
        numeric_runtime = int(split_row[0])
        #print(numeric_runtime, type(numeric_runtime))
        return numeric_runtime
    except Exception as e:
        # if pd.isnull(row), error will occur
        # print(e)
        return row

temp_runtime = temp_runtime.apply(runtime_reformat)
temp_runtime
```

```python
movies['Runtime'] = temp_runtime.astype('int64')
movies['Runtime']
```

>>Filter/Drop Shorts

```python
shorts = movies[movies['Runtime'] < 45].copy()
shorts.sort_values(by=['Runtime'], ascending=False, inplace=True)
print(len(shorts))
shorts = list(shorts.index)
shorts
```

```python
movies.drop(labels=shorts, axis=0, inplace=True)
movies[movies['Runtime'] < 45].copy()
```

>>Reformat imdbVotes

```python
movies.to_csv('omdb_ratings_eval.csv')
```


```python
def votes_reformat(row):
    """remove commas from str and convert field to int"""
    try:
        split_row = row.split(',')
        votes = int(''.join(split_row))
        return votes
    except Exception as e:
        # if pd.isnull(row), error will occur
        # print(e)
        return row

temp_imdbVotes = movies['imdbVotes'].copy()
temp_imdbVotes = temp_imdbVotes.apply(votes_reformat)
temp_imdbVotes
```

```python
movies['imdbVotes'] = temp_imdbVotes.astype('int64')
```



>>Reformat Rotten Tomatoes
    >>fillna now?
    >>have to sep and re-concat nulls?

```python
temp_rt = movies['Rotten Tomatoes'].copy()
temp_rt.isnull().sum()
```


```python
def strip_rt(row):
    try:
        stripped = int(row.strip('%'))
        return stripped
    except Exception as e:
        # print(e)
        return row
        
temp_rt = temp_rt.apply(strip_rt)
temp_rt
```

>>FILL/DROP NULLS????

```python
#temp_rt_mean = temp_rt.mean()
#print(f'Mean: {temp_rt_mean}\n')
#temp_rt.fillna(temp_rt_mean, inplace=True)
#temp_rt
```


```python
movies['Rotten Tomatoes'] = temp_rt.round(1)
movies.head(3)
```


```python

```


```python

```


```python

```


```python

```

