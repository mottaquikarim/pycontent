# Data Wrangling II



## Objectives (part I)

* Document metadata based on common standards
* Add, drop, & rename columns 
* Sort the data
* Count & drop duplicate rows
* Count & drop rows with null values
* Filter the data


## Objectives (part II)

>>* Find & replace data???
>>* Reformat
>>* Normalize 
>>* groupyby

## Data Dictionaries

merge()
>>join()
>>concat()


>>OUTLINE

* dropna
    * or fillna w. mean


* filter out Type == video series
    * unique / nunique
    * value_counts()
    * pd.isnull / pd.notnull

reviews.loc[reviews.country == 'Italy']

* replace (production companies?)

>>* append single row vs. concat multiple rows???
>>* merge???

* update
    * single value
    * remove "min" from Runtime and cast to int so that you can do math

* apply() 
    * convert list as str to real list
    * https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/
    * then do via .apply()

* Normalizing, Centering, Scaling, Transform

The function you pass to map() should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. map() returns a new Series where all the values have been transformed by your function.

apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

```python
# MAP()
m = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p-m)

# APPLY()
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```
