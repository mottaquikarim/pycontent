# OMDb Movies Pandas Content Outline

>>concat()


## EDA Objectives / (or EDA?)

>>* created a calculated col that is the average of the rating across the 3 sources

* Normalizing, Centering, Scaling, Transform

`cut(x, bins, right[, labels])`: Bin values into discrete intervals.
`qcut(x, q[, labels])`: Quantile-based discretization function.

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




>>Text analysis?
    >>word frequency in the plot col?

```python
.str.contains()
.isin()

desc = reviews.description

tropical_count = desc.map(lambda d: 'tropical' in d).sum()
fruity_count = desc.map(lambda d: 'fruity' in d).sum()

descriptor_counts = pd.Series([tropical_count, fruity_count], index=['tropical', 'fruity'])
descriptor_counts
```


## CATEGORICAL VARS

Encoding:
>>https://www.dataschool.io/python-pandas-tips-and-tricks/#encodingdata
`get_dummies(data[, prefix, prefix_sep, …])`: Convert categorical variable into dummy/indicator variables.
`factorize(values, sort, na_sentinel, …)`: Encode the object as an enumerated type or categorical variable.








## DATA VIZ

https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972

>>omdb data viz lab from PYTH2: https://colab.research.google.com/github/mottaquikarim/PythonProgramming/blob/master/app/src/Notebooks/omdb_viz_solution.ipynb#scrollTo=JMjiEiyRT1ey

## OTHER

>>np.where(cond[, other, inplace, axis, level, …])  Replace values where the condition is False.
`np.where(condition, then, else)`
`np.where(condition1, x1, 
        np.where(condition2, x2, 
            np.where(condition3, x3, ...)))`
