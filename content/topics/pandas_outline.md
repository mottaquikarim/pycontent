# OMDb Movies Pandas Content Outline

## Data Wrangling I Objectives

* **Document metadata based on common standards**


* **Add, drop, & rename columns**


* **Sort the data**


* Count & drop duplicate rows


* Count & drop (OR FILLNA) rows with null values


* Filter the data


https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6


## Data Cleaning Objectives

* Genre is str representation of list. need to convert to actual list

>>* Find & replace data???

```python
.str.contains()
.to_numeric() # for the ratings that are in str format



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

In Pandas, the `.iterrows()` method of iterating supplies a balance between efficiency and simplicity of use. It's similar in both concept and syntax to looping through the key/value pairs in a Python dict:

**Dict**: `for key, value in my_dict.items():`
**Series or dataframe**: `for idx, row in obj.iterrows():`


```python
temp = movies.copy()
temp = 

for idx, row in temp.iterrows():
    # print(f'{idx}: {row}\n\n')
    # print(temp.loc[idx])
    print(row['Year'], type(row['Year']))
    row['Year'] = int(row['Year'])
    print(row['Year'], type(row['Year']), '\n')
```