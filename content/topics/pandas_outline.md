# OMDb Movies Pandas Content Outline

## Data Wrangling I Objectives

* **Add, drop, & rename columns**
`.rename` a few
`.drop` ['Average Rating', 'Ratings', 'DVD', 'Awards', 'BoxOffice', 'Production', 'Poster', 'Website', 'Response']

* **Sort the data**
`.sort` by imdbRating, then Title

* **Count & drop duplicate rows**
count & drop dup full rows
count BUT NOT drop rows with dup title
count & drop rows with dup tital/year combin


* Count & drop (OR FILLNA) rows with null values
count & drop rows where imdbRating is null
count rows where RT rating is null (& fill with mean?)

fill or drop rows lacking Genre / Country / Language / Year / Runtime?


* Filter the data

>>Remove TV Series --> filter rows where type == series
1. `.nunique` & `.unique` / `value_counts` Type AND total Seasons
    * FIND THE DIFF....???
2. filter rows where type == series
3. pd.isnull film series with NaN totalSeasons
4. pd.notnull totalSeasons
5. ...remove the idx rows 
`.value_counts` to show how many movies vs. video series 

https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6


## Data Cleaning Objectives

* Genre is str representation of list. need to convert to actual list

>>* Find & replace data???

```python
.str.contains()
.to_numeric() # for the ratings that are in str format
.isin()


desc = reviews.description

tropical_count = desc.map(lambda d: 'tropical' in d).sum()
fruity_count = desc.map(lambda d: 'fruity' in d).sum()

descriptor_counts = pd.Series([tropical_count, fruity_count], index=['tropical', 'fruity'])
descriptor_counts
```

## Data Normalization Objectives


## Data Wrangling II Objectives / (or EDA?)

>>relative frequencies
https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
>>correlation?
>>regression?
>>stats?
>>
>>* groupyby
>>merge()
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

>>np.where(cond[, other, inplace, axis, level, …])	Replace values where the condition is False.

https://realpython.com/python-data-cleaning-numpy-pandas/#tidying-up-fields-in-the-data

`np.where(condition, then, else)`
`np.where(condition1, x1, 
        np.where(condition2, x2, 
            np.where(condition3, x3, ...)))`

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





## Apply / Map

Instead, to edit all the data in a Python list or dict object, you have to iterate through and change each item individually. For Pandas objects, iterating through pandas data objects is not recommended because once your data gets large enough, iteration can cause significant latency in your program. Instead, where possible, you should always apply vectorized operations to Series and dataframe objects. That might mean applying some mathematical operation or even a custom function. 

>>As such, it's actually inefficient to iterate through the items or rows in a Series or dataframe when you want to edit the data. The main use case for iterating through these objects is simply to access the data for some purpose. For example, you might be checking its validity upon ingesting it, sending data you've recorded to a client, etc.

"They follow a common pattern:
1. Write a function that works on a single value
2. Test that function on a single value
3. Apply that function to a whole column"