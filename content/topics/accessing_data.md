# Accessing Data

## **Core Objectives**

We have just one more section before we can get into the kind of contextual analysis you'll use for data science. After all, you can't analyze your data unless you can select exactly which parts you want at any given time. This lesson focuses on how to:

* Load and save data to and from your notebook
* Access a summary or a preview of the dataset
* Reference data using index positions vs. index labels
* Select single values and subsets of a Series
* Select a single column, row, or cell in a dataframe
* Select a slice of rows or columns in a dataframe
* Select a chunk of a dataframe

Over the next several lessons, we're going to use a dataset containing movie metadata that we pulled from the [OMDb API](http://www.omdbapi.com/). In this section, we'll use a subset of that data for simplicity's sake. This subset will include three fields: imdbID, Title, and Year.

## Reading & Writing Data

Before we can even load this data, we have to import the necessary libraries.

```python
import numpy as np
import pandas as pd
```
Reading and writing data to and from your notebook primarily relies on the format and location of your data. The general syntax is:

* **Read:** `pd.read_<format>(<path>)`
* **Write:** `pd.to_<format>(<path>)`

*Notice how saving your data uses pd.to_<format> and NOT pd.write_.* For the syntax of how to load the most common data types, you can reference the "Reading & Writing Data" section of our [Pandas Cheat Sheet](https://mottaquikarim.github.io/PYTH122/#out/resources/pandas_cheat_sheet).

There are a number of **optional parameters** you might want or need to use. A quick exaplanation of the most useful ones are:

* `sep`: By default, ','
You can specify the character that delimits the values so that Pandas can recognize it.
* `header`: By default, Pandas infers the headers.
If you know there is no header row, you should pass `False` and pass a list of column names to the `names` parameter.
* `names`: (see "header" above)
* `index_col`: By default, `None` and Pandas will use a 0-based numerical index for the `Index` labels. If you want to use one (or more) of the columns as the index for axis 0 (the rows), specify them here.
* `usecols`: If you want only a subset of columns loaded, indicate which ones here.
* `nrows`: By default, Pandas loads the full file. If you want only a subset of the data, you can specify a number of rows to load.

#### Loading the OMDb Dataset

Since this is our first time looking at it, let's load the OMDb dataset as is. 

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb_subset.csv')
movies = omdb_orig.copy()
```
It's also a helpful practice to immediately make a hard copy of the dataset so that, at any time, you can compare your data to the original dataset. You can make a shallow copy (see below), but it's always better to make a hard copy with the `.copy()` method.

>> Warning! [SettingWithCopyWarning](https://www.dataquest.io/blog/settingwithcopywarning/)

## Summary Data & Metadata

Typically, the first thing you'll want to do is use the `.info()` method to see a summary of the data in your dataframe. This will tell you things like how many rows there are, what datatype each column Series contains, and how many non-null values are in each column. Note that Series objects do NOT have this attribute.

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
By now, you'll probably want to preview the data itself. `.head(n)` and `.tail(n)` will return the first and last *n* rows of data respectively. If you don't pass in a number, they will both return 5 rows by default. You can use `.head()` and `.tail()` on Series objects as well.

```python
movies.head() 
```

```python
movies.tail(3) 
```

In this column, we can see that we have an existing unique ID for each movie - the IMDb ID. Especially because IMDb is the most well-known movie database, we should make `imdbID` the index. That way we can access each movie via its imdbID label.

```python
movies.set_index(['imdbID'], drop=True, inplace=True)
movies.head(3)
```
By default, the `drop` parameter in the `.set_index()` function is `True`. As you can see above, `imdbID` no longer exists as a column in the dataframe. It has been converted into an `Index` object.

```python
imdbID = movies.index
type(imdbID)
```

If you ever want to go back to the default numerical `Index` labels, you can use `.reset_index()`. It will simply add the custom `Index` object back to the dataframe as a column Series.

```python
movies.reset_index(inplace=True)
movies.tail()
```

Now, let's set the index back to `imdbID`.

```python
movies.set_index(['imdbID'], inplace=True)
```

## Selecting Data

Dataframe columns are the easiest and most flexible pieces of data to select and maneuver.

Return a single column as a Series:

```python
print(type(movies['Title']), '\n')
titles = movies['Title']
titles
```

Return a subset of columns (in any order) as a new DataFrame:

```python
movies[['Title', 'Genre', 'Director', 'Actors']]
```

For most other pieces of data that you want to select, you will use some variation of `.loc[]` or `.iloc[]`. It's vital to understand the difference between these two functions: 

* **`.loc[]`** selects and returns data by passing index **LABELS** as arguments
* **`.iloc[]`** selects and returns data by passing index **POSITIONS** as arguments

### **Single Value in a Series**

Select a single value in a Series by its index label

```python
titles.loc['tt1302006']
```

Select a single value in a Series by its index position

```python
titles.iloc[516]
```

### **Single Row**

Select a single row by its label

```python
movies.loc['tt0088763']
```

Select a single row by its index position

```python
movies.iloc[112]
```

### **Single DataFrame Cell**

**Select a single cell in a DataFrame by row & column labels**

```python
movies.loc['tt0088763', 'Year']
```

Select a single cell in a DataFrame by row & column index positions

```python
movies.iloc[112, 8]
```

### **Subset of a Series**

Returns a subset of a Series by entering a range of labels

```python
titles.loc['tt1302006':'tt1025100']
```

Returns a subset of a Series by entering a range of index positions

```python
titles.iloc[4870:4875]
```

### **Slice of Rows**

Returns a *slice* of rows as a new DataFrame by entering a range of labels

```python
movies.loc['tt1302006':'tt1025100']
```

Returns a *slice* of rows as a new DataFrame by entering a range of index positions

```python
movies.iloc[4870:4875]
```

### **Chunk of a Dataframe**

Select a chunk of a DataFrame by entering a range of row and column labels

```python
movies.loc['tt4972582':'tt1396484','Title':'Runtime']
```

Select a slice of a DataFrame by entering a range of row and column index positions

```python
movies.iloc[4870:4875,0:5]
```

## Key Takeaways

* A data dictionary documents metadata for a dataset by defining each column
* The general syntax for reading (i.e. loading) data is `pd.read_<format>(<path>)`
* The general syntax for writing (i.e. saving) data is `pd.to_<format>(<path>)`
* Use the `.info()` method to see a summary of the data in your dataframe. Series objects do NOT have this attribute.
* `.head(n)` and `.tail(m)` return the first and last *n* elements of an object respectively. (i.e. values for a Series and rows for a Dataframe)
* `.set_index(data, drop=True)` allows you to assign custom index labels to a Series or dataframe
* `.loc[]` selects and returns data by passing index **LABELS** as arguments
* `.iloc[]` selects and returns data by passing index **POSITIONS** as arguments
