# Exceptions Handling

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

## Key Takeaways

* Python has many built-in errors. Some of the **most** common are keep in mind are TypeErrors, ValueErrors, KeyErrors, IndexErrors, AttributeErrors, and SyntaxErrors.
* Use `try`/`except` syntax to catch an expected error.
* Logic issues don't throw errors, so be careful!

### logging

```python
try:
    x = int('foo')
except Exception as e:
    logging.exception('Caught an error')
```

### `raise`

reraise an exception: means the caller of the function has to do own try/except

when you reraise, you must put the function CALL into a try/except

`raise Exception()` is most general if don't want to create custom exception

```python
class MyCustomException(Exception):
    pass

def squares(n):
    try:
        n = float(n)
    except Exception as e:
        # if you ALSO want to log the exception...
        # logging.exception(f'{e.__class__.__name__}: {e}')
        raise MyCustomException(f'{e.__class__.__name__}: {e}')
        """
        don't need to return anything when you re-raise bc the function caller's 
        except clause will handle what should happen if the function can't generate 
        valid output
        """

    sq = n**2
    sqrt = n**0.5

    return sq, sqrt

# error case 1: TypeError
try:
    x, y = squares([4.5])
    print(f'square: {x}, square root: {y}')
except Exception as e:
    print(f'{e}') 
```

^^ `e` is everything in the raised exception here, not just the exception message. see below variation to prove this.

```python
def squares(n):
    n = float(n)
    sq = n**2
    sqrt = n**0.5
    return sq, sqrt

# error case 1: TypeError
try:
    x, y = squares([4.5])
    print(f'square: {x}, square root: {y}')
except Exception as e:
    print(f'{e}')
```

#### Multiple Excepts

```python
class MyCustomException(Exception):
    pass


def rand_list2(how_many, start, end):
    try:
        how_many = int(how_many)
        start = int(start)
        end = int(end)
        return choices(range(start, end+1), k=how_many)
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}') 
        raise MyCustomException(f"Failed to generate random list: {e}")

try:
    y = rand_list2(10, 15, 12) 
    print(y)
except MyCustomException as e:
    print(f"handle this error in user space {e}")
```



## Additional Resources

* [Built-In Exception Docs](https://docs.python.org/3/library/exceptions.html)
* [Error Flowchart PDF](https://www.dropbox.com/s/cqsxfws52gulkyx/drawing.pdf)
* [Raising Exceptions](https://realpython.com/python-exceptions/)
* [A deep dive into try/except clauses](https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
* To get advanced, add [logging](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/) to your code.
* To get very advanced, include [unit tests](http://www.diveintopython.net/unit_testing/index.html)
* The [pytest module](http://pythontesting.net/framework/pytest/pytest-introduction/) is great for unit testing.