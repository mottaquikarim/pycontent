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

>**GOTCHA!**
>If you need to create a tuple that contains only one item, you must define it using `tuple()`.

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

Methods that create a copy of tuple before operating on it will work. HOWEVER, if they're supposed to return a collection of data, they will return a *new **list** object* instead of a new tuple.

```python
tuple2 = ('apple', 'orchard', 'banana', 'cat', 'dance', '8', '6', '6', '3')

# This works
print(', '.join(tuple2))

# This works, but returns a LIST object
print(sorted(tuple2))
```

### Reasons to Use Tuples Instead of Lists

* If a group of values needs to remain constant, using a tuple safeguards against accidental edits.
* As the amount of data increases, using tuples instead of lists optimizes program speed.
* Tuples enable unpacking of individual items.
* Python dictionary objects have a use for tuples (which we'll learn about soon)

## Sets

Sets are another special subtype of lists. Here are some of their notable qualities:

* Sets are denoted with `{}`.
* Sets can only have **unique** elements. 
* Sets are **unordered**, meaning items do not have an index position.
* Sets are mutable, BUT you use different methods to modify them than the methods used with lists.

The most common use for sets is to remove duplicates from a collection of data. Let's define two separate sets. Watch what happens:

```python
set1 = {1,2,3,4,5} # this is a set, notice the {}
set2 = {1,1,1,2,2,3,4,5,5,5} # this is still a set

print(set1 == set2) # True
```

### Modifying Sets

Let's review some common set methods alongside their list method counterparts. 

#### Add a Single Element

Sets use `.add()` instead of `.append()`

```python
# List
x = ['toast', 'mountain', 'atom']
x.append('shiny')
print(x)

# Set
y = {'toast', 'mountain', 'atom'}
y.add('shiny')
print(y)
```

#### Add Multiple Elements

Sets use `.update()` instead of `.extend()`

```python
# List
x = ['toast', 'mountain', 'atom']
x.extend(['shiny', 'crab', 'shell'])
print(x)

# Set
y = {'toast', 'mountain', 'atom'}
y.update(['shiny', 'crab', 'shell'])
print(y)
```

#### Remove a Single Element

Instead of `.pop()`, sets use either `.remove()` or `.discard()`. The latter is preferred because it removes the element *if it exists within the set*. The `.remove()` method will throw an error if you try to remove an element that does not exist in the set.

```python
# List
x = ['toast', 'mountain', 'atom']
x.pop(x.index('toast'))
print(x)

# Set
y = {'toast', 'mountain', 'atom'}
y.discard('toast')
y.discard('shiny')
print(y)
```

#### Other List Methods

You can apply SOME list methods to sets. However, like tuples, these methods will NOT edit the set **in place**. Instead, if they're supposed to return a collection of data, they return a *new **list** object*.

```python
s = {'run', 'jump', 'skip', 'crawl'}

# This works
print(', '.join(s))

# This works, but returns a LIST object
print(sorted(s))
```

### Set Theory

Sets are of course also useful for **[set theory](https://en.wikipedia.org/wiki/Set_theory)** purposes. At its simplest, "set theory" is concerned with examining and comparing collections of items. 

For this class, we'll only discuss the 3 most basic and common use cases of set theory with Python. set membership. 

#### Membership: "Are these values in the data already?"

Because sets are not indexed, you cannot access a specific element. The most you can do is check for Simple and common a value's existence in the set using a boolean membership operator.

```python
set1 = {1,2,3,4,5}

print(2 in set1) # True
print(8 in set1) # False
```

Unfortunately, you CANNOT use operators if you want to check the membership of multiple elements at the same time. For that you can use `smaller.issubset(larger)`. Note that it will only evaluate to `True` if ALL elements in the smaller set are contained in the larger set.

```python
set1 = {1,2,3,4,5}
set2 = {2, 8}
set3 = {2, 3}


print(set2.issubset(set1)) # False
print(set3.issubset(set1)) # True
```

#### Union: "I want to combine these two data collections without adding duplicates."

A **union** combines all the elements of two sets, but excludes adding duplicate values. The syntax used is `a.union(b)`.

```python
colors1 = {'yellow', 'violet', 'green', 'orange'}
colors2 = {'yellow', 'violet', 'indigo', 'red'}

rainbow = colors1.union(colors2)
print(rainbow)
```

#### Intersection: "What elements exist in both collections of data?"

An **intersection** returns ONLY the elements that exist in both groups. The Python syntax used is `a.intersection(b)`.

```python
colors1 = {'yellow', 'violet', 'green', 'orange'}
colors2 = {'yellow', 'violet', 'indigo', 'red'}

rainbow = colors1.intersection(colors2)
print(rainbow)
```

#### More Set Theory with Python

If you're interested in delving further into set theory, you can find a helpful list of set theory operators and methods **[here](https://snakify.org/en/lessons/sets/#section_4)**.

## Key Takeaways

* Tuples and sets are special subtypes of lists.
* Tuples are...
    * denoted with `()`
    * ordered and accessible via index positions
    * *immutable*
* Tuples can be packed `t1 = 'a', 'b'` and unpacked `t2, t3 = ('a', 'b')` 
* Sets are...
    * denoted with {}
    * unordered, meaning items do not have an index position
    * mutable
* Sets can only have unique elements
* Sets use different methods to modify them than the methods used with lists 
    * `.add()` instead of `.append()`
    * `.update()` instead of `.extend()`
    * `.discard()` instead of `.pop()`
* Simple set theory methods work as follows:
    * `in` and `not in` check the membership status of a single value
    * `.issubset()` checks the membership status of a collection of values
    * `.intersection()` returns the elements that exist in BOTH sets
    * `.union()` combines both sets (of course eliminating duplicates)




