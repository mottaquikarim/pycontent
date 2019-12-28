# Data Wrangling I - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.

## Objectives

* Sorting
* Counting & dropping duplicate rows
* Renaming Columns
* 

### Sorting

You can sort a Series or dataframe by different ==ELEMENTS== and specs with the `.sort_values()` method. Its general syntax and default parameter arguments (where applicable) are as follows:

`.sort_values(by, axis=0, ascending=False, inplace=False, na_position=last)`

The `by` parameter takes one or more columns from the dataframe. The method will sort by the first column passed, then the second, and so on. Since a Series is effectively a single column, the `by` parameter isn't required when sorting a Series object.

If you're sorting based on multiple columns, you have the option to specify the order in which to sort each column. Let's say you pass in `by=[col1, col2], ascending=[True, False`. This would sort the rows based on the values in col1 in **ascending** order, THEN sort by the values in col2 in **descending** order. If you only pass one argument to ascending, it will sort all the columns passed to `by` in that order.

If any of the columns you pass to the `by` parameter contain null values, you can choose whether to places those rows first or last using the `na_position` parameter.

```python
movies.head(3)
```

```python
movies.sort_values(by=['imdbRating', 'Title'], ascending=False, inplace=True, na_position=True)
movies.head(3)
```

### Drop Duplicates
* remove duplicate imdbIDs
    * remove duplicates based on a certain col

* `df.duplicated([subset, keep])` -- Return boolean Series denoting duplicate rows

When finding dups, you can choose to consider a `subset` of columns or check whether entire rows are the same across all columns. The `keep` param denotes the occurrence which should be marked as duplicate. You can choose `first` or `last`, but the default is `first`. In other words:

* first : All duplicates except their first occurrence will be marked as True
* last : All duplicates except their last occurrence will be marked as True

**Count the number of dups**

Shows number of Trues and Falses; number of Trues is how many dups there are

```python
movies.duplicated().sum()
```

```python
movies.duplicated().value_counts()
```

whole row vs. dup titles 

```python
movies.duplicated(['Title']).value_counts()
```

**Return a new df of rows containing dups**

```python
dup_rows = movies[movies.duplicated()]

print(len(dup_rows))
dup_rows.head(5)
```

**Drop duplicates**

* `drop_duplicates([subset, keep, inplace])` -- returns DataFrame with duplicate rows removed, optionally only considering certain columns.

```python
print('ROWS BEFORE:', len(movies))

movies = movies.drop_duplicates()

print('ROWS AFTER:', len(movies))
```

Note: If you run this cell more than once, the before and after lengths will be equal because you already dropped the dups.



```python

```

### Organizing Cols

* rename cols (imdb, genres, languages)
* add / drop cols

### Remove Non-Movies

* filter out Type == video series
    * unique / nunique
    * value_counts()
    * pd.isnull / pd.notnull





>>OUTLINE

* dropna
    * or fillna w. mean


* replace (production companies?)
* append single row vs. concat multiple rows
* merge
* 
* update
    * single value
    * remove "min" from Runtime and cast to int so that you can do math

* iterate through Genres and separate strings to list
    * then do via .apply()

## Iterating Through Data

Because Series and dataframe objects allow vectorized operations, 

```python
i = 0

while i < 10:
    row = movies.iloc[i]
    print(row.loc['Title'])
    i += 1
```

`.iterrows()`


```python
movies.sort_values(by="imdbRating", ascending=False, inplace=True)
temp = movies.head(5)

d = None # how to grab the rows without the index or col labels?
i = temp.index
c = temp.columns

top5_movie = pd.DataFrame(data = d, index = i, columns = c)
# pd.DataFrame(data = [], index = [], columns= [])

for idx, row in top5_movie:
    print(i, 'is', row)
```
