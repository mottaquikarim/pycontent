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
try:
	colors = list('red', 'yellow', 'green')
except TypeError as t:
	print(f'{t.__class__.__name__}: {t}')
	# TypeError: list() takes at most 1 argument (3 given)
```
Even if you do pass only *one* item, you still have to enclose it with `[]`. If you pass a single number or a single boolean without using brackets, you'll get a `TypeError`.

```python
try:
	colors = list('red', 'yellow', 'green')
except TypeError as t:
	print(f'{t.__class__.__name__}: {t}')
	# TypeError: list() takes at most 1 argument (3 given)

try:
	y = list(True)
except TypeError as t:
	print(f'{t.__class__.__name__}: {t}')
	# TypeError: list() takes at most 1 argument (3 given)
```

If you pass a string without using brackets, you won't get quite what you want.

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

|  List | 'snickerdoodles' | 'shortbread' | 'oatmeal raisin' | 'gingersnaps' | 'macarons' |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |


To access one of them use the syntax `list_name[index_position]`.

```python
cookies = ['snickerdoodles', 'shortbread', 'oatmeal raisin', 'gingersnaps', 'macarons']
print(cookies[0]) # snickerdoodles
print(cookies[1]) # shortbread
print(cookies[4]) # macarons
```

What if you want to grab a single element from a list nested within a list though? Simply add another level of index selection.

```python
nested_lists = list([['circus', 'clown'], ['trapeze', 'artist']])
print(nested_lists[0][0]) # circus
print(nested_lists[1][0]) # trapeze
```

The `len()` function will give you the total number of list elements (regardless of data type).

```python
cookies = ['snickerdoodles', 'shortbread', 'oatmeal raisin', 'gingersnaps', 'macarons']
types_of_cookies = len(cookies)
print(types_of_cookies) # 5
```

>>**REMEMBER!** 
>>Because the index starts at 0, the index position of the last item in the list will NOT be equal to the list's length.

If you pass in any list index greater than or equal to the length of the list, you will get an `IndexError`:

```python
print(cookies[types_of_cookies])
### IndexError: list index out of range
```

Aside from merely finding the length, `len()` comes in handy if you need to dynamically select the last element of a list. Logically, the length of the list minus 1 will give you the index of the last list element, i.e. `index_of_last_element = len(list_name) - 1`.

```python
cookies = ['snickerdoodles', 'shortbread', 'oatmeal raisin', 'gingersnaps', 'macarons']
types_of_cookies = len(cookies)

# (types_of_cookies - 1) is the index of the last element
print(cookies[types_of_cookies - 1]) # macarons
```

That brings us to something called **negative indexing**. Because of the above rule, Python allows you to take this shortcut to access the last list element:

```python
print(cookies[-1])
```

Likewise, as you count backwards from the last list element, the negative index extends...

```python
print(f'2nd to last item is {cookies[-2]}')
print(f'3rd to last item is {cookies[-3]}')
```

### Selecting Ranges

To select multiple items from a list, simply pass the range of indeces which hold the desired elements, e.g. `my_list[2:7]`. It's important to remember that **the upper bound is NOT inclusive**. In other words, if you want the elements at index 3 and index 4, you have to write `[3:5]`. (Likewise, `my_list[1:1]` would print nothing.) 

```python
cookies = ['snickerdoodle', 'chocolate chip', 'shortbread', 'oatmeal raisin', 'gingerbread', 'pizelle', 'macarons', 'gingersnaps']
print(cookies[3:5])
```

Ommitting one or both bounds acts as a shortcut when the length and order of your list might vary. It allows you to say, "Give me everything from the beginning of the list to index `x`" or "Give me everything from index `x` and onward."

```python
cookies = ['snickerdoodle', 'chocolate chip', 'shortbread', 'oatmeal raisin', 'gingerbread', 'pizelle', 'macarons', 'gingersnaps']

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

#### `.append()` vs. `.extend()`

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

In the next example, take a look at how `.extend()` only considers individual values of the *parent list* passed in. It still adds the nested lists - `['f', 'g']` and `['h', 'i']` - to our list `x` as their own items.

```python
x = ['a', 'b', 'c', 'd']
y = ['e', ['f', 'g'], ['h', 'i'], 'j']
x.extend(y)
print(x)
# ['a', 'b', 'c', 'd', 'e', ['f', 'g'], ['h', 'i'], 'j']
```

#### `.insert(index, value)`

If you want to add an item to a specific point in your list, you can pass the desired index and value into `.insert()` as follows.

```python
pies = ['apple', 'pumpkin', 'pecan', 'blueberry']
pies.insert(1, 'key lime')
print(pies)
```

Whatever you pass into the `value` parameter will be added as a single element though!

```python
pies = ['apple', 'pumpkin', 'pecan', 'blueberry']
pies.insert(1, ['lemon meringue', 'strawberry peach'])
print(pies)
```

### Remove Items from a List

Likewise, you can use `.pop()` or `.pop(index)` to remove any type of element from a list.

#### `.pop()`
- Removes an item from the end of the list.

```python
pies = ['cherry', 'lemon meringue', 'pecan', 'key lime', 'blackberry', 'strawberry peach', 'blueberry']
eaten = pies.pop()
print(f'The {eaten} pie got eaten.')
print(pies)
```

#### `.pop(index)`

- Removes an item from the list.
- Can take an index.

```python
pies = ['cherry', 'lemon meringue', 'pecan', 'key lime', 'blackberry', 'strawberry peach']
eaten = pies.pop(2) # Remember to count from 0!
print(f'The {eaten} pie got eaten.')
```

### Copying Lists

You can create a copy of a list simply by declaring a new variable and setting it equal to the existing list, as seen with `pies2` below. In contrast, you can create a *deep copy*, one that doesn't point back to the original, using `[:]` as seen with `pies3` below.

```python
pies1 = ['strawberry', 'cherry', 'blackberry', 'blueberry']
pies2 = pies1
pies3 = pies1[:]

print(f'''
pies1: {pies1}
pies2: {pies2}
pies3: {pies3}
''')
```

Let's look at the difference in action. With the first method, you're saying that `pies2` points to the place in memory where `pies1` is stored. That means if you edit `pies2`, you're effectively editing `pies1` along with it.

```python
pies1 = ['strawberry', 'cherry', 'blackberry', 'blueberry']
pies2 = pies1

print(f'''
BEFORE:
pies1: {pies1}
pies2: {pies2}
''')

pies2.pop()

print(f'''
AFTER pies2.pop():
pies1: {pies1}
pies2: {pies2}
''')
```

A deep copy creates a *separate instance* of the list in the program's memory so that the two are not tied together at all. Editing a deep copy like `pies3` will NOT alter `pies1`.

```python
pies1 = ['strawberry', 'cherry', 'blackberry', 'blueberry']
pies3 = pies1[:]

print(f'''
BEFORE:
pies1: {pies1}
pies2: {pies3}
''')

pies3.pop()

print(f'''
AFTER pies3.pop():
pies1: {pies1}
pies3: {pies3}
''')
```

### Update/Replace Items in a List

To replace items in a list, you reference them by their index position and simply declare a new value. The general syntax is `my_list[<index>] = <value>`. 

```python
pies = ['apple', 'pumpkin', 'pecan', 'blueberry']
pies[0] = 'banana cream'
print(pies)
```

Let's say you specify one index position and pass a group of elements like the below. That group *as a whole* replaces the element at the specified index position.

```python
pies = ['banana cream', 'pumpkin', 'pecan', 'blueberry']
pies[1] = ['key lime', 'lemon meringue']
print(pies)
```

If you specify a range of index positions, each item in the group gets added individually (sort of like `.extend()`). Here are a few examples...

* This replaces everything from index position 1 onward with the three new elements passed.

```python
pies = ['strawberry', 'banana cream', 'key lime']
pies[1:] = ['blueberry', 'cherry', 'blackberry']
print(pies)
# ['strawberry', 'blueberry', 'cherry', 'blackberry']
```

* This replaces every element up to, but NOT including index position 2 with the three new elements passed. Notice how the *three* new elements replaced only *two* existing elements.

```python
pies = ['strawberry', 'blueberry', 'cherry', 'blackberry']
pies[:2] = ['apple', 'pumpkin', 'pecan']
print(pies)
# ['apple', 'pumpkin', 'pecan', 'cherry', 'blackberry']
```

* Even if you pass one new element, it must be in `list` format. Otherwise, Python will try to break it up into a list like the below...

```python
pies1 = ['strawberry', 'banana cream', 'key lime', 'apple', 'pumpkin']
pies2 = pies1[:]

pies1[1:3] = ['blueberry']
pies2[1:3] = 'blueberry'
print(pies1) # ['strawberry', 'blueberry', 'apple', 'pumpkin']
print(pies2) # ['strawberry', 'b', 'l', 'u', 'e', 'b', 'e', 'r', 'r', 'y','apple', 'pumpkin']
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

Conversely, you can separate a string using `.split(<by_char>)`, which will parse values out of a string and turn each value into a list item. This one doesn't work for single words you might want to split into individual characters. That said, you *can* specify what character should convey to the method when to split out a new item. By default, `.split(<by_char>)` will use a space character to split the string.

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


## Key Takeaways

* Pass comma-separated values within `[]` to create a list object
* An element's *index position* refers to its numerical place in the list. The index always starts at 0, i.e. the first element of the list is at index position 0.
* Access a list elements based on its index position using the syntax `my_list[<index>]`
* `len()` will return the length of the list
* `.append()` adds an element to the end of a list
	* If you pass a group of elements to `.append()`, they get added as a *single* element.
* To elements from a group to a list individually, pass the group to `.extend()`
* `.pop()` removes the last item from the list
	* Pass an index position into `.pop()` to remove a specific element
* `my_list[idx] = new_value` updates an element at a specific index position
* To create a deep, or completely separate, copy, use `my_list[:]`
* For numerical lists...
	* Use `sum()` to find the total of all the numbers in the list
	* Use `max()` and `min()` to return the highest and lowest numbers in the list respectively 
* `.index()` returns the index position of a specific item in the list
* `.count()` returns the number of occurrences of some item within a list
* `.join()` compile your list items into a single string
* `.split(<by_char>)` will split a string at each occurence of <char> and group those items in a list
* `.sort()` or `sorted()` will sort a list in ascending order
	* Pass `reverse = True` to either one to sort the list in descending order