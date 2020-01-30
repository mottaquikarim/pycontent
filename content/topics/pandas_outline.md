# OMDb Movies Pandas Content Outline

>>.str.contains()????
>>.replace()
>>merge()
>>join()
>>concat()
>>.isin()??
>>multiple condition filtering
    >>"To combine filtering conditions in Pandas, use bitwise operators ('&' and '|') not pure Python ones ('and' and 'or')"

Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

```python
# top_oceania_wines = reviews[(reviews['country'] == 'Australia' | reviews['country'] == 'New Zealand') & (reviews['points'] >= 95)]

top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)
]
```


>>https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6


>>* created a calculated col that is the average of the rating across the 3 sourcesß
>>* Actors should be a real list also
	* fun activity to order EACH row's actor list in order of how many films they've been in?

>>Text analysis?

```python
.str.contains()
.isin()


desc = reviews.description

tropical_count = desc.map(lambda d: 'tropical' in d).sum()
fruity_count = desc.map(lambda d: 'fruity' in d).sum()

descriptor_counts = pd.Series([tropical_count, fruity_count], index=['tropical', 'fruity'])
descriptor_counts
```

## EDA Objectives / (or EDA?)

>>relative frequencies
https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
>>correlation?
>>word frequency in the plot col?
>>
>>regression?
>>stats?
>>
>>* groupyby https://chrisalbon.com/python/data_wrangling/pandas_apply_operations_to_groups/




>>np.where(cond[, other, inplace, axis, level, …])  Replace values where the condition is False.
`np.where(condition, then, else)`
`np.where(condition1, x1, 
        np.where(condition2, x2, 
            np.where(condition3, x3, ...)))`


* Normalizing, Centering, Scaling, Transform

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
