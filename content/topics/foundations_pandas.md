# Foundations of Pandas

<img src="https://media.giphy.com/media/EatwJZRUIv41G/giphy.gif" style="margin: 0 auto; float: right;"/>

**Pandas** is an open-source Python library of data structures and tools for exploratory data analysis (EDA). Pandas primarily facilitates acquisition, cleaning, formatting, and manipulating. Used in tandem with NumPy, Matplotlib, SciPy, and other Python libraries, Pandas is an integral part of practicing data science. Its core capabilities include: 

* Robust IO tools to read from flat files (CSV and TXT), JSON, XML, Excel files, SQL tables, and other databases.
* Axis reindexing and hierarchical labeling of matrix-like `dataframes`
* Data manipulation, by applying `vectorized operations` or by iterating through datasets
* Handling duplicates and missing data
* Conditional queries for sorting, filtering, & subsetting
* Merging & joining datasets
* Reshaping, transforming, & pivoting datasets
* Basics statistics
* Time-series functionality, e.g. date shifting, frequency conversions, & moving window statistics

To gain some baseline familiarity with Pandas features and pre-requisites, in this lesson, you'll learn about:

* [NumPy ndarray Objects](intro_pandas.md#numpy-ndarrays-objects)
* [Basic Pandas Objects](intro_pandas.md#basic-pandas-objects)
	* [Index](intro_pandas.md#basic-pandas-objects-index)
	* [Series](intro_pandas.md#basic-pandas-objects-series)
	* [DataFrames](intro_pandas.md#basic-pandas-objects-dataframes)

## Importing Data Science Libraries

The first thing you have to do start a new analysis is import whichever data science libraries you plan to use. Pandas is built on top of NumPy, so you have to import that separately every time you plan to use pandas. Notice the standard abbreviations used for later references of the libraries.

```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

*As a bonus, I've added the notation for importing the other two libraries to be used in this class - matplotlib and seaborn. More to come on these later!*

## NumPy ndarray Objects

Pandas is built on top of NumPy, so before  new users should first understand one NumPy data object that often appears within Pandas objects - the **ndarray, or N-dimensional array**.

`Ndarrays` are deceptively similar to the more general Python `list` type we've been working with. An `ndarray` type is a group of elements, which can be accessed and updated using a zero-based index. Sounds exactly like a `list`, right? 

```python
import numpy as np

listA = [1, 2, 3]
listB = ['a', 'b', 'c']

arrayA = np.array([1, 2, 3])
print(listA) # [1, 2, 3]
print(arrayA) # [1 2 3]

listB = ['a', 'b', 'c']
arrayB = np.array(listB)
print(listB) # ['a', 'b', 'c']
print(arrayB) # ['a' 'b' 'c']
```

Wrong. You don't need to get caught up on the syntactical details of ndarrays for this course. However, you should understand the three key differences between ndarrays and lists: 

### 1) All ndarrays must be homogenous.

All elements in an ndarray must be the same data type (e.g. integers, floats, strings, booleans, etc.). If you try to enter data that is not homogenous, the `.array()` function will force unity of data type.

```python
import numpy as np

bad_array1 = np.array([1, 'b', True])
print(bad_array1) # ['1', 'b', 'True']

bad_array2 = np.array([1, False])
print(bad_array2) # [1 0]
```

### 2) An ndarray can have multiple dimensions.

<img src="../images/ndarray_axes.png" style="margin: 0 auto; display: block;"/>

ndarrays have a parameter called `ndmin`, which allows you to specify the number of dimensions you want for your array when you create it. Each dimension prints on its own line, so the ndarray looks more like a *grid* than a single list. Having n-dimensions also means that when you reference ndarray values by index, you need to use multiple index positions.

**2-D array: 3x3**

```python
dim1 = np.array([1, 2, 3]) 
dim2 = np.array([4, 5, 6])
dim3 = np.array([7, 8, 9])

arrayC = np.array((dim1, dim2, dim3))
print(arrayC) 
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
```

**3-D array: 2x3x3**

```python
arrayD = np.array((([1, 2, 3], [4, 5, 6], [7, 8, 9]), ([1, 2, 3], [4, 5, 6], [7, 8, 9])), ndmin = 3)
print(arrayD)
"""
[[[1 2 3]
  [4 5 6]
  [7 8 9]]

 [[1 2 3]
  [4 5 6]
  [7 8 9]]]
"""
```

### 3) ndarrays are designed to handle `vectorized` operations

In other words, if you apply a function to an ndarray object, the program will perform said function on *each* item in the array individually. Depending on the operand, if you apply a function to a list, either the function will be performed on the list object *as a whole* or you will get a TypeError. As a bonus, these vectorization capabilities also allow ndarrays take up less memory space and run faster.

```python
list1 = [3, 5, 7]
array1 = np.array([3, 5, 7])

print(list1 * 10) # [3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3,5, 7, 3, 5, 7, 3, 5, 7]
print(array1 * 10) # [30 50 70]

# print(list1 + 1) # TypeError
print(array1 + 1) # [4 6 8]
```
## Pandas Series Objects

A **Series** object from the Pandas library is like a simpler version of an ndarray.

* All the values in a Series must homogenous.
* A Series is always 1-D.
* Series support vectorized operations
* By default, the `index` parameter assigns an zero-based index. Alternatively, you can assign custom index labels to a Series. On this front, you can think of a Series kind of like a dict.

The general syntax for creating a Series is `s = pd.Series(data, index, dtype)`. Using this syntax, you can instantiate a Series from a single scalar or boolean value, a list, an ndarray, or a dict.

**Series from a single scalar/boolean value, using a custom index**

```python

s_scalar = pd.Series(1, index=['a', 'b', 'c', 'd', 'e'])
ubstitute 
s_boolean = pd.Series(False, index=['a', 'b', 'c', 'd', 'e'])

print(s_scalar)
print(s_boolean)
```

**Series from a list, using default indexing**

```python
s_list = pd.Series(['red','orange','yellow','green','blue','purple'])
print(s_list)
```

**Series from an ndarray, using default indexing**

```python
s_ndarray = pd.Series(np.ndarray(['red', 'orange' 'yellow','green','blue','purple']))
print(s_ndarray)
```

**Series from a dict, using implicit custom index**

```python
my_dict = {'c': 15, 'B': 20, 'a': 10}
s_dict = pd.Series(my_dict)
print(s_dict)
```

## Pandas DataFrame Objects

<img src="../images/ndarray_axes.png" style="margin: 0 auto; display: block;"/>

A **DataFrame** is a 2-D data matrix that stores data much like a spreadsheet does. 


It has labeled columns and rows with values for each column. It accepts many different data types as values, including strings, arrays (lists), dicts, Series, and even other DataFrames. The general syntax for creating a DataFrame is identical to that of a Series except it includes a second index parameter called `columns` parameter for adding the index values to the second dimension:



```python
import numpy as np
import pandas as pd

df = pd.DataFrame(data, index, columns)
```

Creating a DataFrame is a little more complex than creating a Series because you have to consider both `rows` and `columns`. Aside from creating a dataframe indirectly by importing an existing data structure, you can create a DataFrame by:

* Specifying column names (i.e. column index values) directly within the `data` parameter
* Specifying column names separately in the `columns` parameter

```python
import numpy as np
import pandas as pd

# Specify values for each column.
df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])

# Specify values for each row.
df = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]],
index=[1, 2, 3],
columns=['a', 'b', 'c'])


# Both of these methods create a DataFrame with these values:
"""
   a   b   c
1  4   7   10
2  5   8   11
3  6   9   12
"""
```

Here are a few other examples:

```python
import numpy as np
import pandas as pd

# From dict of Series or dicts
data1 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df1 = pd.DataFrame(data1, index=['d', 'b', 'a'], columns=['two', 'three'])
"""
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN
"""

# From dict of ndarrays / lists
data2 = {'one': [1., 2., 3., 4.],'two': [4., 3., 2., 1.]}
df2 = pd.DataFrame(data2, index=['a', 'b', 'c', 'd'])
"""
   one  two
a  1.0  4.0
b  2.0  3.0
c  3.0  2.0
d  4.0  1.0
"""

# From a list of dicts
data3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df3 = pd.DataFrame(data3, index=['first', 'second'], columns=['a', 'b', 'c'])
"""
        a   b     c
first   1   2   NaN
second  5  10  20.0
"""
```




## Pandas Index Objects

As opposed to the index of a regular Python `list`, Pandas considers `Index` to be its own object class.

We just briefly looked at how to set custom index labels for `Series` objects and `DataFrame` objects. Let's break it down further. 

<img src="../images/ndarray_axes.png" style="margin: 0 auto; display: block;"/>

We just saw how a Series index 
know about the concept of an `index` from basic Python `lists`. In a list object, the index allows you to select a list item by referencing its *numerical position* (like counting).






**BEFORE**

*List object*

|  my_list | Brandi | Zoe | Steve | Aleksander | Dasha |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |


|  my_series | Brandi | Zoe | Steve | Aleksander | Dasha |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |

Because a list's index refers to the item's *position*, if you add, remove, or reorder items, the index is unaffected. In other words, let's say I alphabetize these names. `my_list[1]`, for example, no longer refers to "Zoe". Instead, it refers to "Brandi".

|  my_list | Aleksander | Brandi | Steve | Aleksander | Zoe |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |

Well, Pandas considers `Index` to be its own object class, and it works a little differently. 

As formally defined in the Pandas docs, an `Index` object is an "immutable ndarray implementing an ordered, sliceable set". Whereas a regular list's index is , The main purpose of an `Index` object is to store the labels for each axis in an array. 





It *does NOT have to be unique*, though you should always use unique values when creating a custom index. try to always  Itwhich is the default object for "storing axis labels for all pandas objects".



## Reading/Writing Files

For our lesson on Pandas we'll be using this dataset:

[?????? | Kaggle](https://www.kaggle.com/zynicide/wine-reviews/) -- 
*130k wine reviews with variety, location, winery, price, & description*


We've just finished preparing our first dataset for analysis. This one was in .CSV format, but we also learned above that Pandas can handle many different file types. To open each of these in pandas we use a slightly customized version of the general method `pd.read_<filetype>(<file_name>)`. Look [here](../Resources/pandas_glossary.html#reading--writing-data) for a quick summary of commands for handling different file types in Pandas.