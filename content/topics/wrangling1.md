# Data Wrangling I - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.

### Sorting

`.sort_values(by, axis, ascending=False, inplace=False, na_position=last)`

* Put one or more columns in the `by` parameter
* The `ascending` parameter is True by default

*Example:*
`df.sort_values(by=[col1,col2], ascending=[True,False], inplace=False)`
*This sorts values in a col1 in **ascending** order, THEN sorts values in col2 in **descending** order*

```python
movies.head(3)
```

```python
movies.sort_values(by=['imdbRating', 'Title'], ascending=False, inplace=True)
movies.head(3)
```

### Drop Duplicates
* remove duplicate imdbIDs
    * remove duplicates based on a certain col





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
