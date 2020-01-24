# Expand List-Like Cols

.explode()
.str.split('<char>', expand=False) # True

### Mapping Strings to Lists

The `Genres`, `Country`, and `Languages` columns often hold more than one value per row. But when we pulled this data from the API, we got the contents of each cell in the form of a single string with the values separated by commas. If we want to evaluate the different categories within each of these variables, we need to break out the individual values from the string into list format.

### Genres

Count and view the rows with missing `Genres` data:

```python
missing_genre = movies[pd.isnull(movies['Genres'])]
print(movies['Genres'].isna().sum())
missing_genre
```

We could pass `na_action='ignore'`, but since there are only 3, we might as well look them up and fill in the info ourselves. We can check this by making sure the count of nulls afterward is 0.

```python
genre_updates = {
    'tt8026554': 'Drama',
    'tt6215446': 'Comedy, Horror',
    'tt10084752': 'Documentary'
}

for imdbID, genre in genre_updates.items():
    movies.loc[imdbID, 'Genres'] = genre

print(movies['Genres'].isna().sum())
```

Now, let's make a copy of the `Genres` column to operate on.

```python
temp_genre = movies['Genres'].copy()
```

To turn each string into a list, all we have to do is split each string at the commas. 

Now we can map the `Genres` variable using `lambda x: x.split(',')`.

```python
temp_genre = temp_genre.map(lambda x: x.split(','))
temp_genre
```

Reassign the original column to our manipulated Series.

```python
movies['Genres'] = temp_genre
movies['Genres']
```

### Country

We can do the same for the `Country` variable. First, check how many null values there are.

```python
null_country = movies[pd.isnull(movies['Country'])].copy()
print(movies['Country'].isnull().sum())
null_country
```

None, so we can proceed right away with copying the column.

```python
temp_country = movies['Country'].copy()
```

Use the same mapping strategy of `lambda x: x.split(',')`.

```python
temp_country = temp_country.map(lambda x: x.split(','))
temp_country
```

Reassign the original column to our manipulated Series.

```python
movies['Country'] = temp_country
movies['Country']
```