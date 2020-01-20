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




## Dropping Extra Columns

First, let's get rid of some clutter by dropping a few columns we definitely won't need. The general syntax is:

*`df.drop(columns, inplace=False)`*

Piece of cake. Reference the name of the dataframe and specify which columns to drop. The **most crucial takeaway** at this point is that `inplace` parameter. By default, that argument is set to `False` because it could cause problems with running other cells in your notebook. For example...

Run this cell:

```python
movies['BoxOffice']
```

Now let's drop these extraneous columns:

```python
print(f'BEFORE: \n{movies.columns}')
movies.drop(columns=['Ratings', 'DVD', 'Awards', 'Internet Movie Database', 'BoxOffice', 'Production', 'Poster', 'Website', 'Response'], inplace=True)
movies.columns
```

Go back and re-run the cell `movies['BoxOffice']` cell. KeyError... because you dropped that col from the dataframe earlier in the session. The only way to print that BoxOffice column now is to reload the data from the csv.

### Add, Drop, & Rename Columns


### Drop Duplicates
* remove duplicate imdbIDs
    * remove duplicates based on a certain col

* `.duplicated([subset, keep])` -- Return boolean Series denoting duplicate rows

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