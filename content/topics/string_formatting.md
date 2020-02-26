# String Formatting

Because the content of a string can vary so much, Python has several features that make handling them much easier. In this section, we'll learn about:

* Escape Characters
* f-Strings
* Stripping Extra Spaces
* User Input

## Escape Characters

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

## f-Strings

Python supports a feature called **f-strings** that enables dynamic formatting of strings. By placing "f" before a string, it notifies Python to interpret the string dynamically based on the rules and syntax of f-string formatting. Without the "f", Python will interpret the string literally. Here are some of the most common use cases:

### Multi-Line Strings

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

#### Manipulate Variables Directly in a String

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

## Stripping Extra Spaces

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

## User Input

As a bonus topic, let's discuss how to collect input from the user while running your program. It's quite simple - declare a variable equal to the `input()` function. Your program will stop when it reaches that function and wait for user input. You can (and probably should) add a string within the `input()` function. This will act as a written prompt for the user. Let's see this in action:

```python
answer = input('What is your name? ')
print(answer)
```
One vital thing to remember is that *the `input()` function will always typecast the user's input into a string.* This can be problematic:

```python
subtotal = 48.37
tip = input('Please enter the amount of tip you want to leave: ')
total = subtotal + tip # TypeError
```
To remedy this, you have to remember to typecast the user's input into whatever data type you ultimately need.

```python
subtotal = 48.37
tip = float(input('Please enter the amount of tip you want to leave: '))
total = subtotal + tip 
print(f'{total:.2f}')
```

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Complete the "Shopping List" PSET in your copy of `basic_data_types_psets.ipynb` in Google Drive.

