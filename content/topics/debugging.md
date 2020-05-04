<img src="https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png"/>

# Debugging Principles and Techniques

## Lesson Objectives

This lesson will introduce simple methods for investigating issues in your code. At this point, it's not so much about being able to analyze complex problems as about becoming aware of and familiar with common error messages and their meanings. After this lesson, you will be able to...

* Troubleshoot common types of errors.
* Implement basic exception mitigation.

## Making Errors Into Friends

On the surface, errors are frustrating! However, Python errors are usually very helpful and have clear messages. You'll see that:

* Errors sometimes say exactly what's wrong.
* Errors often point out the line number where the error occurred.
* Some errors have very common causes.
* Errors may say exactly how to fix the issue.

With that in mind, what's the problem with this code?

<img src="https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/ZeroDivisionError.png" width="750px"/>

## List of Common Errors

This chart's for you to refer to later - don't memorize it now!

| Error Type  | Most Common Cause |
| ----------- | ------------------|
| `AttributeError` | Attempting to access a non-existent attribute |
| `KeyError` | Attempting to access a non-existent key in a dict |
| `ImportError` | A module you tried to import doesn't exist |
| `IndexError` | Accessing a list element that doesn't exist |
| `IndentationError` | Indenting code in an invalid way |
| `IOError` | Accessing a file that doesn't exist |
| `NameError` | Attempting to use a module you haven't imported/installed or a variable you haven't created |
| `OverflowError` | You made a number larger than the maximum size |
| `RuntimeError` | Python can't categorize the issue into any other error type. |
| `SyntaxError` | A typo or mistake in adhering to the linguistic syntax of Python |
| `TypeError` | Combining or comparing two different date types in an incompatiable manner |
| `ValueError` | When a function receives an argument of the correct type, but an invalid value |
| `ZeroDivisionError` | Dividing By Zero |

## Error Examples

Copy these example into [Repl.it](https://repl.it/) to run the code and see the error messages for yourself.

### IndexError

**Cause**: Index errors typically happen when you attempt to access a list index that doesn't exist.

```python
race_runners = ["Yuna", "Bill", "Hyun"]

first_place = race_runners[1]
second_place = race_runners[2]
third_place = race_runners[3]

print("The winners are:", first_place, second_place, third_place)
```

### NameError

**Cause**: Attempting to use a module you haven't imported/installed or a variable you haven't created

```python
# Get a number between 2 and 8.
my_nums = 5

# Print the number
print(my_num)
```

### KeyError

**Cause**: Accessing a key in a dictionary that doesn't exist. The error message tells you exactly what key is missing!

Reasons for this could include:

* A misspelling.
* Mixing uppercase and lowercase.
* Forgetting what keys exist

```python
my_favorites = {
  "Food": "Lobster Rolls",
  "Song": "Bohemian Rhapsody",
  "Flower": "Iris",
  "Band": "Tom Petty & the Heartbreakers",
  "Color": "Green",
  "Movie": "The Princess Bride",
  "Programming Language": "Python"
}

# This is okay!
print("My favorite color is", my_favorites["Color"])

# This is NOT okay! (Case sensitivity!)
print("My favorite color is", my_favorites["color"])

# This is NOT okay! (Key doesn't exist)
print("My favorite restaurant is", my_favorites["Restaurant"])
```

### AttributeError

**Cause**: Accessing an attribute that doesn't exist for some object class

```python
class Dog():
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("Bark!")

# Declare a new dog instance
my_dog = Dog("Fido")

# Call the bark method
my_dog.bark() # OK!

# Call the run method
my_dog.run() # AttributeError!
```

### SyntaxError

**Cause**: A typo or mistake in adhering to the linguistic syntax of Python

```python
my_age = 13

if my_age = 18:
    print("I may vote.")
else:
    print("I may not vote.")
```

### TypeError

**Cause**: Combining or comparing two different date types in an incompatiable manner

```python
my_num = 5 + "10"
print(my_num)
```

### IndentationError

**Causes**:

 * Missing indents
 * Mismatched indentation
 * Mixing tabs and spaces

```python
my_age = 13

if my_age == 16:
  print("I may drive.")
else:
print("I may not drive.")
```

### ValueError

**Cause**: When a function receives an argument of the correct type, but an invalid value

This is *most commonly* caused by trying to convert a string into a number.

```python
# This is okay!
my_num = int("10")

# This throws a ValueError
my_num = int("Moose")
```

## Anticipating Errors with Try/Except

Sometimes, we have code that we expect might throw an error. For example, what happens in the below code if a user types in "43F" to signify Fahrenheit?

```python
temp = input('What temperature is it outside? ')

if int(temp) < 65:
    print('wear a jacket!')
```

That would cause a `ValueError` because it's trying to convert a string to an integer. Because we know this is a possibility, we COULD add some conditions to handle asking the user for valid input.

```python
temp = input('What temperature is it outside? ')

if type(temp) == int or type(temp) == float:
    if temp < 65:
        print('wear a jacket!')
else:
    print('Please enter a numeric value for the temperature.')
```

However, this could get out of hand when there are a multitude of scenarios that could cause a potential error. A **Try/Except statement** is a more elegant method for handling common errors. It's syntactically similar to a conditional statement. It also has similar control flow. Just like the `else` in an if/else block, `except` only runs if Python encounters a problem in the `try` code block.

<img src="https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/try_except.png" width="500px"/>

Below is the most general version of a try/except block. It will catch any error.

```python
temp = input('What temperature is it outside? ')

try:
    if int(temp) < 65:
        print('wear a jacket!')
except:
    print(f"Something went wrong!")
```

However, it doesn't capture any details about the issue. That's why it's better to add `Exception as <some_variable>`. You can then access the value and attributes of that variable to get more information about the error. In the below, we call this variable `e`. Simply printing out `e` displays a brief error message. Use `e.__class__.__name__` to print the name of the error.

```python
temp = input('What temperature is it outside? ')

try:
    if int(temp) < 65:
        print('wear a jacket!')
except Exception as e:
    print(f'''{e.__class__.__name__}: {e}''')
    print('Please enter a valid number.')
```

Again, the above is general in that it captures any type of error. If you know the type of error you're anticipating though, it's best to specify that in the code to let others know your thought process.

```python
temp = input('What temperature is it outside? ')

try:
    if int(temp) < 65:
        print('wear a jacket!')
except ValueError as ve:
    print(f'''{ve.__class__.__name__}: {ve}''')
    print('Please enter a valid number.')
```

## Key Takeaways

* Python has many built-in errors. Some of the **most** common are keep in mind are TypeErrors, ValueErrors, KeyErrors, IndexErrors, AttributeErrors, and SyntaxErrors.
* Use `try`/`except` syntax to catch an expected error.
* Logic issues don't throw errors, so be careful!

## Additional Resources

* [Built-In Exception Docs](https://docs.python.org/3/library/exceptions.html)
* [Error Flowchart PDF](https://www.dropbox.com/s/cqsxfws52gulkyx/drawing.pdf)
* [Raising Exceptions](https://realpython.com/python-exceptions/)
* [A deep dive into try/except clauses](https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
* To get advanced, add [logging](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/) to your code.
* To get very advanced, include [unit tests](http://www.diveintopython.net/unit_testing/index.html)
* The [pytest module](http://pythontesting.net/framework/pytest/pytest-introduction/) is great for unit testing.
