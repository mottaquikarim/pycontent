# Lists

In order to begin to truly write dynamic programs, we need to be able to work with data even when we do not know how much we have. Since *variables hold only one item*, Python has some objects that hold collections of data. A **list** object is one of those. **Lists** hold multiple items, called **elements**. List elements can represent any data type, and most, importantly, *a single list can hold any mix of different data types, **including other lists**.*

## Creating lists

To declare a new list varaible, you have two options -- `[]` or `list()`. The `[]` syntax is a bit more straightforward. If you choose to use the `list()` method, you still have to pass the items to it within `[]` because it will only accept **one** parameter...

```python
# Empty
empty1 = []
empty2 = list()
```
```python
# Mixed Data Types
mix1 = [True, ['seal', 'spider monkey'], 22, 'lion', [False, 13]]
mix2 = list([True, ['seal', 'spider monkey'], 22, 'lion', [False, 13]])
```
```python
# Nested List
nested1 = [['circus', 'clown'], ['trapeze', 'artist']]
nested2 = list([['circus', 'clown'], ['trapeze', 'artist']])
```

The `list()` method can be tricky. Here's what happens if you pass more than one item to it:

```python
colors = list('red', 'yellow', 'green')
### TypeError: list() takes at most 1 argument (3 given)
```
Even if you do pass only *one* item, you still have to enclose it with `[]`. If you pass a single number or a single boolean without using brackets, you'll get a `TypeError`.

```python
x = list(100) # or any float e.g. 100.0
### TypeError: 'int' object is not iterable

y = list(True) # booleans
### TypeError: 'bool' object is not iterable
```
And if you pass a string without using brackets, you won't get quite what you want.

```python
z = list('Layla')
print(z)
# ['L', 'a', 'y', 'l', 'a']
```
And if you think it works for sentences by parsing a new list element at each space character...*nope!*

```python
sentence = list('I like to sing!')
print(sentence)
# ['I', ' ', 'l', 'i', 'k', 'e', ' ', 't', 'o', ' ', 's', 'i', 'n', 'g', '!']
```

## Accessing Elements in the List

The **list index** means the location of each element in the list. List indexes start counting at 0!

|  List | "Brandi" | "Zoe" | "Steve" | "Aleksander" | "Dasha" |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |


To access one of them use the syntax `list_name[index_position]`.

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
print(my_class[0]) # Prints "Brandi"
print(my_class[1]) # Prints "Zoe"
print(my_class[4]) # Prints "Dasha"
```
What if you want to grab a single element from a list nested within a list though? Simply add another level of index selection.

```python
nested_lists = list([['circus', 'clown'], ['trapeze', 'artist']])
print(nested_lists[0][0]) # circus
print(nested_lists[1][0]) # trapeze
```

The `len()` function will give you the total number of list elements (regardless of data type).

```python
my_class = ['Brandi', 'Zoe', 'Aleksander', 'Dasha']
num_students = len(my_class)
print(num_students) # 5
```
>>**REMEMBER!** 
>>Because the index starts at 0, the index position of the last item in the list will NOT be equal to the list's length.

If you pass in any list index greater than or equal to the length of the list, you will get an `IndexError`:

```python
print(my_class[num_students])
### IndexError: list index out of range
```
Aside from merely finding the length, `len()` comes in handy if you need to dynamically select the last element of a list. Logically, the length of the list minus 1 will give you the index of the last list element, i.e. `index_of_last_element = len(list_name) - 1`.

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
num_students = len(my_class)

# (num_students - 1) is the index of the last element
print(my_class[num_students - 1]) # Dasha
```

That brings us to something called **negative indexing**. Because of the above rule, Python allows you to take this shortcut to access the last list element:

```python
print(my_class[-1])
```
Likewise, as you count backwards from the last list element, the negative index extends...

```python
print(f'2nd to last item is {my_class[-2]}')
print(f'3rd to last item is {my_class[-3]}')
```

### Selecting Ranges

To select multiple items from a list, simply pass the range of indeces which hold the desired elements, e.g. `my_list[2:7]`. It's important to remember that **the upper bound is NOT inclusive**. In other words, if you want the elements at index 3 and index 4, you have to write `[3:5]`. (Likewise, `my_class[1:1]` would print nothing.) 

```python
my_class = ['Roxanne', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
print(my_class[3:5])
```
Ommitting one or both bounds acts as a shortcut when the length and order of your list might vary. It allows you to say, "Give me everything from the beginning of the list to index `x`" or "Give me everything from index `x` and onward."

```python
my_class = ['Roxanne', 'Zoe', 'Steve', 'Aleksander', 'Dasha']

print('[:2] -- ', my_class[:2]) # All indeces up to, but NOT including index 2

print('[2:] -- ', my_class[2:]) # Index 2 through end of list
```

#### Practice together!

```python
pets = ['dog', 'cat', 'guinea pig', 'ferret', 'bird', 'lizard']

# Print index 1:


# Print ['guinea pig', 'ferret']:


# Print the 5th element:


# Print all elements up to and INCLUDING 'ferret':


# Print 'dog':


# Print all elements from 'ferret' onwards:


```

## Editing List Content

### Add Items to a List
If you want to add elements to a list, you can use any of the below methods:

* `.append()`: adds items to the end of a list in one chunk
* `.extend()`: adds items to the end of a list individually
* `.insert(index, value)`: adds an item to a specific position in the list
* `[index] = value`: adds item to a specific position in the list

Let's go through some examples. First, we'll look at the difference between `.append()` and `.extend()`. As mentioned above, `.append()` will add whatever value or group of values you pass it *in one chunk*. In contrast, if you pass a group of values into `.extend()`, it will add *each* element of the group *individually*. 

**APPEND**

```python
pies = ['apple', 'pumpkin', 'pecan', 'blueberry']
more_pies = ['lemon meringue', 'strawberry peach', 'banana cream']

pies.append(more_pies)
print(f'.append(): {pies}\n')
```
**EXTEND**

```python
pies = ['apple', 'pumpkin', 'pecan', 'blueberry']
more_pies = ['lemon meringue', 'strawberry peach', 'banana cream']

pies.extend(more_pies)
print(f'.extend(): {pies}')
```

In the next example, take a look at how `.extend()` only considers individual values of the parent list passed in. It still adds the nested lists - `['f', 'g']` and `['h', 'i']` - to our list `x` as their own items.

```python
# APPEND
x = ['a', 'b', 'c', 'd']
y = ['e', ['f', 'g'], ['h', 'i'], 'j']
x.append(y)
print(y)
# ['a', 'b', 'c', 'd', ['e', ['f', 'g'], ['h', 'i'], 'j']]


# EXTEND
x = ['a', 'b', 'c', 'd']
y = ['e', ['f', 'g'], ['h', 'i'], 'j']
x.extend(y)
print(x)
# ['a', 'b', 'c', 'd', 'e', ['f', 'g'], ['h', 'i'], 'j']
```

#### `.insert(index, value)`

If you want to add an item to a specific point in your list, you can pass the desired index and value into `.insert()` as follows.

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
my_class.insert(1, 'Sanju')
print(my_class)
# ['Brandi', 'Sanju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
```
Whatever you pass into the `value` parameter will be added as a single element though!

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
my_class.insert(1, ['Sanju', 'Reginald'])
print(my_class)
# ['Brandi', ['Sanju', 'Reginald'], 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
```

### Remove Items from a List

Likewise, you can use `.pop()` or `.pop(index)` to remove any type of element from a list.

#### `.pop()`
- Removes an item from the end of the list.

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
student_that_left = my_class.pop()
print(f'{student_that_left} has left the class.')
# Sonyl has left the class.
print(my_class)
# ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
```

#### `.pop(index)`

- Removes an item from the list.
- Can take an index.

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
student_that_left = my_class.pop(2) # Remember to count from 0!
print('The student', student_that_left, 'has left the class.')
# 'Steve'
print(my_class)
# => ['Brandi', 'Zoe', 'Aleksander', 'Dasha']
```

### Edit Items in a List

#### Update/Replace Items

To replace items in a list, you reference them by their index value and simply declare a new value for that element.

```python
x = ['Brandi', 'Sanju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']

x[1] = 'Raju'
x[4:] = ['Chloe', 'Phoebe']
print(x)
```

## Summary

==need to recreate==

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/Lists_Summary.png?raw=true" width="100%" align="left"/>

