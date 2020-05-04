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
| `ValueError` | When you are trying to convert bad keyboard input to a number |
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

**Cause**: Most commonly caused by trying to convert a bad string into a number.

```python
# This is okay!
my_num = int("10")

# This throws a ValueError
my_num = int("Moose")
```

## Anticipating Errors with Try/Except

Sometimes, we have code that we expect might throw an error.

```python
# The user might not give us a number!
my_num = int(input("Please give me a number:"))
```

What if the user types a string like "Moose"?

- This causes a `ValueError` - we'll be trying to make an int out of a string "Moose".
- We can anticipate and prepare for it!

<aside class="notes">

**Teaching Tips**:

- Start by making sure they understand what the code does. They've seen `input` a few  times, but won't officially learn it for three more lessons; they just learned type casting.

**Talking Points**:

- "Sometimes you may expect certain code to throw an error, and you may want to handle that situation with a smooth error message as opposed to having your whole program blow up with red text."
</aside>

---

## Try-Except

A `Try`-`Except` block is the way we can catch errors in Python. We can catch:

- One error (`except ValueError:`)
- Multiple errors (`except (ValueError, KeyError):`)
- Any/every error (`except:`)

Always try to specify the error, if possible!

**Teaching Tips**:

- Call out that we specifically say "ValueError", and `err` is just a random keyword. Change it to demo. Add other error catches; take out the ValueError specifically.
- "A Try-Except block is the way we can catch errors in Python."
- "We can catch one error (as we see in the code), we can catch multiple errors, or we can just catch any/every error by leaving it blank."
- "You can catch every possible error by leaving the specified error blank, however, this is generally not a great practice because it says very little about how you were thinking."

**Replit Note:** The repl.it has

```python
my_num = None

while my_num is None:
  try:
      my_num = int(input("Please give me a number:"))
  except ValueError as err:
      print("That was not good input, please try again!")
      print("Error was", err)

print("Thanks for typing the number", my_num)
```


## You do: Try-Except


Add a try-except statement to your guessing game which ensures the user inputs a valid number.

## Python Debugger `pdb` - Python 3.7 or greater

**Pro Tip**: You can drop in a `breakpoint()` to stop your code and see what is going on.

* Use `breakpoint()` statements on each line to peek at the values.
* It's like dropping in a `print` but better, as you stop your code in it's tracks
* Remember to remove debugging statements once the problem is solved!

```python
x = 8
y = 10
get_average = x + y / 2
breakpoint()

testing_sum = x + y # To figure out why, break it down.
print("testing_sum is", testing_sum) # Print out each step.
testing_average = testing_average / 2
breakpoint()

print("testing_average is", testing_average) # The individual math test works
# We know there must be a problem with the logic in "average"
```

When your programs become very complex, adding `print` statements will be a great help.

## Summary and Q&A

* Python has many common built-in errors.
* Use `try`/`except` syntax to catch an expected error.
* Logic issues don't throw errors, so be careful!
* Use `print` and/or `breakpoint()` statements to walk through your code line-by-line.

## Additional Resources

* [List of Built-In Errors](https://www.tutorialspoint.com/python/standard_exceptions.htm)
* [Error Flowchart PDF](https://www.dropbox.com/s/cqsxfws52gulkyx/drawing.pdf)
* [Try-Except Documentation](http://www.pythonforbeginners.com/error-handling/python-try-and-except)
* [A deep dive into try/except clauses](https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
* To get advanced, add [logging](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/) to your code.
* To get very advanced, include [unit tests](http://www.diveintopython.net/unit_testing/index.html)
  * The [pytest module](http://pythontesting.net/framework/pytest/pytest-introduction/) is great.
