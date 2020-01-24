# Data Cleaning

<img src="https://i.chzbgr.com/full/1898496256/h42C0CC42/panda-cleaning-instructions" style="margin: 0 auto; float: right;"/>

Data cleaning is arguably as important as any amount of insight you obtain from your dataset. The more data there is, especially data aggregated from multiple sources, the messier it is. You need to reformat and standardize it before you can successfully complete any real analysis. Otherwise...garbage in, garbage out...

## Objectives

* Vectorized typecasting
* Scaling variables
* Dropping null values
* Element-wise functions with .map()
* Element-wise functions with .apply()
* Row- & Column-wise functions with .apply()

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

## Element-wise Functions with `.map()`

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

For the next few example, we'll leverage the `s.map(arg, na_action=None)` function, another **elementwise** function. You can use the `.map(arg, na_action=None)` function to substitute or transform each value in a Series with another value. `.map()` itself serves to pass along "instructions" for how to manipulate each element in the Series. Accordingly, the `arg` parameter will accept single-argument functions, dicts, or Series. As you might imagine, `.map()` requires us to pass it a "mapping" for the before and after values.


| Type of `arg` |    Map From   |    Map To    |
|:-------------:|:-------------:|:------------:|
|   Function    |  1 Parameter  | Return Value |
|     Dict      |      Key      |     Value    |
|    Series     |     Index     |     Value    |


In *most* cases, if there are null values in the original Series, an error will stop your `.map()` function's execution. (We'll see the exception soon.) The `na_action` parameter allows you to bypass this issue until you decide what how to handle different pieces of missing data in your dataset. If you set `na_action='ignore'`, `.map()` will simply skip over null values.

### Mapping Strings to Lists

The `Genres`, `Country`, and `Languages` columns often hold more than one value per row. But when we pulled this data from the API, we got the contents of each cell in the form of a single string with the values separated by commas. If we want to evaluate the different categories within each of these variables, we need to break out the individual values from the string into list format.

### Genres

Count and view the rows with missing `Genres` data:

```python
missing_genre = movies[pd.isnull(movies['Genres'])]
print(movies['Genres'].isna().sum())
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

print(movies['Genres'].isna().sum())
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

### Scaling Variables

If we look at the three movie rating variables, each source has provided ratings for each movie on a different scale and in a different format. 

* `imdbRating`: 0.0-10.0; float format
* `Metascore`: 0.0-100.0; float format
* `Rotten Tomatoes`: 0-100%; string format

For graphical comparisons, you always want numeric variables on the same scale. Since it's easier to see minute differences between data points on a larger scale, we'll scale `imdbRating` to match `Metascore` and eventually Rotten Tomatoes.

First, how many movies are missing a rating from IMDb?

```python
movies['imdbRating'].isna().sum()
```

There are 5 null values, so we need to set `na_action='ignore'`, right? Nope! Here's the exception to `.map()`'s rule about null values. 

Assume `a = np.nan` (`np.nan` is the notation for a null value):

* `a.split(',')` would raise an error because you can't apply that, or any, method or function to a null value
* `a*10` will NOT raise an error because *basic mathematical operators* treat null values like 0s

Knowing this, we could easily scale `imdbRating` with `movies['imdbRating']*10`, but let's use this opportunity to prove the null value exception with `.map()`.

```python
movies['imdbRating'] = movies['imdbRating'].map(lambda x: x*10)
movies.head()
```

## Element-wise Functions with .apply()

When applied to a Series object, the `.apply()` function is effectively the same as `.map()`. It's just another elementwise function. The difference is that you can pass it more complex functions (e.g. more than one line, conditionals, error handling, etc.), while `.map()` is mainly paired with simple lambda functions.

* `s.apply()`

As with `.map()`, if there are null values in the Series, an error will stop the code's execution. However, `.apply()` has no equivalent to the `na_action` parameter in `.map()`. If you don't want to drop all the rows with null values just to get your `.apply()` function working, you can **manually** skip over null values using the same logic behind the `na_action` parameter. For example, you can build in conditional logic or a try/except statement.

### Reformat Runtime

Down to business. Right now, the `Runtime` variable is in string format. If we want to include it in any quantitative analysis or even sort based on this column, we need the values to be numeric. Fixing this won't be as simple as typecasting because each value contains non-numeric characters.

First, how many rows are missing data for `Runtime`?

```python
missing_runtime = movies[pd.isnull(movies['Runtime'])]
print(len(missing_runtime))
missing_runtime
```

There are only three, all of which are missing ratings from Rotten Tomatoes and Metascore. We might as well drop these rows, but we don't need to grab each one's index this time. (Flash back to when we removed TV shows using `movies.drop(labels=non_movie_ids, axis=0)`.) Since these three are the only rows with null values for `Runtime`, we can drop them as a group using `.dropna()`.

* `df.dropna(axis=0, how='any', subset=[col1], inplace=False)`

When you're dropping rows (i.e. axis=0), the `subset` parameters indicates which columns to check for null values. Accordingly, if you're checking for duplicates in multiple columns, the `how` parameters indicates whether you want the function to drop the row if `'any'` of those columns contain a null value or only if `'all'` of them are null.

Let's drop all rows that contain a null value in the `Runtime` column from the `movies` dataframe:

```python
movies.dropna(subset=['Runtime'], inplace=True)
```

Did it work?

```python
movies['Runtime'].isna().sum()
```

Good. Now, we can make a temporary copy of the `Runtime` column for our `.apply()` operations.

```python
temp_runtime = movies['Runtime'].copy()
temp_runtime.head(3)
```

Here's where we define our custom function. The best way to approach this is to test the function on a single value. By the way, even though we just dropped the rows with null values, we should still build in logic to avoid null values from causing issues.

```python
def runtime_reformat(row):
    """remove min from str and convert field to int"""
    try:
        split_row = row.split(' ')
        numeric_runtime = int(split_row[0])
        return numeric_runtime
    except Exception as e:
        # if pd.isnull(row), error will occur
        # print(e)
        return row

test = temp_runtime[0]
result = runtime_reformat(test)

# TESTING ONE VALUE...
print(f'''
BEFORE: {test}, {type(test)}
AFTER: {result}, {type(result)}
''')
```

Let it run on the whole Series:

```python
temp_runtime = temp_runtime.apply(runtime_reformat)
temp_runtime
```

Assign our freshly cleaned Series back to the `movies` dataframe.

```python
movies['Runtime'] = temp_runtime
movies['Runtime']
```

### Filter/Drop Shorts

In the last lesson, we dropped all TV shows from the dataframe because we only want to evaluate movies. In the same vein, it's not truly accurate to compare long-form movies to "short-form videos". That might include [animated shorts from Pixar](https://www.studiobinder.com/blog/pixar-shorts/), for example, or "made-for-TV" specials that last ~40-45 minutes (1 hour with commercials).

How many "shorts" are there?

```python
shorts = movies[movies['Runtime'] < 45].copy()
shorts.sort_values(by=['Runtime'], ascending=False, inplace=True)

print(len(shorts))
shorts
```

Drop these by grabbing their index labels and check to make sure they're gone.

```python
shorts_idx = list(shorts.index)
movies.drop(labels=shorts_idx, axis=0, inplace=True)
shorts = movies['Runtime'] < 45
shorts.sum()
```

### Reformat imdbVotes

`imdbVotes` needs to be a numeric variable as well, and we can likewise leverage the `.apply()` method on this Series.

```python
temp_imdbVotes = movies['imdbVotes'].copy()
temp_imdbVotes
```

All we need to do for the `imdbVotes` variable is remove the commas and typecast each value. 

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

test = temp_imdbVotes[0]
votes_reformat(test)
```

The single-value test worked, so we'll run it on the whole column...

```python
temp_imdbVotes = temp_imdbVotes.apply(votes_reformat)
temp_imdbVotes
```

...and then reassign `temp_imdbVotes` back to the `movies` dataframe.

```python
movies['imdbVotes'] = temp_imdbVotes
movies['imdbVotes'].head(3)
```

### Reformat Rotten Tomatoes

Finally, we need to reformat `Rotten Tomatoes` ratings by simply stripping off the `%` character and typecasting it to a float. Technically, we can do this with `.map()`. We could use `lambda x: float(x.strip('%'))`. But instead, let's practice `.apply()` one more time! 

```python
temp_rt = movies['Rotten Tomatoes'].copy()
temp_rt
```

Write and test the custom function.

```python
def strip_rt(row):
    try:
        stripped = float(row.strip('%'))
        return stripped
    except Exception as e:
        # print(e)
        return row
        
test = temp_rt[0]
print(test)
strip_rt(test)
```

Apply the function to the whole `Rotten Tomatoes` Series.

```python 
temp_rt = temp_rt.apply(strip_rt)
temp_rt
```

Reassign it back to the `movies` dataframe.

```python
movies['Rotten Tomatoes'] = temp_rt
movies['Rotten Tomatoes']
```

## Row- & Column-wise Functions with .apply()

You can also implement `.apply()` as dataframe method. In this context, `.apply()` is a **row-wise** or **column-wise** function. Here's the difference:

* **`s.apply(func)`** dynamically changes each value of that column a Series
* **`df.apply(func, axis=0)`** dynamically changes each value *of each row/column* of a dataframe


passes values from one column of every row to a function
when axis = 1, passes *entire rows* to a function
>>when axis = 0, passes whole cols where the row labels are treated like col labels...?


Of course, the `axis` parameter is what determines whether your function is row-wise or column-wise. However, it's a little counter-intuitive. We know that `axis 0` refers to rows and `axis 1` refers to columns, but in the context of `df.apply()`:

* If `axis=0`, the objects passed to `func` will be *a Series containing the dataframe's COLUMNS*. The changes will be made to each value (i.e. column) in the set of columns.
* If `axis=1`, the objects passed to `func` will be *a Series containing the dataframe's ROWS*. The changes will be made to each value (i.e. column) in the set of rows.

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

### Here's our newly bright and shiny dataframe!

```python
movies.head()
```

## New Functions Featured

Functions featured include (in order of appearance):
* `pd.to_numeric(s)`
* `s.astype()`
* `s.map(arg, na_action=None)`
* `s.apply(func)`
* `df.apply(func, axis=0)`
* `df.dropna(axis=0, how='any', subset=[col1], inplace=False)`

## 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

*TBD*
