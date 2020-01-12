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
We return `square` to pass out the numeric value we calculated. The return statement exits the function so the program can move on to the next block of code you've written. If you don't need to specify a value to return, the function will default to `return None` in order to exit the function.

Once we've written this logic, we can call `NumSquared()` every time we want to use it. Let's say we want to find the value of 12 squared...

```python
sq12 = num_squared(12)
print(sq12) # 144
```

**NOTE!** Make sure you store the function call within a var so that the return value gets stored in the var. If you don't, how will you access the output you wanted??

One last thing - you should know that the `return` statement can return multiple values *by using tuples*. Once you return the tuple from the function, you can *unpack* its values by simultaneously assigning each one to a new var as follows...

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

### Required vs. Optional Parameters

You have a fair amount of flexibility when it comes to defining function parameters. This is because there are so many different use cases for the amount and type of input needed. The differences between function inputs are signified in the syntax of the function definition. We'll go through examples for the main use cases now...

#### **Required Parameters**

Here's how you'd define parameters for two *required* inputs with *no default values*.

```python
def plus(a, b):
  return a + b

c = plus(8, 12)
print(c) # 20
```

Whenever you call this function, you must pass values for each required argument *in the same positional order as they were defined*.

```python
def plus(a, b):
  return a + b

c = plus(8, 12)
print(c) # 20
```

#### **Default Input Values**

If you want, you can give your parameter a **default argument**. Doing so means that you don't have to explicitly pass an value for that argument when you call the function. In that case, the function assumes that you've implicitly passed the pre-defined default value to that argument.

Here's a version of our `plus()` function with default arguments for `b` and `c`. In practice, `b` and `c` are called **keyword arguments**. Essentially, this means that you mention each argument's parameter name if and when you assign it a value during the function call.

```python
def plus(a, b = 12, c = -1):
    return a + b

# Explicitly passing values for b & c
sum1 = plus(8, b = 4, c = 3)
print(sum1) # 15

# Implicitly passing default values for b & c
sum2 = plus(8)
print(sum2) # 20
```

Unlike required arguments, keyword arguments can be passed to the function in any order. Moreover, since you can assign `None` as a default value, keyword arguments are effectively optional. As a best practice for when you define your functions and when you use functions, you should place the required arguments first, then the optional ones.

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

(For simplicity's sake, let's assume all the inputs for this function are strings!)

#### **Variable number of Arguments**

Even if you're not sure how many arguments you will need to pass to your function, you can still define it. To do this, you use the parameter `*args` as a stand-in. This signals to the function that it should expect any variety of arguments. Let's take a look at a few different ways to implement this.

**Using integers** (as we did in the earlier examples)

```python
def plus(*args):
  return sum(args)

c = plus(8,12,17)
print(c) # 37
```

**Using different data types**

```python
def length(*args):
  list1 = [*args]
  return len(list1)

c = length(8,'a',True)
print(c) # 3
```

**Using a variable**

```python
var1 = 'h' + 'i'
def print_all(*args):
  list1 = [*args]
  return list1

c = print_all(8,'a',True,var1)
print(c) # [8, 'a', True, 'hi']
```

**NOTE!** If you use `*args`, your function will be more flexible, *but only if you write it that way*. If you expect different types of arguments, you will have to write the function such that it can handle every use case you expect could occur.

## Variable Scope Recap

* `global variable`: a variable declared outside a function; any function in your script can access this
* `local variable`: a variable declared within a function's code block; you can only access this variable within the function where it is declard, otherwise you will get a `NameError` telling you that variable is not defined.


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

Look at the nuanced difference in this example though:

```python
def foo():
    x = 'I\'m a local variable.'
    print(x) # I'm a local variable.
    return x

foo()

print(x) # NameError: name 'x' is not defined
```

Even though we called the function `foo()`, we did not assign its return value to a variable outside the function. Therefore, trying to print `x` will output `NameError: name 'x' is not defined`. This is because `x` only exists within the function.
