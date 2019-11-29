# Pandas Cheat Sheet - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

<img src="https://news.nationalgeographic.com/content/dam/news/2015/12/15/pandas/01pandainsemination.ngsversion.1450209600474.adapt.1900.1.jpg" style="margin: 0 auto; width: 50%; display: block;"/>

## Reading & Writing Data

* **`pd.read_csv(<file_path>)`** -- From a CSV file
* **`pd.read_table(<file_path>)`** -- From a delimited text file (like TSV)
* **`pd.read_excel(<file_path>)`** -- From an Excel file
* **`pd.read_sql(query, connection_object)`** -- Reads from a SQL table/database
* **`pd.read_json(json_string)`** -- Reads from a JSON formatted string, URL or file.
* **`pd.read_html(url)`** -- Parses an html URL, string or file and extracts tables to a list of dataframes
* **`df.to_csv(<file_path>)`** -- Writes to a CSV file
* **`df.to_excel(<file_path>)`** -- Writes to an Excel file
* **`df.to_sql(table_name, connection_object)`** -- Writes to a SQL table
* **`df.to_json(<file_path>)`** -- Writes to a file in JSON format
* **`df.to_html(<file_path>)`** -- Saves as an HTML table

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
    * **`df.loc[row_start : row_end]`** -- index labels
* Select a slice of a DataFrame by entering a range of row and column...
    * **`df.loc[row_start : row_end , col_start : col_end]`** -- index labels
    * **`df.iloc[row_start : row_end , col_start : col_end]`** -- index positions


## Data Wrangling

## Basic Stats

## Organizating Data