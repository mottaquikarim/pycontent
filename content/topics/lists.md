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

## Built-In Operations for Manipulating Lists

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

#### Join Items

If you need to, you can compile your list items into a single string using `.join()`. You CANNOT do this with lists of numbers, booleans, or a list containing a mix of strings and other data types though.

```python
letters = ['j', 'u', 'l', 'i', 'a', 'n', 'n', 'a']
name = ''.join(letters)
print(name) # 'julianna'

words = ['this', 'is', 'fun']
sentence = ' '.join(words)
print(f'{sentence}.') # 'this is fun.'
```

#### Split Items

Conversely, you can separate a string using `.split('by_char')`, which will parse values out of a string and turn each value into a list item. This one doesn't work for single words you might want to split into individual characters. That said, you *can* specify what character should convey to the method when to split out a new item. By default, `.split('by_char')` will use a space character to split the string.

```python
x = 'this is fun'
sentence = x.split() # note - using default split char at space
print(sentence) # ['this', 'is', 'fun']

y = 'Sandra,hi@email.com,646-212-1234,8 Cherry Lane,Splitsville,FL,58028'
data = y.split(',')
print(data) # ['Sandra', 'hi@email.com', '646-212-1234', '8 Cherry Lane', 'Splitsville', 'FL', '58028']
```

## Built-in Operators for Analyzing Lists

Python has some built-in operations that allow you to analyze the content of a list. Some basic ones include:

**`sum()`**: returns the sum of all items in *numerical lists*.

```python
team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
sum_avgs = sum(team_batting_avgs)
print(f'The total of all the batting averages is {sum_avgs}.')
```
**`min()`** & **`max()`**: return the smallest or largest number *in a numerical list*.

```python
team_batting_avgs = [.299, .208, .301, .275, .328, .226, .253, .232, .287]

print(f'Highest: {max(team_batting_avgs)}') # .328
print(f'Lowest: {min(team_batting_avgs)}') # .208
```

#### `.index()`

Given a list element's value, return its index.

```python
sentence = ['a', 'purple', 'pig', 'and', 'a', 'green', 'donkey', 'flew', 'a', 'kite', 'in', 'the', 'middle','of', 'the', 'night', 'and', 'ended', 'up', 'sunburnt']

pig_index = sentence.index('pig')
print(pig_index)
```

If the element occurs multiple times in the list, `.index()` will only return the index of its *first* occurrence!

```python
sentence = ['a', 'purple', 'pig', 'AND', 'a', 'green', 'donkey', 'flew', 'a', 'kite', 'in', 'the', 'middle','of', 'the', 'night', 'AND', 'ended', 'up', 'sunburnt']

and_index = sentence.index('AND')
print(and_index) # 3
```

#### `.count()`

This returns the number of occurrences of a *single, distinct element* within a list. That means for example, if you're searching a list of words (i.e. strings) for the occurrences of a single letter, only instances where that single letter appears as its own list item will be counted.

```python
nums = [84, 8, 18, 8, 28, 6, 10, 8, 78, 9]
print(nums.count(8)) # 3


sentence = ['a', 'purple', 'pig', 'and', 'a', 'green', 'donkey', 'flew', 'a', 'kite', 'in', 'the', 'middle','of', 'the', 'night', 'and', 'ended', 'up', 'sunburnt']
print(sentence.count('a')) # 3
```

If you want to count the occurrences of a single character within a larger value, you can still use `.count()`...

```python
word = 'sunburnt'
print(word.count('u')) # 2
```

>>**GOTCHA!**
>>`.count()` throws an error if you try to count the number of times the digit "2" appears in the number below. And remember, you CANNOT use the `.split()` method as a workaround because `.split()` only works on strings!

```python
num = 22384232348
print(num.count(2))
```

#### Practice Together!

Now, take a look at how these list operations work together in this contextual example. Let's say we're conducting a probability experiment with coin tosses. We conduct some number of trials (i.e. the coin tosses) and record the outcomes. Based on the sample below, here's one way to find the probabilities of a "Heads" or "Tails" outcome.

```python
coin_toss = [True, False, False, False, True, False, True, True, False, False, True, True, False, True]

```
### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Test your new knowledge with the "List Ops" PSET in your copy of `lists_psets.ipynb` in Google Drive.

## Sorting Lists

If you want to organize your lists better, you can sort them with the `.sort()` or `sorted()` functions. You can sort:

* Numbers: ascending and descending order
* Strings: alphabetically and reverse alphabetically
* You **cannot** sort a list that includes different data types. 

>**GOTCHA!**
>It's important to remember that the `.sort()` method modifies the list *in place*, while the `sorted()` function requires you to assign its result back to the variable.

#### `.sort()`

The first two examples below illustrate how to sort lists in ascending order/alphabetically using `.sort()`.

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5, 6, 7]


letters = ['b', 'e', 'c', 'a', 'd']
letters.sort()
print(letters) # ['a', 'b', 'c', 'd', 'e']
```

To do this in descending order, simply add `reverse=True` as an argument in `.sort()` like this:

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
numbers.sort(reverse = True)
print(numbers) # [7, 6, 5, 4, 3, 2, 1]

letters = ['b', 'e', 'c', 'a', 'd']
letters.sort(reverse = True)
print(letters) # ['e', 'd', 'c', 'b', 'a']
```

#### `sorted()`

The first two examples below illustrate how to sort lists in **ascending order**/alphabetically using `sorted()`.

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
ascending = sorted(numbers)
print(ascending) # [1, 2, 3, 4, 5, 6, 7]


letters = ['b', 'e', 'c', 'a', 'd']
ascending = sorted(letters)
print(ascending) # ['a', 'b', 'c', 'd', 'e']
```

To do this in **descending order**, simply add `reverse=True` as an argument in `sorted()` like this:

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
descending = sorted(numbers, reverse=True)
print(descending) # [7, 6, 5, 4, 3, 2, 1]


letters = ['b', 'e', 'c', 'a', 'd']
descending = sorted(letters, reverse=True)
print(descending) # ['e', 'd', 'c', 'b', 'a']
```
### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Take a shot at the "Sorting" PSET in your copy of `lists_psets.ipynb` in Google Drive.

## Tuples

Tuples are a special subset of lists. They are *immutable* in that they cannot be changed after creation. Tuples are denoted with `()` as opposed to `[]`.

Similar to lists, you can declare tuples with `tuple()` or just `()`. Again, the former can only take one argument, but is useful when you're creating a tuple from an existing list.

```python
x = ['Taq', 100]
score1 = tuple(x)
print(score1) # ('Taq', 100) 

# OR

score2 = ('Randy', 101) # ('Randy', 101)
print(score2)
```
There is also a third way to create a tuple... simply place a comma between two separate values.

```python
score3 = 'Eliza', 102
print(score3) # ('Eliza', 102)
```

We read tuples just like we would read a list:

```python
dna = ('A', 'T'), ('G', 'C')
print(dna) # (('A', 'T'), ('G', 'C'))


print(dna[0]) # ('A', 'T')
print(dna[1][0]) # G
```

You can do SOME operations as long as those operations would not attempt to change the tuple. Since the tuple is immutable, that will throw an error. 

```python
tuple1 = (1, 4, 3, 7, 5, 4, 2, 6)

print(f'''
Length: {len(tuple1)}
Sum: {sum(tuple1)}
Min: {min(tuple1)}
Max: {max(tuple1)}
Occurrences of "4": {tuple1.count(4)}
Index of "2": {tuple1.index(2)}
''')
```
You can also sort, join, or split a tuple the same as a list, **BUT** because you can't edit a tuple:
* You can't use `.sort()` because that edits the object *in place*.
* Each of these will return a *new list object*

#### Sort 

```python
tuple2 = ('b', 'e', 'c', 'a', 'd')

sort_asc = sorted(tuple2)
print(sort_asc, type(sort_asc)) # ['a', 'b', 'c', 'd', 'e'] <class 'list'>

sort_desc = sorted(tuple2, reverse = True)
print(sort_desc, type(sort_desc)) # ['e', 'd', 'c', 'b', 'a'] <class 'list'>
```
#### Join

```python
joined = ', '.join(tuple2) # Joined: b, e, c, a, d <class 'str'>
print('Joined:', joined, type(joined))
```
#### Split

```python
split_up = joined.split(',') # Split: ['b', ' e', ' c', ' a', ' d'] <class 'list'>
print('Split:', split_up, type(split_up))
```

## Sets

Sets are special lists in that they can only have **unique** elements. They are denoted with `{}`.

```python
set_1 = {1,2,3,4,5} # this is a set, notice the {}
set_2 = {1,1,1,2,2,3,4,5,5,5} # this is still a set
print(set_2) # {1,2,3,4,5}

print(set_1 == set_2) # True
```
Sets are NOT indexed, so you cannot access, say, the 3rd element in a set. Instead, you can use *boolean membership operators* to check for a value's existence in the set. Remember those?

```python
set_1 = {1,2,3,4,5}

print(2 in set_1) # True
print(8 in set_1) # False

print(2 and 8 in set_1) # False
print(2 and 3 in set_1) # True
```

That said, you can still perform mathmetical operations on sets. These are the same examples we used for tuples, and they have the same results... EXCEPT you can't find the index of an element for the reasons we just discussed! And as such, you can't count the number of occurrences of an item in a set.

```python
set1 = (1, 4, 3, 7, 5, 4, 2, 6)

print(f'''
Length: {len(set1)}
Sum: {sum(set1)}
Min: {min(set1)}
Max: {max(set1)}
set1.count(4) won't work
set1.index(2) won't work
''')
```

You *can also sort, join, or split* a set, **BUT** you have the same limitations as you do with a tuple:
* You can't use `.sort()` because that edits the object in place
* Each of these will return a *new list object*

#### Sort

```python
set2 = {'b', 'e', 'c', 'a', 'd'}

sort_asc = sorted(set2)
print(sort_asc, type(sort_asc)) # ['a', 'b', 'c', 'd', 'e'] <class 'list'>

sort_desc = sorted(set2, reverse = True)
print(sort_desc, type(sort_desc)) # ['e', 'd', 'c', 'b', 'a'] <class 'list'>
```
#### Join

```python
joined = ', '.join(set2) # Joined: b, e, c, a, d <class 'str'>
print('Joined:', joined, type(joined))
```
#### Split

```python
split_up = joined.split(',') # Split: ['b', ' e', ' c', ' a', ' d'] <class 'list'>
print('Split:', split_up, type(split_up))
```
>**Pro Tip!**
>Sets give a great way to remove duplicates from a list!

```python
my_list = [1,2,4,5,2,3,1,4,5,1,5,3]

uniques_in_my_list = set(my_list)
print(uniques_in_my_list) # {1, 2, 3, 4, 5}

my_list = list(uniques_in_my_list)
print(my_list) # [1, 2, 3, 4, 5]
```

Here's a **[helpful list](https://snakify.org/en/lessons/sets/#section_4)** of other set operations.

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Complete the "List Manipulation" PSET in your copy of `lists_psets.ipynb` in Google Drive. Then, try to solve the "List Challenges" PSET.

## Summary

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/Lists_Summary.png?raw=true" width="100%" align="left"/>

