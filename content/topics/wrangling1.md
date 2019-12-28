# Data Wrangling I - 👷‍♀️🚧 UNDER CONSTRUCTION 🚧👷‍♀️

Over the next few lessons, we will use Pandas to wrangle, clean, explore, analyze, and visualize data. We know that the data science lifecycle is NOT made of discrete, linear steps. As such, we will not review one-off examples of each function or attribute. Instead, we will walk through the analysis of a dataset together. We will integrate Pandas examples based on how and when we need to use them.

This might get a little confusing, so brace yourself! Ultimately though, this approach will help you apply the material on your own much more easily. To help keep things as consistent as possible, we'll use the same dataset across units. We also created a **[categorized cheat sheet of common Pandas functions](../resources/pandas_cheat_sheet.md)**.

* rename Genre col to Genres
	* replace
* sort by imdbID (or title)
* unique values (Type & totalSeasons)
	* nunique
* drop col
* dropna
	* or fillna w. mean
* drop dups
	* # dups
* add column for Average Rating across sources
	- add single row
	- concat
	- merge
* update
	* single value
	* remove "min" from Runtime and cast to int so that you can do math
* replace
* iterate through Genres and separate strings to list
* 

## Iterating Through Data

`.iterrows()`


```python
movies.sort_values(by="imdbRating", ascending=False, inplace=True)
temp = movies.head(5)

d = None # how to grab the rows without the index or col labels?
i = temp.index
c = temp.columns

top5_movie = pd.DataFrame(data = d, index = i, columns = c)
# pd.DataFrame(data = [], index = [], columns= [])

for idx, row in top5_movie:
	print(i, 'is', row)
```





