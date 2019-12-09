# Modules & Packages

When you `modularize` code, it means that you group functions and objects into specific areas of focus. We call these groups `modules` and `packages`. A `module` is a Python source file that contains pre-defined objects like variables, functions, classes, and other items we'll talk about soon. A Python `package`, sometimes used synonymously with the term `library`, is simply a collection of Python modules.

The diagram below can show you this hierarchy visually.

![package_def](https://365datascience.com/wp-content/uploads/2018/07/image2-min-6-768x419.png)

For instance, the `statsmodels` module ([here](https://www.statsmodels.org/)) contains code useful to a data scientist. The `Pyglet` library ([here](http://www.pyglet.org/)) contains code useful to game developers needing shortcuts for 3D game animation. 

`Modular programming` allows us to break out certain packages and modules from the standard library. This means that when you first install Python, the packages and models that have been broken out are NOT installed. If you want to use them, you have to separately import them. It's sort of like "a la carte" code, and it makes the standard library more efficient for the general public. This becomes especially valuable once you scale your programs. Why take on extra baggage?

## Global vs. Local Scope

One of the reasons Python leverages modular programming is because it helps avoid conflicts between `local` and `global` variables. It does so by creating separate `namespaces`. `Namespaces` are the place where variables are stored, and they exist on several independent levels, including **local, global, built-in, and nested namespaces**. For instance, the functions `builtin.open()` and `os.open()` are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. 

At a high level, a variable declared outside a function has `global scope`, meaning you can access a it inside or outside functions. A variable declared within a function has `local scope`, which means you can only access it within the object where you created it. If you try to access the variable outside that object, you will get a `NameError` telling you that variable is not defined. The same goes for functions created within modules, as you'll see soon. 

## Importing Modules & Packages

Importing modules and packages is very easy and saves you a lot of time you'd otherwise spend reinventing the wheel. Modules can even import other modules! 

Let's look at a few different way to import modules and their contents. The simplest way to import a module is to simply write `import module_name`. This will allow you to access all the contents within that module. Take a look at how we use the square root function from the `math` module:  

```python
import math
math.sqrt(25) # 5
```

Notice how we included `math.` when we called the `sqrt` function. Because of *variable scope*, you need to reference the `namespace` where `sqrt` is defined. Simply importing `sqrt` does not give it `global scope`. It still has `local scope` within the math module.

#### Optimize Your Imports

One way to decrease clutter in your code is to give the module a custom name when you import it. If we rename the `math` module `m`, the code to call a function is more succinct.

```python
import math as m
m.sqrt(25) # 5
```

If you only need a few functions from a module, you can go one step further. When you import a module, you can specify that you only want to import certain functions. This obviates the need to reference the name of the module when you call its functions.

```python
from math import sqrt, pow, factorial
sqrt(25) # 5
pow(12, 2) # 144
factorial(8) # 40320

print(sqrt(25), pow(12, 2), factorial(8))
```

If you want, you can even give the imported functions shorter names.

```python
from math import sqrt as s, pow as p, factorial as f
s(25) # 5
p(12, 2) # 144
f(8) # 40320

print(s(25), p(12, 2), f(8))
```


The same works for modules. Below, we're importing the `math` module under the alias `m`. *Note the difference in how we reference the square root function.*

```python
import math as m
m.sqrt(25) # 5.0`
```

>>
The best practice is to place all import statements at the of your script file so you can easily see everything you've imported right at the top.

## Managing Dependencies

In addition to "built-in" modules, Python provides the ability to create, distribute and most importantly *consume* community defined Python modules. This is powerful because anyone who builds something useful has the ability to share with the larger python community. Modules can be found in [**PyPI**](https://pypi.org/), or, the Python Package Index. Any registered module in pypi is installable by running `pip install <module_name>`.

However, let's say Project A requires module1 version 1.2, while Project B, which you started a year later needs to use module1 version 2.1. How can you ensure that each project has access to the correct version of module1? In order to safely install modules across projects, we need to create **virtual environments**, or isolated python environments where we can install our modules and rest assured that they won't interfere with other projects or the system at large.

Here's how you create a virtual environment:

```python
python3 -m venv .env
source .env/bin/activate
```

The `.env` folder contains everything needed for this **"virtualenv"**. We go *inside* the env by running the `source ./env/bin/activate` command. To exit `.env`, simply write `deactivate`.

>>NOTE!
While using Colab, you don't need to worry about virtual environments. Google manages dependencies for you in that each separate notebook acts as its own virtual environment.

## Common & Featured Modules & Packages

* [Python's `itertools` library](https://docs.python.org/3/library/itertools.html)
* [Pandas](http://pandas.pydata.org/) / ([Pandas github repo](https://github.com/pandas-dev/pandas))
* [NumPy](https://www.numpy.org/) / ([NumPy github repo](https://github.com/numpy/numpy))
* [SciPy](https://www.scipy.org/) / ([SciPy github repo](https://github.com/scipy/scipy))
* [Matplotlib](https://matplotlib.org/) / ([Matplotlib github repo](https://github.com/matplotlib/matplotlib))
* [scikit-learn](https://scikit-learn.org/) / ([scikit-learn github repo](https://github.com/scikit-learn/scikit-learn))
