pandas_iteration.md

## Iterating Through Data

To edit all the data in a Python list or dict object, you have to iterate through and change each item individually. As we discussed in the last section, you can apply vectorized operations to Series and dataframe objects. That might mean applying some mathematical operation or even a custom function. As such, it's actually inefficient to iterate through the items or rows in a Series or dataframe when you want to edit the data. The main use case for iterating through these objects is simply to access the data for some purpose. For example, you might be checking its validity upon ingesting it, sending data you've recorded to a client, etc.

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


4
# iterate over the dataframe row by row
for index_label, row_series in salaryDfObj.iterrows():
   # For each row update the 'Bonus' value to it's double
   salaryDfObj.at[index_label , 'Bonus'] = row_series['Bonus'] * 2
