# Accessing Data

Before we get into any sort of data analysis, we need to understand the most basic code for loading, summarizing, and selecting data. This is a lot of memorizing "one-and-done" examples. But! Once we get past that, we will have the flexibility to learn via a contextual analysis of a single dataset. Let's take a look at that dataset now.

## Data Dictionary

When you analyze a set of data, always include a `data dictionary`, or a list of variable definitions, alongside your notebook. It can serve as a contextual overview of the variables in the dataset as well as share information about how certain variables are formatted. If you're looking to study a dataset yourself, the data dictionary can also give you high-level ideas for what you might want to analyze and how.

Our dataset contains movie metadata that we pulled from the [OMDb API](http://www.omdbapi.com/). Below is the data dictionary for the *unaltered OMDb data*. If it seems disorganized and convoluted... that's because it is! The fields and formats here are the original ones obtained straight from the OMDB API. In order to wrangle this data for our purposes, we have to first clean it ourselves. (That said, the OMDb dataset does have a few pretty self-explanatory variables, so we've left some definitions blank.)

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

## Reading & Writing Data

Before we load any data, we have to import all the libraries we'll use throughout the next few units.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Reading and writing data to and from your notebook primarily relies on the format and location of your data. The general syntax is:

* **Read:** `pd.read_<format>(<path>)`
* **Write:** `pd.to_<format>(<path>)`

*Notice how saving your data uses pd.to_<format> and NOT pd.write_.* For the syntax of how to load the most common data types, you can reference ==**this (URL TBD) section**== of our Pandas Cheat Sheet. 

There are a number of optional parameters you might want or need to use. A quick exaplanation of the most useful ones are:

* `sep`: By default, ','
You can specify the character that delimits the values so that Pandas can recognize it.
* `header`: By default, Pandas infers the headers.
If you know there is no header row, you should pass `False` and pass a list of column names to the `names` parameter.
* `names`: (see "header	" above)
* `index_col`: By default, `None` and Pandas will use a 0-based numerical index for the `Index` labels. If you want to use one (or more) of the columns as the index for axis 0 (the rows), specify them here.
* `usecols`: If you want only a subset of columns loaded, indicate which ones here.
* `nrows`: By default, Pandas loads the full file. If you want only a subset of the data, you can specify a number of rows to load.

#### Loading the OMDb Dataset

Since this is our first time looking at it, let's load the OMDb dataset as is. 

```python
omdb_orig = pd.read_csv('omdb_5000.csv')
movies = omdb_orig.copy()
```
It's also a helpful practice to immediately make a hard copy of the dataset so that, at any time, you can your data to the original dataset. You can make a shallow copy (see below), but it's always better to the `.copy()` method.

>> Warning! [SettingWithCopyWarning](https://www.dataquest.io/blog/settingwithcopywarning/) ==<-- **important article to read!!**==

## Summarizing Data

#### Metadata

Typically, the first thing you'll want to do is use the `.info()` method to see a summary of the data in your dataframe. This will tell you things like how many rows there are, what datatype each column Series contains, and how many non-null values are in each column.

```python
movies.info()
```
Sometimes you'll want to grab some of this information individually though. To return all the column names, you can use `.columns`... 

```python
movies.columns
```
...and `len(df)` returns the number of rows in a dataframe. For a Series, `len(series)` gives the number of items in the array. Similarly, `.size` and `.shape` give the number of elements in the object and the dimensions of the object. Check these out:

```python
print(
'Length:', len(movies), 
'\nSize:', movies.size, 
'\nShape:', movies.shape
)
```
By now, you'll probably want to preview the data itself

#### Data Preview

`.head(n)` and `.tail(n)` will return the first and last *n* rows of data respectively. If you don't pass in a number, they will both return 5 rows by default.

```python
movies.head() 
```

```python
movies.tail(3) 
```

In this column, we can see that we have an existing unique ID for each movie - the IMDb ID. Especially because IMDb is the most well-known movie database, we should make `imdbID` the index.

```python
movies.set_index(['imdbID'], inplace=True)
movies.head(3)
```
By default, the `drop` parameter in the `.set_index()` function is `True`. As you can see above, `imdbID` no longer exists as a column in the dataframe. It has been converted into an `Index` object.

If you ever want to go back to the default numerical `Index` labels, you can use `.reset_index()`. It will simply add the custom `Index` object back to the dataframe as a column Series.

```python
movies.reset_index(inplace=True)
movies.tail()
```
>>Warning!

>>Be careful with `.reset_index()`. If you accidentally rerun this cell, it will add the generic 0-based index to the dataframe as a *column*.

Now, let's set the index back to `imdbID`.

```python
movies.set_index(['imdbID'], inplace=True)
```

## Selecting Data



For most other pieces of data that you want to select, you will use some variation of `.loc[]` or `.iloc[]`. Before we go into specific examples, it's important to understand the difference between these two functions: 

* **`.loc[]`** selects and returns data by passing index **LABELS** as arguments
* **`.iloc[]`** selects and returns data by passing index **POSITIONS** as arguments

### Series

Select a single value by its
* **`obj.s[idx_label]`** -- index label
* **`obj.s[idx]`** -- index position


### Columns

Dataframe columns are the easiest and most flexible pieces of data to select and maneuver...

Select a single column as a Series

```python
print(type(movies['Title']), '\n')
movies['Title']
```

Returns multiple columns (in any order) as a new DataFrame

```python
movies[['Title',  'Genre', 'Director', 'Actors']]
```

### Rows
.loc vs. iloc


### Cells

.loc vs. iloc


==Select a:
* Row
* Column
* Single item from a specific row, column
* Slice of Rows
* Subset of columns (return as a new df)
* Slice of series values (by index and by label)==

* **`df[col]`** -- returns one column as a Series


* **`df[[col_label, col2]]`** -- Returns multiple columns (in any order) as a new DataFrame


* Select a single item (i.e. a value from a Series or a row from a Dataframe)...
    * **`obj.loc[idx_label]`** -- by its index label
    * **`obj.iloc[idx]`** -- by its index position

* Select a single value in a DataFrame...
    * **`df.loc[row_label, col_label]`** -- by row & column index label
    * **`df.iloc[row_idx, col_idx]`** -- by row & column index label position


* Returns a slice of rows as a new DataFrame by entering a range of...
    * **`df.loc[row_start : row_end]`** -- index labels
    * **`df.loc[row_start : row_end]`** -- index labels

* Select a slice of a DataFrame by entering a range of row and column...
    * **`df.loc[row_start : row_end , col_start : col_end]`** -- index labels
    * **`df.iloc[row_start : row_end , col_start : col_end]`** -- index positions



## Iterating Through Data