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

* `drop_duplicates([subset, keep, inplace])` -- returns DataFrame with duplicate rows removed, optionally only considering certain columns.

```python
print('ROWS BEFORE:', len(movies))

movies = movies.drop_duplicates()

print('ROWS AFTER:', len(movies))
```

Note: If you run this cell more than once, the before and after lengths will be equal because you already dropped the dups.



```python

```

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
