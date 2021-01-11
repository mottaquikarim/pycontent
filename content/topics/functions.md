# Functions

In Python, `functions` are your best friends! Let's say you need to perform some action or calculation multiple times for multiple values. For example, you might want to convert temperatures in Celsius to Fahrenheit like you did in the last chapter's exercises. It would be inefficient and messy to copy that code every time you need it. Instead, you can define a `function` to contain that code. Every time you call that function, it runs the whole block of code inside and saves you lots of time. Sweet!

## Anatomy of a Function

For now, let's start with the basics. Here's the skeleton of a function and a breakdown of each part.

```python
def function_name(parameters):
    """docstring"""
    # statement(s)
```

**Naming & Input**
* `def` shows you are "defining" a new function
* A unique function_name (same naming rules as  variables)
* *Optional* variables, or `parameters`, that represent what input the function needs in order to run correctly
* `:` ends the function header

**Function Body**
* An *optional* `docstring`, i.e. a comment that documents the purpose and workings of the function
* At least one statement make up the `function body`; this code achieves the purpose for calling the function.

**Output**
* An *optional* `return statement`, which exits the function and passes out some `return value(s)` from the function's body code.

### A Simple First Function

Let's say we want to create a function to get the square of a number. At the most basic level, there are three parts:
1. Input the number we want to square
2. Calculate the square of that number
3. Output the square of that number

Let's implement this in a function called `NumSquared()`.

```python
def num_squared(num):
    """Find the square of some number passed in"""
    square = num*num # code to find the square
    return square
```

1. Input the number we want to square 

We create an *parameter* called `num` to represent the number we will past into our function as an argument. (p.s. Parameters are the names used when defining a function.) Remember that arguments should always be passed in the correct format and positional order, or the function will not be able to recognize them.

2. Calculate the square of that number

Using the value of `num`, we write the formula for calculating a square and assign it to the variable `square`.

3. Output the square of that number

We return `square` to pass out the numeric value we calculated. 

Once we've written this logic, we can call `NumSquared()` every time we want to use it. Let's say we want to find the value of 12 squared...

```python
sq12 = num_squared(12)
print(sq12) # 144
```

**NOTE!** Make sure you store the function call within a var so that the return value gets stored in the var. If you don't, how will you access the output you wanted??

## Variable Scope

* `global variable`: 
  * A variable declared outside a function
  * Any function in your script can access this
* `local variable`: 
  * A variable declared within a function's code block
  * You can only access this variable within the function where it is declard, otherwise you will get a `NameError` telling you that variable is not defined.


```python
x = 'I\'m a global variable.'

def foo():
    x = 'I\'m a local variable.'
    print(x) # I'm a local variable.
    return x

y = foo()

print(x) # I'm a global variable.
print(y) # I'm a local variable.
```

Notice that even though the function `foo()` above says `return x`, it **only returns the value of the local variable `x`**. We assign this *value* to the variable `y` when we call foo().

## Function Outputs

Let's expand on output a bit...

The return statement exits the function so the program can move on to the next block of code you've written. If you don't need to specify a value to return, the function will default to `return None` in order to exit the function.


```python
def say_hello():
    print('hello!')
```

Also, the `return` statement can return multiple values *by using tuples*. Once you return the tuple from the function, you can *unpack* its values by simultaneously assigning each one to a new var as follows...

```python
    # some function...
    return 3,'a',True

x, y, z = (3,'a',True)
print(x, type(x)) # 3 <class 'int'>
print(y, type(y)) # a  <class 'str'>
print(z, type(z)) # True <class 'bool'>
```

## Types of Function Input

The term `parameter` and the term `argument` are often used synonomously to refer to function input values. However, there *IS* a distinction between the two terms:

* **`Parameters`** are values you declare when defining a function. 
* **`Arguments`** refer to the values passed into the function upon calling it

**Required vs. Optional Parameters**

You have a fair amount of flexibility when it comes to defining function parameters. This is because there are so many different use cases for the amount and type of input needed. The differences between function inputs are signified in the syntax of the function definition. We'll go through examples for the main use cases now...

### Required Parameters

Below is how you'd define parameters for two *required* inputs with *no default values*. Whenever you call this function, you must pass values for each required argument *in the same positional order in which they were defined*.

```python
def plus(a, b):
  return a + b

c = plus(8, 12)
print(c) # 20
```

### "Optional" Parameters

If you want, you can give your parameter a **default argument**. Doing so means that you don't have to explicitly pass an value for that argument when you call the function. In that case, the function assumes that you've implicitly passed the pre-defined default value to that argument. 

**NOTE!** Technically speaking, these parameters are still required. If you don't pass them arguments when you call the function, Python still does it for you. Hence, we say they're "optional" because it's optional for us to pass them arguments.

Let's take a look at another version of our `plus()` function with default arguments for `b` and `c`:

```python
def plus(a, b = 12, c = -1):
    return a + b + c

# Explicitly passing values for b & c
sum1 = plus(8, b = 4, c = 3)
print(sum1)

# Implicitly passing default values for b & c
sum2 = plus(8)
print(sum2)
```

Here's where things get a little sticky between how terms are colloquially used and how they actually work in Python... In practice, `b` and `c` are called **keyword arguments** because you often reference their keyword when you do want to pass them some explicit value.

```python
def plus(a, b = 12, c = -1):
    return a + b + c

# sum3 and sum4 will be the same
sum3 = plus(a = 4, c = -6)
sum4 = plus(4, c= -6)

print(sum3, sum4)
```

That said, you *CAN certainly reference the keyword for required arguments as well*. It even makes sense to do so when you're using complex built-in functions. For example, some pandas functions have several required parameters AND more than a few optional ones.

**IMPORTANT!**

Unlike required arguments, keyword arguments can be passed to the function *in any order*. As a best practice for when you define your functions and when you use functions, you should place the required arguments first, then the optional ones. Here's another example:

```python
def full_name(first, last, middle = None, prefix=None, suffix = None):
    parts = [prefix, first, middle, last, suffix]
    name = ''
    for i in parts:
        if i is not None and len(name) != 0:
            name += f' {i}'
        elif i is not None:
            name += f'{i}'
    return name

name1 = full_name('Taq', 'Karim')
name2 = full_name('Julianna', 'Garreffa', prefix = 'Ms.')
name3 = full_name('Rupert', 'Buckworth', suffix = 'III', middle = 'Malcolm', prefix = 'Mr.')

print(name1)
print(name2)
print(name3)
```

### Variable number of Arguments

Even if you're not sure how many arguments you will need to pass to your function, you can still define it. To do this, you use the parameter `*args` as a stand-in. This signals to the function that it should expect any variety of arguments. Let's take a look at a few different ways to implement this.

**Using integers** (as we did in the earlier examples)

```python
def plus(*args):
  return sum(args)

c = plus(8, 12, 17)
print(c) # 37
```

**Using different data types**

```python
def length(*args):
  list1 = [*args]
  return len(list1)

c = length(8, 'a', True)
print(c) # 3
```

**Using a variable**

```python
var1 = 'h' + 'i'
def print_all(*args):
  list1 = [*args]
  return list1

c = print_all(8, 'a', True, var1)
print(c) # [8, 'a', True, 'hi']
```

**NOTE!** If you use `*args`, your function will be more flexible, *but only if you write it that way*. If you expect different types of arguments, you will have to write the function such that it can handle every use case you expect could occur.

If interested, you can learn more about the intricacies of `*args` and its cousin `*kwargs` [here](https://realpython.com/courses/python-kwargs-and-args/).

### 🏋️‍♀️ **EXERCISES** 🏋️‍♀️ 

Flex your functions muscles in your copy of `function_psets.ipynb` in Google Drive.

### Key Takeaways

* This is the most generic anatomy of a function:

```python
def func_name(required_params, keyword_args = 'default_arg'):
    """docstring"""

    # statement(s) with local variables

    return None
```

* Local variables are those defined within a function and which can only be accessed inside that function.
* Global variables are defined outside functions and can be accessed anywhere in the code.
* The `return` statement:
  * Defaults to returning `None`
  * Can be passed multiple values, which will be output together as a tuple
* **Required Paremeters**:
  * Must be passed arguments in positional order
  * Can optionally be referenced by name 
* **Keyword Arguments**:
  * Have a default argument assigned
  * Can be passed arguments in *any* order
  * Should be referenced by name
  * If no argument is explicitly passed, Python automatically passes the default argument value.
* The `*args` parameter is used when any number of arguments can be passed to a function.



   




