# Basic Data Types

## Variables & Primitive Data Types

### Creating & Reading Variables

In all programming languages, developers leverage **variables** to store and retrieve units of information. Each language categorizes these pieces of data...hence the term **data types**. Because variables are so ubiquitous, there are some **rules for naming variables** that help avoid confusion.

* **Rule:** snake_case with the underscore character
* **Rule:** Can’t use keywords as var names, e.g. True, None, function, class, object
* **Rule:** Can’t start with a numeric value, e.g. can't name something "1var", but you CAN do function1
* **Best Practice:** You COULD use CamelCase to name a variable, but this is typically reserved for naming a different Python object called a "class".

As seen below, once you create your variable, you can display the value stored in a variable on the screen using the `print()` statement. 

```python
first_prime = 2
print(first_prime) # expect to see 2
```
>>**Pro tip!** Let's quickly look at how to write **comments** in the code. Documenting notes with comments is extremely useful, especially when multiple people are working on a project.

```python
# I'm a comment!

"""
I'm a
multi-line
comment
"""
```
### Primitive Data Types

The following list defines Python's "primitive" data types. In other words, these are the building blocks, which compose the more complex data types we'll learn about later.

* **Strings**: alphanumeric characters read as text
* **Integers**: whole numbers
* **Floats**: decimals
* **Booleans**: represents True or False values; used for evaluating conditional statements
* **Nonetype**: represents variables not yet defined or essentially blank values (shown as None, used as a placeholder to avoid errors)

```python
# Strings
cat = 'Layla' # or "Layla" because single & double quotes are both valid

# Integers
age = 8

# Floats
weight = 10.5

# Booleans
vaccinated = True
good_with_other_cats = False

# Nonetype
good_with_other_dogs = None
```

## String Formatting

A string can be any combination of alphanumeric characters of any length. The below are all examples of strings. Notice how putting quotes around other data types turns them into strings.

```python
cat = 'Layla' # a single word
colors = 'white and orange' # a phrase or sentence

age = '8'
weight = '10.5'

vaccinated = 'True'
good_with_other_cats = 'False'

good_with_other_dogs = 'None'
```
Because the content of a string can vary so much, Python has several features that make handling them much easier...

### Escape Characters

Python has defined certain **escape characters** that will NOT be read literally when placed inside a string. Instead, they tell Python to insert a character in a special way. For example, since strings can be enclosed by single or double quotes, what happens when you need to use one of those within the string? Python will get confused as to where you want your string to start and end! That's where the `\'` and `\"` escape characters come in.

```python
demeanor = 'Layla\'s mischievous, but very sweet!'
print(demeanor)


sound = "Layla says \"Meow\"!"
print(sound)
```

The `\n` escape character tells Python to start a new line before displaying the rest of the string. 

```python
print('Layla:\nMaine Coon\n8 years old\n10.5 lb')
```

### String Formatting with f-Strings

Python supports a feature called **f-strings** that enables dynamic formatting of strings. By placing "f" before a string, it notifies Python to interpret the string dynamically based on the rules and syntax of f-string formatting. Without the "f", Python will interpret the string literally. Here are some of the most common use cases:

#### Multi-Line Strings

Using `\n` will let you tell Python to split your string into multiple lines when printed. Using an f-string makes the text more readable within your code as well. For a multi-line f-string, you need to enclose your string in triple `'''` or `"""`. Let's say you're storing song lyrics, so you want to have a line break between each line of the song. 

```python
print('Cause if you liked it, then you should have put a ring on it\nIf you liked it, then you should have put a ring on it\nDon\'t be mad once you see that he want it\nIf you liked it, then you should have put a ring on it')

print(f'''
'Cause if you liked it, then you should have put a ring on it
If you liked it, then you should have put a ring on it
Don't be mad once you see that he want it
If you liked it, then you should have put a ring on it
''')
```

>**Remember!**
> If you use triples quotes *without* the "f", you're creating a multi-line *comment*, which won't print out.


#### Insert Variables in a String

If you want to insert variables within a string, you can separate string snippets with commas. Note that the commas will not be printed, but also that each comma automatically adds a space before the next item.

```python
a = 5
b = 12
c = 'pomegranate'

print(a, '+', b, '= 17') # 5 + 12 = 17
print('I\'d like a', c, '.') # I'd like a pomegranate .
```
But that can get annoying when you're inserting multiple variables. It can also end up printing out spaces where you don't want them (e.g. between `pomegranate` and `.` To simplify this with an f-string, you can add variables directly into a string within `{}`. Remember that if you don't add the "f" before the opening quote, it will interpret the string content literally!

```python
a = 5
b = 12
c = 'pomegranate'

print(f'{a} + {b} = 17') # 5 + 12 = 17
print('{a} + {b} = 17') # {a} + {b} = 17


print(f'I\'d like a {c}.') # I'd like a pomegranate.
print('I\'d like a {c}.') # I'd like a {c}.
```

You can insert as many variables as you want than one variable

####    Manipulate Variables Directly in a String

You can even do simple operations on variables within the `{}` such as math, functions, and methods. (More on the latter two to come!

```python
a = 5
b = 12
c = pomegranate

# MATH
print(f'{a} + {b} = {a + b}') # 5 + 12 = 17
print(f'{b % a}') # 2

# FUNCTION
print(f'{len(c)}') # 11

# METHOD
print(f'{c.upper()}') # POMEGRANATE
```

>**Bonus Topic**: You can use several versions of the the `.strip()` function to remove leading and trailing spaces from strings.
>* `.lstrip()`: remove all leading AND trailing spaces
>* `.rstrip()`: remove all leading AND trailing spaces
>* `.strip()`: remove all leading AND trailing spaces

```python
a = '    hi mom!'
print(f'LEADING SPACES: \n{a} \n{a.strip()}\n\n')


b = 'hi mom!    '
print(f'TRAILING SPACES: \n{b} \n{c.strip()}\n\n')


c = '    hi mom!    '
# print(c, '\n', c.strip(), '\n\n')
print(f'LEADING & TRAILING SPACES: \n{c} \n{c.strip()}')
```

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Complete the "Easy" PSET in your copy of `basic_data_types_psets.ipynb` in Google Drive.

## Typecasting

### `type()`

Check what data type is stored in a variable using the `type()` statement or the `isinstance()` statement.

```python
# Example 1 - type()
a = 1
print(type(a)) # <class 'int'>

b = '2.5'
print(type(b)) #  

# Example 2 - isinstance()
c = -1
print(f'Is {c} a boolean?', isinstance(c, bool)) # False

d = False
print(f'Is {d} a boolean?', isinstance(d, bool)) # True
```

### Convert Values Into Different Data Types

**Typecasting** is a way to convert an instance of one data type to another. Numbers are the most flexible for converting, while strings are very inflexible. Booleans get a bit more complicated, so we'll look at those last!

#### Converting Numbers

```python
"""INTEGERS"""
int_to_float = float(10) # 10.0, <class 'float'>
int_to_string = str(10) # 10, <class 'str'>

"""FLOATS"""
float_to_int = int(2.5) # 2, <class 'float'>
# Notice it does NOT ROUND!
float_to_string = str(2.5) # '2.5', <class 'str'>
```

#### Converting Strings

```python
string_to_int = int('mango') # ERROR!
string_to_float = str('strawberry') # ERROR!
```

#### Converting Booleans

Typecasting between strings and booleans is relatively simple.

```python
t = str(True) # 'True'
f = str(False) # 'False'

str_to_True_bool = bool('peach') # True (<class 'bool'>)
```
The **ONLY** way a *string* converted into a boolean will be False is if it's **empty** (as seen above). Spaces count as characters even though they wouldn't display anything if printed. We can prove this by finding the length of a string that only contains spaces.

```python
empty = ''
print(bool(empty), len(empty)) # False (<class 'bool'>), 0

spaces = '     '
print(bool(spaces), len(spaces)) # True (<class 'bool'>), 5
```

Typecasting numbers to and from boolean values is a little more nuanced. A `False` boolean is always associated with `0` or `0.0`.

```python
int_to_boolean = bool(0) # False (<class 'bool'>)
float_to_boolean = bool(0.0) # False (<class 'bool'>)


false_to_int = int(False) # 0
false_to_float = float(False) # 0.0
```
However, while you can convert any number to a True boolean, a True boolean will only ever become 1 or 1.0. 

```python
int_to_boolean = bool(10) # True (<class 'bool'>)
float_to_boolean = bool(2.5) # True (<class 'bool'>)


true_to_int = int(True) # 1
true_to_float = float(True) # 1.0
```

To give you a contextual example, let's say you're running a drug trial at a pharmaceutical company. You have a spreadsheet of the participants and info about them such as their name, age, gender, etc. You also have a field that represents whether or not that participant is on the real drug (True / 1) or a placebo (False / 0). The reason you'd use the 1s and 0s is to allow you to quantify that categorical variable.\

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Take a stab at the "Typecasting" PSET in your copy of `basic_data_types_psets.ipynb` in Google Drive.

## Simple Integer, Float, & String Operators

**Operators** are shortcuts for manipulating values stored in variables.

### Integer/Float Operators

We can operate on integers/floats in the following ways:

* Addition
* Subtraction
* Multiplication
* Division
* Modulus (This one divides and returns **only the remainder**.)

```python
orig_num = 10

# Addition
num1 = orig_num + 5 # 15

# Subtraction
num2 = orig_num - 5 # 5

# Multiplication
num3 = orig_num * 5 # 50

# Division
num4 = orig_num / 5 # 2

# Modulus
num5 = orig_num % 5 # 0
num6 = orig_num % 3 # 1
```

### String Operators

* We can "add" strings
* We CANNOT add strings to non strings

```python
a = 'this string'
b = 'that string'

print(a + b) # 'this stringthat string'


print(a + ' and ' + b) # 'this string and that string'
print(a, 'and', b) # 'this string and that string'


"""ERROR!!!
print('this will not work' + 4) doesn't work 
because you can't add a number to a string"""
```

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Complete the "Operators" PSET in your copy of `basic_data_types_psets.ipynb` in Google Drive.


## Additional Resources

* [A Repl.it Summarizing Print Statements](https://repl.it/@brandiw/Python-01-Variables-4?lite=true)
* [Python For Beginners](http://www.pythonforbeginners.com/basics/python-variables)
* [Python Programming Tutorial: Variables](https://www.youtube.com/watch?v=vKqVnr0BEJQ)
* [Variables in Python](https://www.guru99.com/variables-in-python.html)
* [Operators Cheatsheet](http://python-reference.readthedocs.io/en/latest/docs/operators/)
* [Python Style Guide: Naming](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)
* [Python-Strings](https://www.tutorialspoint.com/python/python_strings.htm)
* [String Concatenation and Formatting](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
* [String Concatenation and Formatting - Video](https://www.youtube.com/watch?v=jA5LW3bR0Us)
