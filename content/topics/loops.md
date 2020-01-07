# Loops

## Iterating with Loops

In programming, we define `iteration` to be the act of running the same block of code over and over again a certain number of times.For example, say you want to print out every item within a list. You could certainly do it this way -

```python
visible_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

print(visible_colors[0])
print(visible_colors[1])
print(visible_colors[2])
print(visible_colors[3])
print(visible_colors[4])
print(visible_colors[5])
print(visible_colors[6])
```

Attempting to print each item in this list - while redundant - isn't so bad. But what if there were over 1000 items in that list? Or, worse still, what if that list changed based on user input (ie: *either* 10 items *or* 10000 items)?

To solve such problems, we can create a **loop** that will iterate through each item on our list and run the `print()` function. This way, we only have to write the print() one time to print out the whole list!

When you can iterate through an object (e.g. a string, list, dict, tuple, set, etc.), we call it an `iterable` object. Python has many built-in `iterables`. You can reference some of the most common ones in the `itertools` module (read more about itertools [here](https://realpython.com/python-itertools/)). You can also define your own Python iterables using the principles of OOP (object-oriented programming). In fact, Python features a more advanced construct called a `generator` to simplify this process for you.

For now, let's print each color in the visible spectrum again, but take one step toward making this more dynamic. We'll use a variable called `idx` to represent the index positions in `visible_colors`. We'll set `idx = 0` to start, since the first list element is at index 0.

```python
visible_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

idx = 0

print(visible_colors[idx]) # idx = 0
idx = idx + 1

print(visible_colors[idx]) # idx = 1
idx = idx + 1

print(visible_colors[idx]) # idx = 2
idx = idx + 1

print(visible_colors[idx]) # idx = 3
idx = idx + 1

print(visible_colors[idx]) # idx = 4 
idx = idx + 1

print(visible_colors[idx]) # idx = 5
idx = idx + 1

print(visible_colors[idx]) # idx = 6
```

As you can see, you simply have to increase the value of idx by 1 after each item you print. That way, we can repeat `print(visible_colors[idx])` to access ALL elements in the list without typing in their unique index numbers. If you consider this code conceptually...

## the `while` loop

...it is functionally the same as the `while` loop below.

```python
idx = 0

while idx < len(visible_colors):
    print(visible_colors[idx])
    idx = idx + 1
```

The loop represents an abstraction of the code above, wherein we use a boolean expression to determine how many times to run the code in the loop's body. 

At each iteration, we increase the value of idx by 1. As long as `idx < len(visible_colors)` evaluates to `True`, the loop keeps running. Once `idx < len(visible_colors)` evaluates to `False`, the loop ends and your program moves onto the next code block.

### Counting

Here's another very basic use case for the `while` loop:

```python
i = 0
while i < 10:
    print(i)
    i += 1
print(i) # will print out numbers 1 through 10
```

What is happening here is we are running the code block within the `while` 10 times. We know to stop because the `boolean comparison` will evaluate to `False` once i exceeds `10`, which is possible only because `i` is being incremented when we write `i += 1`.

#### Practice Together!

Use a loop to make a list of all odd numbers between 1 and 10 and another list with all the evens in this range. When done, print the lists.

```python
odds = []
evens = []

i = 1

while i <= 10:
  if i % 2 != 0:
    odds.append(i)
  else:
    evens.append(i)
  i += 1

print(odds,'\n', evens)
```

### Booleans

While loops are based on boolean expressions. They effectively direct the program to "do this action as long as this condition is True." Here's real-life scenario where you might apply a `while` loop. Let's say you've programmed your Amazon Echo or Google Home to make a pot of coffee whenever you say the trigger word "tired". Once you say tired, here's a *simplified pseudo-code version* of what happens behind the scenes:

```python
tired = True
while tired:
  print('I\'ll make some coffee!') # this might be a "say" command
  # code to turn on coffee maker
  tired = False
```

Whenever a pot of coffee is made, the smart device sets `tired` back to `False`. Next time you say "tired", it will reset `tired` to `True`. 

## the `for` loop

Let's go back to that list of colors we wanted to print out and use a `for` loop. The most important part of the for loop is the statement `for item in obj`. This means the code **considers each item in the iterable one at a time** when executing the code below.

```python
# Syntax:
# for <item> in <iterable>:
#     <statement(s)>


visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for color in visible_colors:
  print(color)
```

## Loops with Ranges

If you want to iterate through only a section of a list, the `range()` and `enumerate()` functions can facilitate this. `range` and `enumerate` are also both their own data type objects. 

### `range()`

With `while` loops, we saw one way to iterate while counting. Using `range()` with a for loop allows us to be more concise and more specific. 

The  `range()` function uses this syntax: `range(<begin>, <end>, <stride>)`. It returns a `range` iterable that yields values starting with the <begin> index, *up to but **NOT** including the <end> index*. The <stride> argument isn't required, but if specified, it indicates an amount to skip between values. For example, `range(5, 20, 3)` would iterate through 5, 8, 11, 14, and 17. If <stride> is omitted, it defaults to incrementing by 1.

Consider the differences in the loops below...

#### `range()` with a `while` loop

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(len(visible_colors), '\n')

idx = 3

while 2 < idx < 6:
    print(visible_colors[i]) # prints green blue indigo
    idx += 1
```

#### `range()` with a `for` loop

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
print(len(visible_colors), '\n')

x = range(3, 6)

for i in x:
    print(visible_colors[i])
```

### `enumerate()`

When looping through a `list`, you might want to keep track of the index position of the item in each loop iteration. Converting the `list` it into an `enumerate` object allows you to achieve this more easily.

Take a look at what an `enumerate` object looks like below. Note that you can print the object as a whole to view its contents like you do with a list.

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
enum = enumerate(visible_colors)

print('Print whole list...', visible_colors)
print('Print whole enumerate object...', enum)
```

You have to loop through them and print each one. As you do this, you'll see that each item in the `enumerate` object is a tuple. 

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
visible_colors = enumerate(visible_colors)

for i in visible_colors:
    print(i)
```

But you can access each item in each tuple like this...

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
visible_colors = enumerate(visible_colors)

for idx, i in visible_colors:
    print(f'{idx} & {i}')
```

## Control Flow with `break`, `continue`, & `else:`

Something very important to watch out for here is falling into an **infinite loop**. This is one of the most common traps and can make your code go crazy running the loop over and over without moving through the rest of the program! It happens when you do not have proper control flow in the loop's code. 

The **`break` keyword**, the **`continue` keyword**, and the **`else: ` statement** are three core ways to help control the flow and logic within your loops.

### The `break` Keyword

In a Python loop, the `break` keyword *escapes the loop*, regardless of the iteration number and regardless of how much of the loop code it has completed on its current iteration. Once a break executes, the program will continue to execute after the loop.

We might use a break statement if we only want the loop to iterate under a certain condition. For example:

```python
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')

## This loop will output...
"""
corge
qux
baz
Done.
"""
```

Let's walk through the logic of how we got that outcome:

```python
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
```
* ^^^ This tells us that as long as `a` is `True` - essentially, as long as it exists - go ahead with the next loop iteration.

```python
if len(a) < 3:
        break
    print(a.pop())
```
* ^^^ This says that, if the length of `a` is less than 3, break out of the loop. In the first iteration, `a` has 5 items. Given this, the `break` is not executed. Instead, the code removes a random item from `a` and prints it. Once the loop gets to the 4th iteration, `len(a)` is 2. This triggers the `break`.

After that, the program goes to the next line of code after the break, in this case `print('Done.')`.

This works the same with a `for` loop as in the example below. Can you think through why we get the outcome `foo` here?

```python
for i in ['foo', 'bar', 'baz', 'qux']:
  if 'b' in i:
    break
  print(i) # foo
```

### The `continue` Keyword

You can also use the `continue` keyword to interrupt the loop code. The difference is that the `continue` keyword escapes *only the current iteration*. A `break` escapes the loop entirely and goes on to execute the code immediately following the loop. A `continue` tells the program to stop where it is within the within the current iteration and *skip to the the next iteration* of the loop. 

Here's an example using a `while` loop. Notice that the `continue` applies to the *outer* while loop, whereas the `break` applies only to the *inner* while loop.

```python
# Prints out 0,1,2,3,4
s = ''

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break

print(s) # '3foo3bar1foo1bar'
```

As the program iterates through the decreasing values of `n`, it determines whether each value is even. The `continue` executes *only for these even-number iterations*. Then the loop continues to the next iteration. Thus, the inner while loop only initiates when n is 3 and 1.

Inside the inner while loop, `a.pop(0)` removes the first item of a. Once this has occurred twice, yielding 'foo' and 'bar', a has fewer than two items, and the `break` terminates the inner loop. Thus, the values concatenated onto `s` are, in turn, 3foo, 3bar, 1foo, and 1bar.

Again, this works the same with `for` loops like so:

```python
for i in ['foo', 'bar', 'baz', 'qux']:
  if 'b' in i:
    continue
  print(i) # foo, qux
```

### The `else` Statement
The `else` statement works similarly to a `break` in that it is triggered once the loop has finished all iterations that meet any conditional specifications. Now, you might wonder why you might use this because putting a statement after the loop will also execute once the loop has finished all iterations that meet any conditional specifications.

Here's the difference:

Statements after the loop *will always execute*. But if you place additional statements in an `else` clause, the program will only execute them if the loop terminates *by exhaustion*. In other words, it **only** executes if the loop fully completes each iteration until the controlling condition becomes false. If a `break` terminates the loop before that, for example, the `else` clause won't be executed.

```python
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    print(a.pop())
else:
    print('Done.') # foo, bar, baz, qux, Done.
```

And again, here's are `for` loop examples where the `else` statement will and will NOT execute:

```python
# else DOES execute
for i in ['foo', 'bar', 'baz', 'qux']:
  print(i)
else:
  print('Done.') # foo, bar, baz, qux, Done.

# else DOES NOT execute
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') # foo
```

Here, `i == 'bar'` evaluates to `True` during the second iteration. Even though the third and fourth iterations could have printed when evaluated by the conditional, the `break` executed before the loop got there. Therefore, the loop did not exhaust all viable iterations and it does not trigger the `else` statement.

### Infinite Loop Example

See if you can figure out why this loop is infinite. (Tip: Don't actually run this code, or your computer will freak out!)

```python
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        continue
    print(a.pop())
print('Done.')
```

Got it? After the first three iterations, `a` shrinks to fewer than three items and executes a `continue` statement. It then returns to the beginning of the loop, where it will find that `a` still has fewer than three items. So it goes back to the beginning again... and again and again and again... 

Your program will get stuck here, so you want to make sure you pay special attention to the control flow when you write loops!

## Iterating Through Dicts

Iterating over dicts is slightly more complicated than other iterabless because each item consists of two elements, specifically mapped to each other. That said, you can do some really cool stuff with your dicts using loops! 

#### Iterate Through Dict Items
Let's start with a few simple examples. This first one iterates over the dict by each *item*, i.e. each key-value pair.

```python
transaction = {
  "amount": 10.00,
  "payee": "Joe Bloggs",
  "account": 1234
}

for key, value in transaction.items():
    print(f'{key}: {value}')

"""Output:
account: 1234
payee: Joe Bloggs
amount: 10.0"""
```

#### Iterate Through Dict Keys

If you only have a dict's keys, you can still iterate through the dict. Notice the loop below results in the same output as the one above iterating through items.

```python
transaction = {
  "amount": 10.00,
  "payee": "Joe Bloggs",
  "account": 1234
}

for key in transaction.keys():
    print(f'{key}: {transaction[key]}')

"""Output:
account: 1234
payee: Joe Bloggs
amount: 10.0"""
```

### Sorting Dicts with Loops

#### By Key


```python
transaction = {
  "amount": 10.00,
  "payee": "Joe Bloggs",
  "account": 1234
}

for key in sorted(transaction.keys()):
    print(f'{key}: {transaction[key]}')


"""Output:
account: 1234
amount: 10.0
payee: Joe Bloggs"""
```

#### By the Values of Each Key

Note that the dict itself will not be sorted by the first value in each item. Because the keys are the unique element of a dict, you can only sort dict values *within each key*.

```python 
dict1 ={ 
  "L1":[87, 34, 56, 12], 
  "L2":[23, 00, 30, 10], 
  "L3":[1, 6, 2, 9], 
  "L4":[40, 34, 21, 67] 
}

for k, v in dict1.items(): 
  sorted_pair = {k: sorted(v)} # here is sorting!
  dict1.update(sorted_pair)

print(dict1)
""" # prints out...
{'L1': [12, 34, 56, 87],
'L2': [0, 10, 23, 30],
'L3': [1, 2, 6, 9],
'L4': [21, 34, 40, 67]
} """
```