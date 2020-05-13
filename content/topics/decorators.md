# Decorators

"functions are first-class objects. This means that functions can be passed around and used as arguments, "

>>https://realpython.com/primer-on-python-decorators/

## Inner Functions

You can define, call, and return functions inside other functions, thereby creating a parent-child hierarchy. The children are called inner functions, and they have local scope. Again, that means you can only reference them from within their parent functions.

```python
############ FROM REALPYTHON!!!!!!!

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()
```


```python
def parent(num):
    def first_child():
        return 'Hi, I am Emma'

    def second_child():
        return 'Call me Liam'

    if num == 1:
        return first_child # without parentheses
    else:
        return second_child() # with parentheses

f = parent(1)
s = parent(2)

print(f) # <function parent.<locals>.first_child at ... >
returned_value = f()
print(returned_value) # Hi, I am Emma

print(s) # Hi, I am Liam
```

## Basic Decorator



```python
############ FROM REALPYTHON!!!!!!!
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# this is where the decoration happens
say_whee = my_decorator(say_whee)
# ^ this var represents the return value of the my_decorator function, which IS the wrapper function. That wrapper

say_whee()
```

WITH RIGHT SYNTAX

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()
```


However, after being decorated, say_whee() has gotten very confused about its identity. It now reports being the wrapper_do_twice() inner function inside the do_twice() decorator. Although technically true, this is not very useful information.

To fix this, decorators should use the @functools.wraps decorator, which will preserve information about the original function. 


## Template Decorator

>>https://realpython.com/lessons/decorators-section-3-overview/

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```


## Resources

* [Primer on Decorators](https://realpython.com/primer-on-python-decorators/)
* [Cheat Sheet](https://static.realpython.com/decorators-cheatsheet.pdf?__s=s3czi062ac69nqnzmfws)
* [Template Decorator](https://realpython.com/lessons/decorators-section-3-overview/)
* [Examples](https://github.com/realpython/materials/blob/master/primer-on-python-decorators/examples.py)
* [Examples Using Flask](https://github.com/realpython/materials/blob/master/primer-on-python-decorators/decorators_flask.py)