# How Data Flows through DataFrames

## Intro

The syntax for adding or updating a dataframe's data is as simple as declaring a variable: `df[col_name] = series_name`. What if the data in your Series doesn't have all of the same index values in the same order though? It's important to understand how to get data to flow into the right place in your dataframe in different scenarios. This lesson will present examples for some of the most common use cases such as:

* Add a placeholder column (empty or filled with a default value)
* Insert columns at different locations on axis 1
* Add columns with only partial data and/or with extra index values
* Update a subset of existing dataframe rows, while also adding new ones

### Import Data

```python
import pandas as pd
import numpy as np

print('import successful')
```

For this exercise, we'll import a dataframe of the top 25 movies according to IMDb. Our goal is to mark which movies we have seen and add our personal rating for each of those. We'll call the dataframe `top25`.

```python
omdb_top25 = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/top_25.csv')
top25 = omdb_top25.copy()
top25
```

## Adding Columns

Add an empty column called "My Rating" to the end of the dataframe as a placeholder.

```python
top25['My Rating'] = pd.Series()
top25
```

Use `.insert(loc, column, value)` to add a column called "Seen" as the third column in the `top25` dataframe. It will have boolean values that represent whether or not we've seen the movie. For now, we want to add `False` as a default placeholder value for all rows. A few points to remember:

* Because the index labels here ARE the integer index positions, we can pass `range(25)` as the `index` argument.
* We're passing `False` as a default placeholder value. Because the index we're passing has 25 values, all 25 rows in this column will say `False`.
* The `loc` parameter refers to the index position on axis 1, where we want to insert this column.
* The `column` parameter will be the name (i.e. index label) for this new column.

```python
seen = pd.Series(data=False, index=range(25))
top25.insert(loc=2, column='Seen', value=seen)
top25
```

## Update Columns

The `df.update()` function allows you to update a dataframe with values passed to it from another dataframe or from a Series. Let's update the "Seen" column to mark all the movies we've seen as `True`. Below is a pre-made list containing the index labels of movies to flip to `True`.

**NOTE!** We set the `name` attribute of the `seen` Series specifically because `.update()` needs it to determine which column of the dataframe needs updating.

```python
seen_idx = [0, 1, 5, 6, 7, 10, 12, 13, 14, 16, 17, 19, 20, 22, 23]
seen = pd.Series(data=True, index=seen_idx, name='Seen')
seen
```

Once you run the cell, you can see clearly that this Series contains only a subset of the movies in the top25 dataframe. In addition, it also contains a few index labels for movies that don't exist in the `top25` dataframe. Watch what happens when we use `.update()` to refresh values in `top25` with values from the `seen` Series:

```python
top25.update(seen)
top25
```

There are 3 takeaways here:

* `.update()` maps the values from the `seen` Series to the corresponding values in the "Seen" column of `top25` by automatically matching up index labels.
* Index labels in `top25`, but NOT the `seen` Series remain unchanged.
* Index labels in the `seen` Series, but NOT in `top25` are skipped over instead of added to `top25` as new rows.

```python
my_ratings_dict = {
    0: 6, 
    1: 9.2,
    5: 6.6, 
    6: 8.7, 
    7: 5, 
    10: 6, 
    12: 7.5, 
    13: 10, 
    14: 7.9, 
    16: 6.3, 
    17: 8.8, 
    19: 8, 
    20: 7.8, 
    22: 8.5, 
    23: 5.7
}
```

Let's say that the dict above contains your personal rating for each of the movies we've seen. We can turn this into a Pandas Series...

```python
my_ratings_series = pd.Series(data=my_ratings_dict, name='My Rating', dtype='float64')
my_ratings_series
```

...and use it to update the "My Rating" column.

```python
top25.update(my_ratings_series)
top25
```

## Conclusion

Finally, we'll combine these concepts by adding a column called "Average Rating". To do this, we have to create a Series that is:

* derived from multiple columns, but
* only contains data for a subset of the original dataframe's rows

Here's the step-by-step logic:

1. First, we'll take the subset of index values we need from the dict of our personal ratings. 
2. For each of the movie's we've seen, we want to find the average of the IMDb rating and our personal rating. Create an empty list to hold these values.
3. Write a loop to iterate through the subset of movies we've seen and calculate the average rating.

```python
my_ratings_ids = list(my_ratings_dict.keys())
avg_rating_list = []

for i in my_ratings_ids:
    a = top25.iloc[i, 3]
    # or .loc here bc same in this instance
    b = top25.iloc[i, 4]
    avg = (a + b)/2
    avg_rating_list.append(avg)
```

4. Create a Series by passing the list of average ratings to `data` and the list of movies we've seen to `index`. Remember to set `name` to the exact same label as the target column in the `top25` dataframe.

```python
avg_rating_series = pd.Series(data= avg_rating_list, index= my_ratings_ids , dtype='float64', name='Average Rating')
avg_rating_series
```

5. Insert this Series to `top25` at index position 3 with `.insert()`. (Alternatively, you could use the simpler sytax if you wanted to add it to the end of the dataframe: `top25['Average Rating'] = avg_rating_series`.)

```python
top25.insert(loc=3, column='Average Rating', value=avg_rating_series)
top25
```

As you can see, when we inserted the "Average Rating" column, all the movies not in the Series we built get set as `NaN`. Finally, if our `avg_rating_series` contained rows for movies not in `top25`, those rows would **NOT** be added to the dataframe via either column insertion method.

