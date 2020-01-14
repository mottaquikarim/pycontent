# Pandas Cheat Sheet - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

<img src="https://news.nationalgeographic.com/content/dam/news/2015/12/15/pandas/01pandainsemination.ngsversion.1450209600474.adapt.1900.1.jpg" style="margin: 0 auto; width: 50%; display: block;"/>

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

## Data Wrangling

### Summary Metadata

* `obj.info()`
* `df.head(n=5)` -- return first n rows
* `df.tail(n=5)` -- return last n rows
* `s.nlargest(n)` -- select and order largest n entries
* `s.nsmallest(n)` -- select and order smallest n entries
* `df.nlargest(n, columns)` -- select and order largest n entries based on one or more cols
* `df.nsmallest(n, columns)` -- select and order smallest n entries based on one or more cols
* `df.shape` -- returns tuple w. (# of rows, # of cols)
* `df.columns` -- returns Index object containing the df's column labels
* `obj.index` -- returns Index object containing the obj's row values
* `s.isunique` -- returns boolean for whether Series values are unique
* `obj.describe()`

### Typecasting

* `s.astype()` -- convert items in series to a diff dtype
* `s.tolist()` -- convert Pandas Series to Python List type
* `s.to_dict()` -- convert Pandas Series to Python Dict type
* `s.to_frame()` -- convert Pandas Series to Pandas Dataframe
* `pd.to_numeric(s, errors='coerce')` -- convert the items within a Series to numbers
* `s.to_string()` -- convert the items within a Series to strings

**!!!to_dict() has an underscore, but tolist() doesn't!!!**

### Indexing

* `obj.set_index(keys, drop=False, append=False, inplace=False)`
* `obj.reset_index(drop=False, inplace=False)` -- reset index to default integer index; adds current index as a col to the df when drop=False

### Renaming & Replacing

* `df.rename(columns/index={'old_name': 'new_ name'})` -- rename specific columns (or index) with dict of old to new names
* `df.rename_axis('new_name', axis)` -- rename the axis
* `s.replace(1,'one')` -- replace all values equal to 1 with 'one'
* `s.replace([1,3],['one','three'])` -- replace all values equal to 1 with 'one' and all values equal to 3 with 'three'
* `df.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False)` -- replace values (passed per `to_replace` param) in a DataFrame per those passed via `value` param.


### Null Values - NEED FLESH OUT 

* `pd.isnull()` -- checks for null (NaN values in the data and returns an array of booleans, where "True" means missing and "False" means present
* `pd.isnull().sum()` -- returns a count of null (NaN)
* `pd.notnull()` -- returns all values that are NOT null

* `df.dropna(subset=[col1])` -- Drops all **rows** that contain null values in one or more specific columns and returns a new df
* `df.dropna(axis=1)` -- Drops all **columns** that contain null values and returns a new df
* `df.fillna(value=x)` —- replace all missing values with some value `x` (*S & df)
* `s.fillna(s.mean())` -- Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section)

### Duplicates

* `s.duplicated(keep='first')` -- return boolean Series denoting duplicate rows; by default keeps the first instance of a dup
* `s.drop_duplicates(keep='first', inplace=False)` -- return Series with dups removed; by default keeps the first instance of a dup
* `df.duplicated(subset=None, keep='first')` -- return boolean Series denoting duplicate rows; by default determines whether full row is a dup; by default keeps the first instance of a dup
* `df.drop_duplicates(subset=None, keep='first', inplace=False)` -- return df with dups removed; by default determines whether full row is a dup; 

### Filtering / Conditional Selection

* `obj.where(cond, other = NaN, inplace = False, axis = None)` -- replace values in the object where the condition is False (*S or df)
* `.isin()`

### Apply


### Map


## Structuring


* `df.drop(axis, labels, index, columns=[col1, col2, ...])` -- drops specified columns from the dataframe
* `insert(<position>,<column_name>, <data>)`

### Sorting

* `s.sort_values(ascending=False, inplace=False)` -- sort values of a Series in ascending order
* `df.sort_values(by=[col1, col2], ascending=False, inplace=False)` -- sort df rows by col1, then by col2; descending order by default

>>* `df.sort_index(axis=0, ascending=True, inplace=False)` -- sort axis values by index in *ascending* order


### Grouping


### Combining


### Reshaping



## Statistics


### Normalization



