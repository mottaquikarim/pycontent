# Accessing Data

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will learn Pandas by integrating it into a contextual data analysis. Instead of reviewing groups of similar functions, we will apply various functions based on how and when we need them.

This might get a little confusing, so brace yourself! To help keep things as consistent as possible, we'll use the same dataset across units. Ultimately, this contextual approach will help you apply the material on your own much more easily.

## Data Dictionary

==FILL LATER==
[OMDb API](http://www.omdbapi.com/) to pull movie metadata

Always include a data dictionary alongside your notebook. It can serve as a contextual overview of the variables in the dataset as well as sharing information about how certain variables are formatted.

Below is the data dictionary for the *unaltered OMDb data*. If it seems disorganized and convoluted... that's because it is! The fields and formats here are the original ones obtained straight from the OMDB API. In order to wrangle this data for our purposes, we have to first clean it ourselves. (That said, the OMDb dataset does have a few pretty self-explanatory variables, so we've left some definitions blank.)

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
* **Rotten Tomatoes**: Rotten Tomatoes rating from critics 
* **imdbRating**: Crowd-sourced audience rating from IMDb
* **imdbVotes**: Number of user ratings from IMDb
* **imdbID**: Unique movie ID from IMDb
* **Type**: Content category ==(e.g. movie, tv, etc.)==
* **DVD**: Date the movie was released to DVD
* **BoxOffice**: Box office earnings in US dollars
* **Production**: Production company
* **Website**: url
* **Response**: 
* **Internet Movie Database**: 
* **Rotten Tomatoes**: 
* **Metacritic**: 
* **totalSeasons**: Number of seasons, if applicable

## Reading & Writing Data

Before we load any data, we have to import all the libraries we'll use throughout the next few units.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Reading and writing data to and from your notebook primarily relies on the format and location of your data. The general syntax is like this:

**Read:** `pd.read_<format>(<path>)`
**Write:** `pd.to_<format>(<path>)`

*Notice how saving your data uses pd.to_<format> and NOT pd.write_.* For the syntax of how to load the most common data types, visit ==this URL TBD == section of our Pandas Cheat Sheet. As for our OMDb dataset, here is the code we will use to load it. We've included a comment underneath just to show an example of how we might save the data later.

```python
omdb_orig = pd.read_csv('omdb_5000.csv')

# pd.to_csv(headers=True)
```

==params for if there are headers or an idx?????==
It is also a helpful practice to immediately make a hard copy of the dataset so that, at any time, you can your data to the original dataset. You can make a shallow copy (see below), but it's always better to the `.copy()` method.

==SHOW THAT ANNOYING ERROR ABOUT MAKING CHANGES TO ORIGINAL DATAFRAME== 

```python
movies = omdb_orig.copy()
```

## Summarize Data 

Typically, the first thing you'll want to do is use the `.info()` method to see a summary of the amount and type of data in your dataframe. (Note: This method doesn't work for Series objects).

* `	Metascore       4713 non-null float64` means that only 4713 rows have a metascore available.
* `RangeIndex: 5788 entries` means that the dataframe has 5788 rows. 

```python
movies.info()
```

Alternatively, you could use `len(df)` to find the number of rows in a dataframe. For a series, `len(series)` gives the number of items in the array.

```python
len(movies)
```

Number of rows in a DataFrame / number of items in a Series

```python
len(movies) 
```


Size # of elements vs. tuple showing dimensions shape

```python
print(movies.shape)
movies.size
```

First rows

```python
movies.head() 
```

Last rows

```python
movies.tail() 
```

Series containing the column names

```python
movies.columns
```

Core descriptive stats about each *numerical* column

```python
movies.describe()
```

Let's say that I want to see what the "object" in the `Genre` column looks like.


```python
movies.describe()
movies['Genre'].describe()
```

## Selecting Data


.loc vs. iloc


Select a:
* Row
* Column
* Single item from a specific row, column
* Slice of Rows
* Subset of columns (return as a new df)
* Slice of series values (by index and by label)


## Iterating Through Data