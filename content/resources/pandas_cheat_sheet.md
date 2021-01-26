# Pandas Cheat Sheet

<img src="https://news.nationalgeographic.com/content/dam/news/2015/12/15/pandas/01pandainsemination.ngsversion.1450209600474.adapt.1900.1.jpg" style="margin: 0 auto; width: 50%; float: right;"/>

## Reading & Writing Data

[pd.read_csv() parameter documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

* **`pd.read_csv(<file_path>)`** -- From a CSV file
* **`pd.read_table(<file_path>)`** -- From a delimited text file (like TSV)
* **`pd.read_excel(<file_path>)`** -- From an Excel file
* **`pd.read_sql(query, connection_object)`** -- Reads from a SQL table/database
* **`pd.read_json(json_string)`** -- Reads from a JSON formatted string, URL or file.
* **`pd.read_html(url)`** -- Parses an html URL, string or file and extracts tables to a list of dataframes
* **`obj.to_csv(<file_path>)`** -- Writes to a CSV file
* **`obj.to_excel(<file_path>)`** -- Writes to an Excel file
* **`obj.to_sql(table_name, connection_object)`** -- Writes to a SQL table
* **`obj.to_json(<file_path>)`** -- Writes to a file in JSON format
* **`obj.to_html(<file_path>)`** -- Saves as an HTML table

## Selecting Data

* **`df[col]`** -- returns one column as a Series
* **`df[[col_label, col2]]`** -- returns multiple columns (in any order) as a new DataFrame
* Select a single item (i.e. a value from a Series or a row from a Dataframe)...
    * **`obj.loc[idx_label]`** -- by its index label
    * **`obj.iloc[idx]`** -- by its index position
* Select a single value in a DataFrame...
    * **`df.loc[row_label, col_label]`** -- by row & column index label
    * **`df.iloc[row_idx, col_idx]`** -- by row & column index label position
* Returns a slice of rows as a new DataFrame by entering a range of...
    * **`df.loc[row_start : row_end]`** -- index labels
    * **`df.iloc[row_start : row_end]`** -- index positions
* Select a slice of a DataFrame by entering a range of row and column...
    * **`df.loc[row_start : row_end , col_start : col_end]`** -- index labels
    * **`df.iloc[row_start : row_end , col_start : col_end]`** -- index positions

## Object Structuring & Indexing

* **`pd.Series(data=None, index=None, dtype=None, name=None, copy=False)`** -- create a Series object from list of data and index list or from dict
    * `name` can serve to match with df col name
* **`pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)`** -- create a DataFrame object
* **`obj.set_index(keys, drop=False, append=False, inplace=False)`**
* **`obj.reset_index(drop=False, inplace=False)`** -- reset index to default integer index; adds current index as a col to the df when drop=False
* **`obj.rename_axis(mapper=None, index=None, columns=None, axis=None, inplace=False)`** -- rename either the index or column(s), where mapper represents the new name
* **`obj.rename(columns/index={'old_name': 'new_ name'}, inplace=False)`** -- rename specific columns (or index) with dict of old to new names
* **`df.insert(loc, column, value)`** -- insert a col into a df at a specified index location
* **`df.drop(axis, labels, index, columns=[col1, col2, ...])`** -- drops specified columns from the dataframe
* **`df.update(other, join='left', overwrite=True, errors='ignore')`** -- update a df with values passed to `other`
    * if a Series is passed in, its `name` attribute must match a column in the df
    * always a `left` join to keep the index and columns of the original object
    * `overwrite` signals whether or not to overwrite existing values for overlapping keys
    * When `'raise'` is passed to `errors`, the function will raise a `ValueError` if both objects contain non-NA data in the same place
* **`s.replace([1,3],['one','three'])`** -- replace all values equal to 1 with 'one' and all values equal to 3 with 'three'
* **`df.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False)`** -- replace values (passed per `to_replace` param) in a DataFrame per those passed via `value` param.

## Data Wrangling

### Summary Metadata

* **`.info()`**
* **`.index`** -- return Index of the Series or df
* **`df.head(n=5)`** -- return first n rows
* **`df.tail(n=5)`** -- return last n rows
* **`df.dtypes`**
* **`s.nlargest(n)`** -- select and order largest n entries
* **`s.nsmallest(n)`** -- select and order smallest n entries
* **`df.nlargest(n, columns)`** -- select and order largest n entries based on one or more cols
* **`df.nsmallest(n, columns)`** -- select and order smallest n entries based on one or more cols
* **`df.shape`** -- returns tuple w. (# of rows, # of cols)
* **`df.columns`** -- returns Index object containing the df's column labels
* **`obj.index`** -- returns Index object containing the obj's row values
* **`s.isunique`** -- returns boolean for whether Series values are unique
* **`.count()`**
* **`.sum()`**
* **`.unique()`** -- returns all unique values
* **`.nunique()`** -- returns a count of the unique values

### Typecasting

* **`s.astype()`** -- typecast the items in a Series to some data type; accepts `'int64'`, `'float64'`, `'str'`, etc.
* **`pd.to_numeric(s, errors='coerce')`** -- convert the items within a Series to numbers
* **`s.tolist()`** -- convert Pandas Series to Python List type
* **`s.to_dict()`** -- convert Pandas Series to Python Dict type
* **`s.to_frame()`** -- convert Pandas Series to Pandas Dataframe
* **`s.to_string()`** -- convert the ENTIRE series into a single string

### Sorting

* **`s.sort_values(ascending=False, inplace=False, na_position='last')`** -- sort values of a Series in ascending order
* **`df.sort_values(by=[col1, col2], ascending=False, inplace=False, na_position='last')`** -- sort df rows by col1, then by col2; descending order by default
* **`df.sort_index(axis=0, ascending=True, inplace=False)`** -- sort axis values by index in *ascending* order

### Duplicates

* **`s.duplicated(keep='first')`** -- return boolean Series denoting duplicate rows; by default keeps the first instance of a dup
* **`s.drop_duplicates(keep='first', inplace=False)`** -- return Series with dups removed; by default keeps the first instance of a dup
* **`df.duplicated(subset=None, keep='first')`** -- return boolean Series denoting duplicate rows; by default determines whether full row is a dup; by default keeps the first instance of a dup
* **`df.drop_duplicates(subset=None, keep='first', inplace=False)`** -- return df with dups removed; by default determines whether full row is a dup

### Null Values

* **`.isna()`** -- return Series or df of booleans, where True indicates a null value; empty strings are NOT considered null values
    * chain with `.sum()` to get a count of nulls
* **`.notna()`** -- boolean inverse of `.isna()`
* **`pd.isnull(obj)`** -- same functionality as `.isna()`
* **`pd.notnull(obj)`** -- same functionality as `.notna()`
* **`s.dropna(inplace=False)`** -- Drops all null values and returns new Series
* **`s.fillna(value=None, inplace=False)`** -- replace all missing values with some value (e.g. the mean, some placeholder value, etc.)
* **`df.dropna(axis=0, how='any', subset=[col1], inplace=False)`** -- Drops rows/columns containing null values in one or more specific fields and returns new df
    * when `how='all'`, drop that row or column only if all values (in row as a whole or in all columns specified in `subset`) are null
    * `subset` indicates which columns to check for null values (*when dropping rows, i.e. axis=0*)
* **`df.fillna(value=None, axis=0, inplace=False)`** -- replaces all null values with some value (e.g. the mean, some placeholder value, etc.)

## Vectorized Functions

* **`s.map(arg, na_action=None)`** -- Map/substitute each value in a Series with another value
    * `arg` parameter accepts single-argument functions, dicts, or Series
    * If `na_action` is `'ignore'`, propagate NaN values, without passing them to the mapping correspondence
* **`s.apply(func, convert_dtype=True, args=(), **kwds)`** -- same as map, but invokes a more complex custom elementwise function on each value of Series
    * `convert_dtype` will try to find better dtype for elementwise function results; if `False` the Series remains `object` dtype
    * `args` : tuple of *positional* args to pass to `func` *in addition to the array/series*
    * `**kwds` : any keyword args to pass to `func`
* **`df.apply(func, axis=0, args=(), **kwds)`** -- apply row-wise or column-wise function to df, i.e. objects passed to `func` are Series objects whose index is either the df's index or the df's column labels
    * `args` : tuple of *positional* args to pass to `func` *in addition to the array/series*
    * `**kwds` : any keyword args to pass to `func`

## Transforming Data

* **`df.groupby(by=None, sort=True)`** -- return a `Groupby object`
* **`gb.groups`** -- from a GroupBy object, returns the group names and a collection of each group's elements 
* **`gb.get_group(<group_name>)`** -- returns the elements of a specific group in a GroupBy object as a new dataframe object
* **`df.explode(column, ignore_index=False)`**: split list-like rows into individual values, replicating indices

## Statistics

* **`.describe(include=np.object)`** -- return count, mean, standard deviation, min, max, & interquartile range (IQR); *only includes numerical columns by default*
* **`df.sample(frac = 0.5)`** - randomly select a fraction of rows of a DataFrame
* **`df.sample(n=10)`** - randomly select n rows of a DataFrame
* **`s.value_counts(normalize=False, sort=True, ascending=False, dropna=True)`** -- return a Series containing counts -- or, if `normalize=True`, relative frequencies -- of unique values
* **`s.mean()`** -- mean
* **`s.median()`** -- median
* **`s.min()`** -- minimum
* **`s.max()`** -- maximum
* **`s.quantile(q=0.5)`** -- return value at the given quantile q, where 0 <= q <= 1.
    * Can pass multiple values for q to return a Series of quantiles
* **`s.var()`** -- variance
* **`s.std()`** -- standard deviation
* **`s.mad()`** -- mean absolute variation
* **`s.skew()`** -- skewness of distribution
* **`s.sem()`** -- unbiased standard error of the mean
* **`s.kurt()`** -- kurtosis
* **`s.cov()`** -- covariance
* **`s.corr()`** -- Pearson Correlation coefficent
* **`s.autocorr()`** -- autocorelation
* **`s.cumsum()`** -- cummulative sum
* **`s.comprod()`** -- cumulative product
* **`s.cummin()`** -- cumulative minimum

## Data Viz

**Histogram**

* Purpose: Illustrate the frequency distribution of a numerical variable
* Pandas: `<series>.plot(kind='hist', bins=None)`
* Seaborn: `sns.distplot(a, bins=None, hist=True, kde=True, color=None, ax=None)`

**Box-and-Whiskers Plot**

* Purpose: Highlight the variability in a distribution
* Pandas: `<series>.plot(kind='box')`
* Seaborn: `sns.boxplot(x, y, hue=None, data=None, orient=None, color=None, ax=None)`

**Bar Chart**

* Purpose: Show a numerical comparison across different categories
* Pandas: `<series>.plot(kind='bar')`
* Seaborn: `sns.barplot(x, y, hue=None, data=None, estimator=np.mean, ci=95, orient=None, color=None, palette=None, ax=None)`

**Line Graph**

* Purpose: Show the trend of a numerical variable over time
* Pandas: `<series>.plot()`
* Seaborn: `sns.lineplot(x, y, hue=None, data=None, palette=None, markers=None, estimator=np.mean, ci=95, ax=None)`

**Scatterplot**

* Purpose: Compare the relationship between two numerical variables
* Pandas: `<series>.plot.scatter(x, y)`
* Seaborn: `sns.scatterplot(x, y, hue=None, data=None, estimator=None, ci=95, ax=None)`

