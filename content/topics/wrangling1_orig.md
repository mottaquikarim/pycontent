# Data Wrangling I

## Objectives

>>* Document metadata based on common standards
* Add, drop, & rename columns 
* Sort the data
* Count & drop duplicate rows
* Count & drop rows with null values
* Filter the data
>>* Find & replace data
>>* Reformat
>>* Normalize 

### Add, Drop, & Rename Columns


### Sorting

Using the `.sort_values()` method.You can sort a Series or dataframe by different criteria using the `.sort_values()` method. Its general syntax and default parameter arguments (where applicable) are as follows:

`.sort_values(by, axis=0, ascending=False, inplace=False, na_position=last)`

The `by` parameter takes one or more columns from the dataframe. The method will sort by the first column passed, then the second, and so on. Since a Series is effectively a single column, the `by` parameter isn't required when sorting a Series object.

If you're sorting based on multiple columns, you have the option to specify the order in which to sort each column. Let's say you pass in `by=[col1, col2], ascending=[True, False`. This would sort the rows based on the values in col1 in **ascending** order, THEN sort by the values in col2 in **descending** order. If you only pass one argument to ascending, it will sort all the columns passed to `by` in that order.

If any of the columns you pass to the `by` parameter contain null values, you can choose whether to place those rows `first` or `last` using the `na_position` parameter.

For our movies dataset, it makes logical sense to sort the movies in order of most to least popular or well-known. We have three different movie ratings sources which can serve as a measure of that for us - IMDb, Rotten Tomatoes, & Metacritic. (The "Ratings" column is an aggregate of these, and the "Internet Movie Database" column is a duplicate of "imdbRating.") Which should we use then? If you take a look at `movies.info()`...

```python
movies.info()
```

...you'll see that IMDb has the most the non-null values


Above, are the 
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

## Filtering

### Remove Non-Movies

* filter out Type == video series
    * unique / nunique
    * value_counts()
    * pd.isnull / pd.notnull
    * .isin()

reviews.loc[reviews.country == 'Italy']
"To combine filtering conditions in Pandas, use bitwise operators ('&' and '|') not pure Python ones ('and' and 'or')"

Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

```python
# top_oceania_wines = reviews[(reviews['country'] == 'Australia' | reviews['country'] == 'New Zealand') & (reviews['points'] >= 95)]

top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)
]
```


...?