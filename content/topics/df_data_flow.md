# How Data Flows through DataFrames



## Adding & Updating Columns


```python
omdb_top25 = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/top_25.csv')
top25 = omdb_top25.copy()
top25
```



```python
seen = pd.Series()
top25.insert(loc=2, column='Seen', value=seen)
top25
```


```python

```

>>update seen col (partial data)

```python

```

```python

```

```python

```



* Insert columns at different locations
* Add and update columns with partial data