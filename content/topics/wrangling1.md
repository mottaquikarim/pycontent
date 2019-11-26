# Data Wrangling I

## Selecting Data

First, let's set the index back to `imdbID`.

```python
movies.set_index(['imdbID'], inplace=True)
```
### Columns


### Rows
.loc vs. iloc


### Cells

.loc vs. iloc


Select a:
* Row
* Column
* Single item from a specific row, column
* Slice of Rows
* Subset of columns (return as a new df)
* Slice of series values (by index and by label)


## Iterating Through Data