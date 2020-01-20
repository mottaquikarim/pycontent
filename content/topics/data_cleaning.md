# Data Cleaning

## Objectives

>>* Converting data types en masse
>>* Reformatting Strings to Lists & Numbers
>>* Scaling variables
>>* 
>>* Map
>>* Apply

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

## Mapping Strings to Lists

### Genres

```python
missing_genre = movies[pd.isnull(movies['Genres'])]
print(movies['Genres'].isnull().sum())
missing_genre
```



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

### Convert Year to Integer

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



```python
# NEED TO MAP LANGUAGES NOW THAT THIS IS FIXED
```



```python

```



```python

```


```python

```



```python

```



```python

```



```python

```



```python

```



```python

```



```python

```



```python

```

