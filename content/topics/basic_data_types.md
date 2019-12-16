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

**NOTE!**
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
## Simple Operators

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

To print out multiple variables within one `print()` statement...
* We can "add" strings as a way to save or print out multiple variables dynamically
* We CANNOT add strings to non-strings, i.e. `'this will not work' + 4`

```python
a = 'peanut butter'
b = 'jelly'

print(a + b) # 'peanut butterjelly'
print(a + ' and ' + b) # 'peanut butter and jelly'
```
You can also separate variables and strings with commas. Notice how each comma automatically adds a space when you execute the `print()` statementl.

```python
a = 'peanut butter'
b = 'jelly'

print(a, 'and', b) # 'this string and that string'
```

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Complete the "Easy" and "Operators" PSETs in your copy of `basic_data_types_psets.ipynb` in Google Drive.

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
To give you a contextual example, let's say you're running a drug trial at a pharmaceutical company. You have a spreadsheet of the participants and info about them such as their name, age, gender, etc. You also have a field that represents whether or not that participant is on the real drug (True / 1) or a placebo (False / 0). The reason you'd use the 1s and 0s is to allow you to quantify that categorical variable.

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Take a stab at the "Typecasting" PSET in your copy of `basic_data_types_psets.ipynb` in Google Drive.
