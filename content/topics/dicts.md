# Dicts

## Intro

In addition to lists, another more comprehensive method for storing complex data are **dicts**, or dictionaries. In this lesson, you'll:

* Define the rules for the structure of dict objects
* Create dicts using 4 different methods
* Access dict data
* Edit dict content

## Dict Structure

In the example below, we associate a `key` (e.g. 'taq') to a `value` (e.g. 'karim'). Instead of being enclosed in `[]`, dicts are enclosed in `{}`.

```python
my_dict = {
    'key' : 'value'
}
```
The keys and values of a single dict don't have to be homogenous. In other words, you can mix and match different key, value, and key/value pair data types within one dict as seen below.

```python
dict1 = {
    'taq': 'karim',
    'apple': 35,
    False: 87.96,
    35: 'dog',
    'tree': True
    # etc.
}

print(dict1)
```

The `values` in a dict can be any valid Python data type, but there are some restrictions on what you can use as `keys`:

*1. Keys **CAN** be strings, integers, floats, booleans, and tuples.* 

*2. Keys **CANNOT** be lists, sets, or dicts.*

Do you see the pattern here so far? The data in a *dict key must be immutable.* Since lists and dicts are mutable, they cannot be used as keys in a dict. That said, they *CAN* serve as the values in a dict.

```python
dict2 = {
    47: [12.1, 'blue', True], # list as a dict value
    'julianna': {False: 'cat'} # dict as a dict value
}
```

*3. Also, the keys in a dict _**must be unique**_.* You'll see why shortly... But remember -- be careful not to add a key to a dict a second time. If you do, the second item will _**override**_ the first item.

## Creating Dicts

There are several ways you can create your `dict`, but we'll go through the most basic ones here.

### Method 1: Pass in key value pairs directly using `{}`:


```python
food_groups = {} # this creates a new, empty dict

food_groups = {
    'pomegranate': 'fruit',
    'asparagus': 'vegetable',
    'goat cheese': 'dairy',
    'walnut': 'legume'
}

print(food_groups)
```

### Method 2: Convert a *list of tuples* into a dict using `dict()`

This is a good example of using typecasting on more complex data structures. 

```python
# list of tuples   
listofTuples = [("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]

wordFrequency = dict(listofTuples)
print(wordFrequency) # {'this': 77, 'there': 45, 'hi': 10, 'at': 23, 'Hello': 7}
```

### Method 3: Use `zip()` to convert two lists into dict keys and values

The `zip()` method takes the names of each list as parameters - the first list will become the dict's keys, and the second list will become the dict's values.

**NOTE!** *This only works if you're sure the key/value pairs have the same index position in their original lists (so they will match in the dict).*

```python
names = ['Taq', 'Valerie', 'Viktor', 'Zola']
scores = [[98, 89, 92, 94], [86, 45, 98, 100], [100, 100, 100, 100], [76, 79, 80, 82]]

grades = dict(zip(names, scores))
print(grades) # {'Taq': [98, 89, 92, 94], 'Zola': [86, 45, 98, 100], 'Valerie': [76, 79, 80, 82]}
```

## Accessing Dict Data

Once you've stored data in your dict, you'll need to be able to get back in and access it! Take a look at this dict holding state capitals.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston'
}
```

### Referencing Values by Keys

You *CANNOT* access dict items with index positions like you do with lists! If you try, you'll get a `KeyError` because dict items do not have index positions. **Instead, the dict keys serve the same purpose as indeces in lists.** Accordingly, you can access each value in the list by referencing its key like so:

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston'
}

MAcap = state_capitals['MA']
print(f'The capital of MA is {MAcap}.') # 'The capital of MA is Boston.'
```

Attempting to find a key that does not exist leads to error.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston'
}

print(state_capitals['PA']) # KeyError from missing key
print(state_capitals[2]) # KeyError from index reference
```

Instead, it's better to look up a key in a dict using `.get(key)`. The `.get(key)` method takes the key argument just as above EXCEPT it allows you to enter some default value it should return if the key you enter does not exist. Usually, we use `[]` as that value so that it's `.get(key, [])`.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston'
}

print(state_capitals.get('PA', []))
# PA is not in our dict, so .get() returns []
```

### Retrieving All Keys, Values, & Key/Value Pairs

Now, this dict has 4 keys, but what if it had *hundreds?* We can isolate pieces of the dict's data structure using these functions:

* `.keys()` -- returns a collection of all the keys in a dict 
* `.values()` -- returns a collection of all the values in a dict 
* `.items()` -- returns a collection of all the key/value pairs in a dict 

#### Isolating Keys & Values

Let's separate the keys and values from the `pets` dict below.

```python
pets = {
  'Taq': ['teacup pig','cat','cat'],
  'Francesca': ['llama','horse','dog'],
  'Walter': ['ferret','iguana'],
  'Caleb': ['dog','rabbit','parakeet']
}

pet_keys = pets.keys()
pet_values = pets.values()
```

You would think the `.keys()` and `.values()` functions return lists of the keys and values repsectively, right? Wrong. These functions return *list-LIKE* objects called `dict_keys()` and `dict_values()`. Run this cell to see the results summarized for you.

```python
print(f'''
Keys: 
{pet_keys}
{type(pet_keys)}
''')

print(f'''
Values: 
{pet_values}
{type(pet_values)}
''')
```

In contrast to lists, you CANNOT access the elements in either a `dict_keys` or a `dict_values` object by index. Here's what happens if you try to:

```python
try:
    print(pet_keys[0])
except TypeError as t:
    print(f'{t.__class__.__name__}: {t}')
    # TypeError: 'dict_keys' object is not subscriptable
```

The same error would occur if you tried that with a `dict_values` object. Because of this, it's often best to convert the objects to lists when you create them.

```python
pets = {
    'Taq': ['teacup pig','cat','cat'],
    'Francesca': ['llama','horse','dog'],
    'Walter': ['ferret','iguana'],
    'Caleb': ['dog','rabbit','parakeet']
}

pet_keys = list(pets.keys())
pet_values = list(pets.values())
```
Then you can easily access each key or value by index: 

```python
print(f'First Key: {pet_keys[0]}') # 'Taq'
print(f'First Value: {pet_values[0]}') # ['teacup pig','cat','cat']
```

#### Isolating Key/Value Pairs

You can access the full group of key/value pairs with `.items()`. Accordingly, `.items()` one will return a `dict_items` object.

```python
pets = {
  'Taq': ['teacup pig','cat','cat'],
  'Francesca': ['llama','horse','dog'],
  'Walter': ['ferret','iguana'],
  'Caleb': ['dog','rabbit','parakeet']
}

pet_kv_pairs = pets.items()

print(f'''
Key/Value Pairs: 
{pet_kv_pairs}
{type(pet_kv_pairs)}
''')
```

It looks like a list of tuples, right? Again, you'd think you could access each pair's tuple by index then, but you can't without first converting the `dict_items` object to a list like we did before.

```python
pets = {
  'Taq': ['teacup pig','cat','cat'],
  'Francesca': ['llama','horse','dog'],
  'Walter': ['ferret','iguana'],
  'Caleb': ['dog','rabbit','parakeet']
}

pet_kv_pairs = list(pets.items())
print(f'Key/Value Pairs: \n{pet_kv_pairs}\n{type(pet_kv_pairs)}\n\n')
# [('Taq', ['teacup pig','cat','cat']), ('Francesca', [['llama','horse','dog']), etc]

print(pet_kv_pairs[0])
# ('Taq', ['teacup pig','cat','cat'])
```

We'll learn *WHY* this is useful in the next section on iterating through dicts with loops!

## Methods for Modifying Dicts

Just like lists, you can edit, analyze, and format your dicts. Some work the same for dicts and lists such as `len()` -- that will give you the number of key/value pairs in the dict. However, adding, deleting, and updating data requires a little more detail for dicts than for lists.

### Add or Edit Dict Items

You can add a single item to dict in two ways. The first way is similar to updating a list...

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston'
}

state_capitals['CA'] = 'Sacramento'

print(state_capitals) # {'NY': 'Albany', 'NJ': 'Trenton', 'CT': 'Hartford', 'MA': 'Boston', 'CA': 'Sacramento'}
```

...but more likely you'll want to use the `.update({key: value})` method.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston'
}

state_capitals.update({'CA': 'Sacramento'})

print(state_capitals) # {'NY': 'Albany', 'NJ': 'Trenton', 'CT': 'Hartford', 'MA': 'Boston', 'CA': 'Sacramento'}
```

The `.update()` method also allows you to make bulk updates. In that case, you can simply pass it a variable containing another dict to add to the first one.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Trenton',
    'CT': 'Hartford',
    'MA': 'Boston',
    'CA': 'Sacramento'
}
more_states = {
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'NJ': 'Hoboken',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}

state_capitals.update(more_states)

state_capitals = {
    'NY': 'Albany',
    'NJ': 'Hoboken',
    'CT': 'Hartford',
    'MA': 'Boston',
    'CA': 'Sacramento',
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}
```

**Notice something?** It's easy to accidentally override items when you're merging datasets. *Oops, we just changed the capital of NJ to Hoboken!* Don't worry though - we'll learn an easy way to check for duplicate keys in the next section on loops.

### Remove Items from a Dict

#### `.clear()` simply empties the dict of all items.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Hoboken',
    'CT': 'Hartford',
    'MA': 'Boston',
    'CA': 'Sacramento',
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}

state_capitals.clear()
print(state_capitals) # {}
```

#### `.pop(key)`:

This removes an item, which you must specify by key. There are two things to note here -

1. **First**, you *cannot delete a dict item by specifying a value*. Since values do not have to be unique the way keys are, trying to delete items by referencing values could cause issues.
2. **Second**, just like we saw earlier with `.get(key)`, `.pop(key)` will raise a `KeyError` if you try to remove a key that does not exist in the dict. We avoid this in the same way, by setting a default value - typically `[]` - for the program to return in case of a missing key.

Unfortunately, you *can't* use the same method as we did for `.update()` to delete larger portions of data. You have to use a loop to do that.

```python
state_capitals = {
    'NY': 'Albany',
    'NJ': 'Hoboken',
    'CT': 'Hartford',
    'MA': 'Boston',
    'CA': 'Sacramento',
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}

state_capitals.pop('AZ', [])
# removes 'AZ': 'Phoenix' from our dict
```

## Iterating Through Dicts

Iterating over dicts is slightly more complicated than other iterables because each item consists of two elements, specifically mapped to each other. That said, you can do some really cool stuff with your dicts using loops! 

#### Example 1

Let's start with the most basic example. The loop below iterates over the dict by each *item*, i.e. each key-value pair.

```python
state_capitals = {
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}

for key, value in state_capitals.items():
    print(f'{key}: {value}')
```

#### Example 2

The below loop illustrates how to update multiple items in a dict without over-writing the values for existing keys. It also keeps track of which keys didn't get updated.

```python
state_capitals = {
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}

updates = {
    'CT': 'Hartford',
    'MA': 'Boston',
    'CA': 'Sacramento',
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin'
}

existing = set(state_capitals.keys())
dups = []

for key, value in updates.items():
    if key not in existing:
        state_capitals.update({key: value})
    else:
        dups.append(key)

print(state_capitals)
print(dups)
```

#### Example 3

Dicts are inherently unordered, so you can't sort them. However, you CAN use a loop to sort the keys and print out the records in the desired order.

```python
state_capitals = {
    'WA': 'Olympia',
    'OR': 'Salem',
    'TX': 'Austin',
    'AZ': 'Phoenix',
    'GA': 'Atlanta'
}

for key in sorted(transaction.keys()):
    print(f'{key}: {transaction[key]}')
```

## Key Takeaways

* To create a dict:
    * Pass comma-separated `key : value` pairs within `{}`
    * Pass a list of tuples to `dict()`
    * Pass two lists to `zip()`
* Unlike a list, a dict is inherently unordered and thus has no index.
* Access a value by referencing its key using `my_dict[key]` or `.get(key, [])`. The latter is preferable because it guards against `KeyErrors` from referencing missing keys.
* `my_dict[key] = value` and `.update({key: value})` both add or update a specific key/value pair based on whether the key passed exists already in the dict or not
    * You can also pass another dict into `.update()` in order to make bulk edits 
* `.update({key: value})` adds or updates a key/value pair based on whether the key passed exists already in the dict or not
* `.pop(key, value)` removes a key/value pair from the dict
* The following methods return list-like objects that isolate certains of a dict:
    * `.keys()` returns the keys
    * `.values()` returns the values
    * `.items()` returns the key/value pairs as tuples 
* `len(my_dict.items())` will return the number of pairs in the dict
* To iterate through a dict, use one of the following as the context requires:
    * `for key in my_dict.keys():`
    * `for value in my_dict.values():`
    * `for key, value in my_dict.items():`

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Try out all the dict PSETs in your copy of `dict_psets.ipynb` in Google Drive.