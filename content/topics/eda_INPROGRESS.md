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

3. Use the `.explode()` function, setting `ignore_index=True`.

```python
# 3.
movie_genres = movie_genres.explode('Genre', ignore_index=True)

movie_genres.head()
```

Take note of the movie IDs and see how their data got spread out after we applied `.explode()`. 

Next, we'll repeat this for `Languages`, `Countries`, and `Actors`. Afterwards, we'll drop all the columns we exploded from the main dataframe to keep it uncluttered.

```python

```



```python

```



```python

```












