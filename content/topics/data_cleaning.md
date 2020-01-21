# Data Cleaning

## Objectives

>>* Converting data types en masse
>>* Reformatting Strings to Lists & Numbers
>>* Scaling variables
>>* Elementwise functions with .map()
>>* Row- & Column-wise functions with .apply()

### Import

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
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_cleaning.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

## Elementwise Functions with `.map()`

An **elementwise** function is one that you call on a Series object as a whole, but that vectorizes the functions actions across each of the Series elements. 

### Convert Year to Integer

```python
year = movies['Year']
type(year[0])
```


```python
movies['Year'] = pd.to_numeric(year)
```


### The `.map()` function

For the next few example, we'll leverage the `Series.map(arg, na_action=None)` function, another **elementwise** function. You can use the `.map(arg, na_action=None)` function to substitute or transform each value in a Series with another value. `.map()` itself serves to pass along "instructions" for how to manipulate each element in the Series. Accordingly, the `arg` parameter will accept single-argument functions, dicts, or Series. 

By default, if there are null values in the Series, an error will stop your `.map()` function's execution. The `na_action` parameter allows you to bypass this issue until you decide what how to handle different pieces of missing data in your dataset. If you set `na_action='ignore'`, `.map()` will simply skip over null values.

### Mapping Strings to Lists

The `Genres`, `Country`, and `Languages` columns often hold more than one value per row. But when we pulled this data from the API, we got the contents of each cell in the form of a single string with the values separated by commas. If we want to evaluate the different categories within each of these variables, we need to break out the individual values from the string into list format.

### Genres

Count and view the rows with missing `Genres` data:

```python
missing_genre = movies[pd.isnull(movies['Genres'])]
print(movies['Genres'].isnull().sum())
missing_genre
```

We could pass `na_action='ignore'`, but since there are only 3, we might as well look up how to 


```python
genre_updates = {
    'tt8026554': 'Drama',
    'tt6215446': 'Comedy, Horror',
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

### Country

```python
null_country = movies[pd.isnull(movies['Country'])].copy()
print(movies['Country'].isnull().sum())
null_country
```

No dups, so we can proceed right away.


```python
temp_country = movies['Country'].copy()
```



```python
temp_country = temp_country.map(lambda x: x.split(','))
temp_country
```



```python
movies['Country'] = temp_country
movies['Country'].unique()
```

### Languages

```python
null_lang = movies[pd.isnull(movies['Languages'])].copy()
print(movies['Languages'].isnull().sum())
null_lang.sort_values(by=['Rotten Tomatoes'], inplace=True)
null_lang
```



```python
# movies[movies['Year'] < 1927]
print('^ This will return an error.')
```

^^ have to convert year to number first, so let's do that now... and then fix all the silent films 



## Reformatting Strings to Numbers





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



```python
temp_lang = movies['Languages'].copy()
temp_lang = temp_lang.map(lambda x: x.split(','))
temp_lang
```



```python
movies['Languages'] = temp_lang
movies['Languages']
```


### Scale imdbRating to Match Metascore


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

### Reformat Runtime



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

### Filter/Drop Shorts



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


### Reformat imdbVotes



```python
movies.info()
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

### Reformat Rotten Tomatoes


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

