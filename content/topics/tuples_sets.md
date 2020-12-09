# Tuples & Sets

## Objective

Learn the properties of tuples and sets, which are special subsets of lists.

## Tuples

Tuples are a special subset of lists. Tuples are *immutable* in that they cannot be changed after creation. Tuples are denoted with `()` as opposed to `[]`.

Similar to lists, you can declare tuples with `tuple()` or just `()`. Again, the former can only take one argument, but is useful when you're creating a tuple from an existing list.

```python
x = ['Taq', 100]
score1 = tuple(x)
print(score1) # ('Taq', 100) 

# OR

score2 = ('Randy', 101) # ('Randy', 101)
print(score2)
```

>>**GOTCHA!**
>>If you need to create a tuple that contains only one item, you must define it using `tuple()`.

```python
# Wrong
t = (True)
print(type(t))

# Right
t = tuple([True])
print(type(t))
```

Also, we read and index slice tuples just like we would a list:

```python
dna = ('A', 'T'), ('G', 'C')
print(dna) # (('A', 'T'), ('G', 'C'))


print(dna[0]) # ('A', 'T')
print(dna[1][0]) # G
```

### Tuple Packing & Unpacking

There is also a third way to create a tuple... simply place a comma between two separate values. This is called **packing**.

```python
name = 'Eliza'
score = 102
eliza_score = 'Eliza', 102
print(eliza_score) # ('Eliza', 102)
```

Similarly, you can **unpack** tuples, which means assigning each value in a tuple to its own variable. Remember that the number of variables on the left must be equal to the number of items in the tuple for this to work. Otherwise, it will throw an error!

```python
# Pack
eliza_score = 'Eliza', 102
print(eliza_score) # ('Eliza', 102)

# Unpack
name, score = eliza_score
print(name, score) # Eliza 102
```

### Tuple Methods

MOST list methods can be used on tuples, *so long as they do not attempt to change the tuple **in place**.* Since the tuple is immutable, that will throw an error.

```python
tuple1 = ('apple', 'orchard', 'banana', 'cat', 'dance', '8', '6', '6', '3')

# This won't work
try:
    tuple1.extend(['toast', 'mountain', 'atom'])
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
```

Methods that create a copy of tuple before operating on it will work, BUT they will return a *new **list** object*. 

```python
tuple2 = ('apple', 'orchard', 'banana', 'cat', 'dance', '8', '6', '6', '3')

# This works
print(f'''
Sorted: {sorted(tuple2)}
Joined: {', '.join(tuple2)}
etc...
''')
```

### Reasons to Use Tuples Instead of Lists

* If a group of values needs to remain constant, using a tuple safeguards against accidental edits.
* As the amount of data increases, using tuples instead of lists optimizes program speed.
* Tuples enable unpacking of individual items.
* Python dictionary objects have a use for tuples (which we'll learn about soon)

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