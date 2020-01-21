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

### Typecasting

Typecasting a Series is one of the most basic elementwise functions. Most commonly in cleaning your data, you'll use:

* `pd.to_numeric(s)`: typecast the items in a Series to ints or floats; will infer which numeric type is best
* `s.astype()`: typecast the items in a Series to some data type; accepts `'int64'`, `'float64'`, `'str'`, etc.

Let's test these out quickly on the `Year` column. What data type is it now?

```python
test_year = movies['Year'].copy()
print(type(test_year[0]))
```

Convert it to string type using `.astype()`.

```python
test_year = test_year.astype('str')
type(test_year[0])
```

Convert it to one of the numeric types using `pd.to_numeric(s)`.

```python
test_year = pd.to_numeric('int64')
type(test_year[0])
```

### The `.map()` function

For the next few example, we'll leverage the `Series.map(arg, na_action=None)` function, another **elementwise** function. You can use the `.map(arg, na_action=None)` function to substitute or transform each value in a Series with another value. `.map()` itself serves to pass along "instructions" for how to manipulate each element in the Series. Accordingly, the `arg` parameter will accept single-argument functions, dicts, or Series. As you might imagine, `.map()` requires us to pass it a "mapping" for the before and after values.


| Type of `arg` |    Map From   |    Map To    |
|:-------------:|:-------------:|:------------:|
|   Function    |  1 Parameter  | Return Value |
|     Dict      |      Key      |     Value    |
|    Series     |     Index     |     Value    |


By default, if there are null values in the original Series, an error will stop your `.map()` function's execution. The `na_action` parameter allows you to bypass this issue until you decide what how to handle different pieces of missing data in your dataset. If you set `na_action='ignore'`, `.map()` will simply skip over null values.

### Mapping Strings to Lists

The `Genres`, `Country`, and `Languages` columns often hold more than one value per row. But when we pulled this data from the API, we got the contents of each cell in the form of a single string with the values separated by commas. If we want to evaluate the different categories within each of these variables, we need to break out the individual values from the string into list format.

### Genres

Count and view the rows with missing `Genres` data:

```python
missing_genre = movies[pd.isnull(movies['Genres'])]
print(movies['Genres'].isnull().sum())
missing_genre
```

We could pass `na_action='ignore'`, but since there are only 3, we might as well look them up and fill in the info ourselves. We can check this by making sure the count of nulls afterward is 0.

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

Now, let's make a copy of the `Genres` column to operate on.

```python
temp_genre = movies['Genres'].copy()
```

To turn each string into a list, all we have to do is split each string at the commas. But we have to pass `.map()` a function for this, remember? For brevity, whenever possible, most people use **lambda functions** with `.map()`. A **lambda function** is a nameless function that is defined, used, and forgotten in one line. Here's the syntax relative to a regular function.

```python
"""
def split_list(x):
    return x.split(',')

...equivalent to...

lambda x: x.split(',')
"""
```

Now we can map the `Genres` variable using `lambda x: x.split(',')`.

```python
temp_genre = temp_genre.map(lambda x: x.split(','))
temp_genre
```

Reassign the original column to our manipulated Series.

```python
movies['Genres'] = temp_genre
movies['Genres']
```

### Country

We can do the same for the `Country` variable. First, check how many null values there are.

```python
null_country = movies[pd.isnull(movies['Country'])].copy()
print(movies['Country'].isnull().sum())
null_country
```

None, so we can proceed right away with copying the column.

```python
temp_country = movies['Country'].copy()
```

Use the same mapping strategy of `lambda x: x.split(',')`.

```python
temp_country = temp_country.map(lambda x: x.split(','))
temp_country
```

Reassign the original column to our manipulated Series.

```python
movies['Country'] = temp_country
movies['Country']
```

### Languages

Finally, we'll repeat this with `Languages`. 

```python
null_lang = movies[pd.isnull(movies['Languages'])].copy()
print(movies['Languages'].isnull().sum())
null_lang
```

There are 4 movies with `NaN` in their `Languages` field. But do you notice anything? The first movie with sound was The Jazz Singer, released in 1927. All four of these movies were released before that year. So here's what we'll do...

First, map the rest of the values as planned by setting `na_action='ignore'`

```python
temp_lang = movies['Languages'].copy()

temp_lang = temp_lang.map(lambda x: x.split(','), na_action='ignore')
temp_lang
```

```python
movies['Languages'] = temp_lang
movies['Languages']
```

Next, filter to find all the movies made before 1927...

```python
silent_films = movies[movies['Year'] < 1927].copy()
silent_films
```

...and change their `Language` value to "Silent".

```python
silent_list = list(silent_films.index)

for film in silent_list:
    movies.loc[film, 'Languages'] = 'Silent'
```

Now look:

```python
movies[movies['Year'] < 1927]
```

### Scaling Variables

* `imdbRating`: 0.0-10.0; float format
* `Metascore`: 0.0-100.0; float format
* `Rotten Tomatoes`: 0-100%; string format

## Reformatting Strings to Numbers













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

