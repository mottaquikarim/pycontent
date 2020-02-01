# OMDb Movies Pandas Content Outline

>>.str.contains()????
>>concat()
>>.isin()??
>>multiple condition filtering
    >>"To combine filtering conditions in Pandas, use bitwise operators ('&' and '|') not pure Python ones ('and' and 'or')"


>>https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6


>>* created a calculated col that is the average of the rating across the 3 sources
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
GROUPBY 
>>https://chrisalbon.com/python/data_wrangling/pandas_apply_operations_to_groups/
>>https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html

Encoding:
>>https://www.dataschool.io/python-pandas-tips-and-tricks/#encodingdata
`get_dummies(data[, prefix, prefix_sep, …])`: Convert categorical variable into dummy/indicator variables.
`factorize(values, sort, na_sentinel, …)`: Encode the object as an enumerated type or categorical variable.
`cut(x, bins, right[, labels])`: Bin values into discrete intervals.
`qcut(x, q[, labels])`: Quantile-based discretization function.





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

## DATA VIZ

https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972



## Apply / Map

Instead, to edit all the data in a Python list or dict object, you have to iterate through and change each item individually. For Pandas objects, iterating through pandas data objects is not recommended because once your data gets large enough, iteration can cause significant latency in your program. Instead, where possible, you should always apply vectorized operations to Series and dataframe objects. That might mean applying some mathematical operation or even a custom function. 

>>As such, it's actually inefficient to iterate through the items or rows in a Series or dataframe when you want to edit the data. The main use case for iterating through these objects is simply to access the data for some purpose. For example, you might be checking its validity upon ingesting it, sending data you've recorded to a client, etc.

"They follow a common pattern:
1. Write a function that works on a single value
2. Test that function on a single value
3. Apply that function to a whole column"
