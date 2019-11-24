# Accessing Data

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will learn Pandas by integrating it into a contextual data analysis. Instead of reviewing groups of similar functions, we will apply various functions based on how and when we need them.

This might get a little confusing, so brace yourself! To help keep things as consistent as possible, we'll use the same dataset across units. Ultimately, this contextual approach will help you apply the material on your own much more easily.

## Data Dictionary

==FILL LATER==
OMDb API to pull movie metadata

Always include a data dictionary alongside your notebook. It can serve as a contextual overview of the variables in the dataset as well as sharing information about how certain variables are formatted.

Below is the data dictionary for the *unaltered OMDb data*. The formats here are the original ones obtained from the OMDB API as it exists before *
The OMDb dataset has pretty self-explanatory variables, so we've left some definitions blank.

* Title
* Year: Year the movie was made
* Rated: MPAA content rating (e.g. PG, NC17, R, etc.)
* Released: Date the movie was released to the public
* Runtime: How long in number of minutes 
* Genre: One or more genres that describe the movie* 
* Director*
* Writer*
* Actors*
* Plot
* Language
* Country
* Awards*
* Poster: Amazon-hosted image url for the poster of the movie
* Ratings: Series containing ratings from multiple sources (e.g. Rotten Tomatoes)
* Metascore: Metacritic rating from critics
* Rotten Tomatoes: Rotten Tomatoes rating from critics 
* imdbRating: Crowd-sourced audience rating from IMDb
* imdbVotes: Number of user ratings from IMDb
* imdbID: Unique movie ID from IMDb
* Type: Content category ==(e.g. movie, tv, etc.)==
* DVD
* BoxOffice
* Production
* Website: url
* Response: 

Runtime', 'Genre', 'Director',
       'Writer', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster',
       'Ratings', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type',
       'DVD', 'BoxOffice', 'Production', 'Website', 'Response',
       'Internet Movie Database', 'Rotten Tomatoes', 'Metacritic',
       'totalSeasons'


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