# Data Wrangling I - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.


* sort by imdbRating
* remove duplicate imdbIDs
    * remove duplicates based on a certain col
* rename cols (imdb, genres, languages)
* add / drop cols
* filter out Type == video series
    * unique / nunique
    * value_counts()
    * pd.isnull / pd.notnull


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


### Duplicate Values

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

