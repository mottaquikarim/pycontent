# Data Cleaning

<img src="https://i.chzbgr.com/full/1898496256/h42C0CC42/panda-cleaning-instructions" style="margin: 0 auto; float: right;"/>

Data cleaning is arguably as important as any amount of insight you obtain from your dataset. The more data there is, especially data aggregated from multiple sources, the messier it is. You need to reformat and standardize it before you can successfully complete any real analysis. Otherwise...garbage in, garbage out...

## Objectives

* Handling null values
* Element-wise functions
* Vectorized typecasting
* Scaling variables
* Series.map()
* Series.apply()
* Row- & Column-wise functions 
* DataFrame.apply()

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

## A Note on Handling Null Values

Having null values in your data can cause various issues with your code and with your analysis. Deciding how to deal with null values is a huge part of cleaning your data, and you have to think about each column contextually. At a high level, you can drop rows/columns containing null values or replace all instances of null values with some default value (e.g. the mean, the value with the highest frequency, "Unknown", etc.). 

In addition to the "how", you also have to contextually consider the "when". For example, we had to get rid of all rows containing TV shows before we could sort by year because those rows contained non-numeric values such as "2009-2017". In this lesson, we'll be dropping rows with null values as we explore different concepts and consider different variables.

## Element-wise Functions

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
test_year = pd.to_numeric(test_year)
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

Finally, *notice that there is no `inplace` parameter for `.map()`*. You have to remember to assign the results to some variable, or you'll never see them!

### Reformat Rotten Tomatoes

If we look at the three movie rating variables, each source has provided ratings for each movie on a different scale and in a different format. 

* `imdbRating`: 0.0-10.0; float format
* `Metascore`: 0.0-100.0; float format
* `Rotten Tomatoes`: 0-100%; string format

Let's start by mapping `Rotten Tomatoes` ratings from strings to numeric values. 

```python
movies['Rotten Tomatoes']
```

All we have to do is strip off the "%" character and typecast the values to floats. Of course, we have to pass this to `.map()` in the form of a function. For brevity, whenever possible, most people use **lambda functions** with `.map()`. A **lambda function** is a nameless function that is defined, used, and forgotten in one line. Here's an example of the syntax relative to a regular function.

```python
"""
def squared(x):
    return x**2

...is equivalent to...

lambda x: x**2
"""
```

The body of the lambda function we need for reformatting `Rotten Tomatoes` ratings is `float(x.strip('%'))`. Also, don't forget to set `na_action='ignore'`, since there are null values in this column.

```python
movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].map(lambda x: float(x.strip('%')), na_action='ignore')
movies['Rotten Tomatoes']
```

### Scaling Variables

Look again at the formats for our ratings variables:

* `imdbRating`: 0.0-10.0; float format
* `Metascore`: 0.0-100.0; float format
* `Rotten Tomatoes`: 0.0-100.0; float format

For graphical comparisons, you always want numeric variables on the same *scale*. Since it's easier to see minute differences between data points on a larger scale, we'll scale `imdbRating` to match `Metascore` and `Rotten Tomatoes`.

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
movies['imdbRating']
```

## Element-wise Functions with .apply()

When applied to a Series object, the `.apply()` function is effectively the same as `.map()`. It's just another elementwise function. The difference is that you can pass it more complex functions (e.g. more than one line, conditionals, error handling, etc.), while `.map()` is mainly paired with simple lambda functions.

* `s.apply()`

As with `.map()`, if there are null values in the Series, an error will stop the code's execution. However, `.apply()` has no equivalent to the `na_action` parameter in `.map()`. If you don't want to drop all the rows with null values just to get your `.apply()` function working, you can **manually** skip over null values using the same logic behind the `na_action` parameter. For example, you can build in conditional logic or a try/except statement.

### Reformat imdbVotes

`imdbVotes` also needs to be a numeric variable, but it would take more than one line to accomplish this. Therefore, it wouldn't be as efficient to use `.map()`. Instead, we can define our own function and pass it to `.apply()`.

First, make a temporary copy of the `imdbVotes` column to use with our `.apply()` operations.

```python
temp_imdbVotes = movies['imdbVotes'].copy()
temp_imdbVotes.head(3)
```

When you define a custom function to use with `.apply()`, it's always a good idea to test the function on a single value.

```python
def votes_reformat(value):
    """remove commas from str and convert field to int"""
    try:
        split = value.split(',')
        votes = int(''.join(split))
        return votes
    except Exception as e:
        return value

test = temp_imdbVotes[0]
votes_reformat(test)
```

The single-value test worked, so we'll run it on the whole column...

```python
temp_imdbVotes = temp_imdbVotes.apply(votes_reformat)
temp_imdbVotes
```

Wait... they're floats, not ints... And if you try to typecast directly to integers using `.astype('int64)`, it will cause a `TypeError`. Why? This is because the null values. In Pandas, `NaN` is considered a float. Since Series object must have homogenous data types, any numeric Series containing null values will be forced to `dtype='float64'`.

When we decide how we want to handle the null values across our ratings fields, we can re-typecast this column. For now, we'll just reassign `temp_imdbVotes` back to the `movies` dataframe.

```python
movies['imdbVotes'] = temp_imdbVotes
movies['imdbVotes']
```

### Reformat Runtime

Next, we'll repeat this process with `Runtime`. This time though, we'll look at the column's null values first.

```python
missing_runtime = movies[pd.isnull(movies['Runtime'])]
print(len(missing_runtime))
missing_runtime
```

There are only three rows missing data for `Runtime`, all of which are also missing ratings from Rotten Tomatoes and Metascore. We might as well drop these rows, but we don't need to grab each one's index this time. (Flash back to when we removed TV shows using `movies.drop(labels=non_movie_ids, axis=0)`.) Since these three are the only rows with null values for `Runtime`, we can drop them as a group using `.dropna()`.

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

Now when we reformat `Runtime`, there won't be any null values forcing the rest of the Series values into `float` format.

Make a temporary copy of the `Runtime` column:

```python
temp_runtime = movies['Runtime'].copy()
temp_runtime
```

Define and test a custom function to remove `' min'` from each value and typecast it to an integer. By the way, even though we just dropped the rows with null values, we should still build in a try/except statement to catch other potential issues!

```python
def runtime_reformat(value):
    """remove 'min' from str and convert field to int"""
    try:
        value = value.split(' ')
        numeric_runtime = int(value[0])
        return numeric_runtime
    except Exception as e:
        print(e)
        return value

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

Assign it back to the `movies` dataframe:

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

*Notice that the rows with null values are NOT included here!*

Drop these by grabbing their index labels and check to make sure they're gone.

```python
shorts_idx = list(shorts.index)
movies.drop(labels=shorts_idx, axis=0, inplace=True)
shorts = movies['Runtime'] < 45
shorts.sum()
```

## BONUS: Row- & Column-wise Functions with .apply()

You can also implement `.apply()` as dataframe method. In this context, `.apply()` is a **row-wise** or **column-wise** function. Here's the difference:

* **`s.apply(func)`** dynamically changes each value of a Series; in the context of a dataframe, it's like passing all the rows but only a single column to the function
* **`df.apply(func, axis=0)`** dynamically changes each value *of each row/column* of a dataframe; when axis = 1, passes *entire rows* to the function

Of course, the `axis` parameter is what determines whether your function is row-wise or column-wise. However, it's a little counter-intuitive. We know that `axis 0` refers to rows and `axis 1` refers to columns, but in the context of `df.apply()`:

* If `axis=0`, the objects passed to `func` will be *a Series containing the dataframe's COLUMNS*. The changes will be made to each value (i.e. column) in the set of columns.
* If `axis=1`, the objects passed to `func` will be *a Series containing the dataframe's ROWS*. The changes will be made to each value (i.e. column) in the set of rows.

### Languages

```python
null_lang = movies[pd.isnull(movies['Languages'])].copy()
print(movies['Languages'].isnull().sum())
null_lang
```

There are 4 movies with `NaN` in their `Languages` field. But do you notice anything? The first movie with sound was The Jazz Singer, released in 1927. All four of these movies were released before that year. 

* `.fillna(value=None, inplace=False)`

```python
movies['Languages'].fillna(value='Silent', inplace=True)
movies.loc[null_lang.index]
```

What if other early movies were incorrectly labeled? If we want to be consistent, we need to check all the movies made before 1927 and set those to "Silent" as well.

```python
silent_films = movies[movies['Year'] < 1927]
silent_films
```

As expected, there are a few. Let's write a function to change that. We'll want to test two values here: one movie made before 1927 and one after.

```python
def silent_lang(row):
    try:
        if row['Year'] < 1927:
            row['Languages'] = 'Silent'
            return row
        else:
            return row
    except Exception as e:
        print(e)
        return row

temp = movies.copy()

pos_test = silent_lang(temp.loc['tt0013442'].copy()) # Nosferatu
pos_test
```

```python
neg_test = silent_lang(temp.iloc[0].copy())
neg_test
```

The tests worked, so it's safe to apply it to the dataframe as a whole. Check to see if those silent films changed.

```python 
temp = temp.apply(silent_lang, axis=1)
temp.loc[silent_films.index]
```

Remember to reassign this new dataframe back to the `movies` variable before moving on! Now look at all the movies made before 1927.

```python
movies = temp.copy()
movies[movies['Year'] < 1927]
```

## Compound Filtering & Handling Null Movie Ratings 

We can probably uncover some interesting insights by comparing different characteristics of movies to different ratings sources. For movies missing one or more ratings, we can always replace those null values with the mean of the column. However, a strict statistician would tell you that this distorts the accuracy of your results. And when there's money riding on the outcomes of your analyses, you probably want to aim as close to the bull's eye as possible.

Ultimately, we want to know what proportion of movies is missing at least one rating. If it's too large, we might consider dropping one of the rating sources. The count of non-null values per column that we see with `.info()` will NOT answer this question for us. 

```python
movies.info()
```

We don't know whether each movie is missing one, both, or neither of the ratings from Rotten Tomatoes and Metacritic. We have to use compound filtering to determine the proportion of movies with complete ratings data vs. the proportion missing at least one rating. First, we need the total number of movies:

```python
whole_rows = len(movies)
```

Now we need to write a compound filter to return all the movies that:

* have a rating from IMDb *AND*
* have a rating from Rotten Tomatoes *AND*
* have a rating from Metacritic

**NOTE!** When implementing compound filters, you have to use `&` and `|` instead of `and` and `or` respectively.

```python
full_ratings = movies[pd.notnull(movies['imdbRating']) & pd.notnull(movies['Rotten Tomatoes']) & pd.notnull(movies['Metascore'])]

p1 = len(full_ratings)
print(f'{p1} movies, or', '{:.2%},'.format(p1/whole_rows), 'have ratings from all 3 sources.')
```

Next, we need to write a compound filter to return all the movies that:

* are missing a rating from IMDb *OR*
* are missing a rating from Rotten Tomatoes *OR*
* hare missing a rating from Metacritic

```python
missing_rating = movies[pd.isnull(movies['Rotten Tomatoes']) | pd.isnull(movies['Metascore']) | pd.isnull(movies['imdbRating'])]

p2 = len(missing_rating)
print(f'{p2} movies, or', '{:.2%},'.format(p2/whole_rows), 'are missing a rating from at least one source.')
```

A good gut check to make sure your results line up with what you expect is to run this conditional:

```python
p1 + p2 == whole_rows
```

A significant chunk of these movies are missing at least one rating, but even if we remove those, we still have a relatively large sample size. As such, we'll drop all the rows missing a rating. 

Notice how we pass `how='any'` *as well as* a subset of columns. This very specifically drops all the rows where *any column in the subset* contains a null value.

```python
movies.dropna(axis=0, how='any', subset=['imdbRating', 'Rotten Tomatoes', 'Metascore'], inplace=True)
```


## Missing Qualitative Data 

With qualitative or categorical data, you can either drop null values or fill them with some version of an "Unknown" category. How you determine that value is really subjective.

Let's see how many movies are missing data about their **actors**.

```python
missing_actors = movies[pd.isnull(movies['Actors'])]
print(f'{len(missing_actors)} movies are missing actor info.\n')
missing_actors
```

ALL of these are documentaries. Documentaries shouldn't theoretically have actors, so we can use `.fillna()` to update all of these with "None (Documentary)".

```python
movies['Actors'].fillna('None (Documentary)', inplace=True)
movies['Actors'].isna().sum()
```

**How about writers?**

```python
missing_writer = movies[pd.isnull(movies.Writer)]
print(f'{len(missing_writer)} movies are missing writer info.\n')
missing_writer
```

It looks like a lot of there are documentaries too. We can isolate the ones which aren't documentaries by negating `movies['Genre'].str.contains('Documentary')`. To negate a whole condition, simply preface it with a tilde `~`.

```python
missing_doc_writer = movies[(pd.isnull(movies.Writer)) & ~movies['Genre'].str.contains('Documentary')]
missing_doc_writer
```

Only one of them isn't a documentary. I looked up the outlier, so we could add it here. The rest, we can fill with "Unknown".

```python
movies.loc['tt4063178', 'Writer'] = 'Alex Ranarivelo, Ali Afshar'
movies['Writer'].fillna('Unknown', inplace=True)
movies['Writer'].isna().sum()
```

## New Functions Featured

Functions featured include (in order of appearance):
* `pd.to_numeric(s)`
* `s.astype()`
* `s.map(arg, na_action=None)`
* `s.apply(func)`
* `df.dropna(axis=0, how='any', subset=[col1], inplace=False)`
* `.fillna(value=None, inplace=False)`
* `df.apply(func, axis=1)`
* `s.fillna(value=None, inplace=False)`

## 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Practice using these methods in your copy of wrangling_pset2.ipynb in Google Drive.
