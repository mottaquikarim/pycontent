# Data Visualization I: Intro to Plotting Libraries

## Objectives

In this lesson, we'll discuss what plotting capabilities are available with Pandas, Matplotlib, and Seaborn. We'll combine a cherry-picking of features that will allow you to create common plots with elegance, but relative ease. Here is a summary of points we'll cover:

* A review of qualitative data viz best practices
* The anatomy of a plot and the building blocks of data visualizations
* Styling with Seaborn

## Review 

Below is a brief review of the key points about data visualization & storytelling from the "Data Science Foundations" section.

* Visualizations serve to quickly explain features and conclusions about data to your stakeholders.
* As such, they should be *simple*, *uncluttered*, and *clearly labeled*. Less is more.
* Visual considerations include position, color, order, & size.
* The best visualizations tell a story about the data by illustrating key points supporting your thesis and conclusions.
* Most importantly, *consider your audience* when crafting your story.
* The chart type you select should accurately represent the variables you are pulling from data in a way that is clearly readable for your audience.

## Intro to Plotting Libraries

Let's start with where the different libraries fit in:

* Matplotlib is the foundational data viz library in Python. Plotting functionality in other libraries is built on top of Matplotlib. Matplotlib is vastly flexible, but also quite complex. 
* Pandas plotting capabilities are limited to the basics. Pandas provides a way to plot using your Series or DataFrame object as a base. (We'll explain that shortly). Any bells and whistles require you to incorporate Matplotlib.
* Seaborn specializes in statistical visualizations. It simplifies the creation of a collection of statistical plots, but it lacks some of the customization options that Matplotlib provides.

```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

print('import successful')
```

**`%matplotlib inline`** is specific to Jupyter Notebooks & Colab. It tells Python to draw the figure inline with the code as opposed to making it available only as a downloadable .png file.

## Anatomy of a Plot

The underlying elements of a plot:

<img src="https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/fig_map_realpython.png" width="400px"/>

[image source](https://realpython.com/python-matplotlib-guide/#the-matplotlib-object-hierarchy)

* The **Figure** encompasses the axes as well as all its accompanying parts, i.e. the title, the legend, axis labels, etc.
* If you have a grid/matrix of graphs in a single figure, we call each cell in the grid a **Subplot**. 
* When you create a subplot, it automatically creates an **Axes** object. This is where the data actually gets graphed.
* Spines refer to the outlines of the axes (bottom (x-axis), left (y-axis), top, and right)
* **Ticks** are the periodic marks on the x and y axes.
* You should also include a **Title** and **Labels** for the x and y axes. 
* A **Legend** (not pictured above) is used to define  different colors or shapes on a single graph as different categories or segments of data.

With Matplotlib, many of the above objects must be created manually BEFORE plotting the data. With Pandas and Seaborn, often the figure, axes, and even the labels are created implicitly when you plot the data. 

### Plot Anatomy Examples

1. Here is how you would create a figure object with a custom size using Matplotlib. Notice how it does not print any sort of visual object. That's because it doesn't have any axes objects on it yet.

```python
fig = plt.figure(figsize=(7,7))
```

2. `plt.subplots()` creates a figure object with some number of subplot/axes objects. Its default args are `nrows=1, ncols=1`, so the below code creates only a single subplot/axes object. Using the tuple unpacking syntax below allows you to access the figure and axes objects individually. 

```python
fig, ax = plt.subplots() # default args are nrows=1, ncols=1
```

3. This creates a 2x2 grid of axes objects on a single figure:

```python
fig, ax = plt.subplots(nrows=2, ncols=2)
```

4. You can pass the `figsize` parameters to `plt.subplots()`...

```python
fig, ax = plt.subplots(figsize=(9, 6))
```

5. ... Note that it changes the size of the whole figure, not each subplot. 

```python
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
```

Various functions for plotting data can infer other descriptive plot elements like the title, labels, and the legend. When possible, they implicitly add those to the plot. However, they also have their own dedicated Matplotlib functions. You can combine these with Pandas and Seaborn plots to add some customization. The main ones you'll use are:

* `plt.title()`
* `fig.suptitle()` -- adds a title to the overall figure if there's more than one subplot (i.e. supertitle)
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.legend()` or `<axes>.legend()`
* `plt.savefig('image_name.png', transparent=False)`

## Setting Figure Styles with Seaborn

To help illustrate style examples without loading a dataset, we've copied a function that creates a sine wave graph from the [Seaborn Aesthetics Tutorial](https://seaborn.pydata.org/tutorial/aesthetics.html).

```python
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()
```

### Color Palettes

* `sns.color_palette()` -- create a `_ColorPalette` object

This function can accept pre-existing Seaborn color palette, like any of the ones found [here](https://seaborn.pydata.org/tutorial/color_palettes.html), or a list of HEX colors in string format (e.g. '#3399FF').

```python
BrBG = sns.color_palette('BrBG') # pre-existing palette

cpal = ['dodgerblue', '#2ecc71', '#bb64ed', '#ffd13b', 'xkcd:tangerine', '#fa62b7']

print(type(BrBG))
```

* `sns.palplot()` -- prints an image of whatever color palette is passed to it

Depending on how many colors a certain plot needs, it will pull them in the order you see here. 

```python
sns.palplot(cpal)
```

* `sns.setpalette()` -- pass a `_ColorPalette` object to use it with all the plots you subsequently create

```python
sns.set_palette(BrBG)
sinplot()
```

### Axes Styles

* `sns.set_style(style='ticks')` -- apply a preset "style" to axes objects

Options include `ticks` (default), `darkgrid`, `whitegrid`, `dark`, or `white`.

```python
sns.set_style('whitegrid')
sinplot()
```

* `sns.set_context(context='notebook', font_scale=1)`

In order of relative size, the four preset context styles are `paper`, `notebook` (default), `talk`, and `poster`. You can separately scale the font-size and line spacing using the `font_scale` parameter.

```python
sns.set_context('talk', font_scale=1.5)
sinplot()
```

### Combining Style Settings

You can customize all the styling settings at once using `sns.set()`. Calling this function with no parameters *resets* all the settings to their defaults:

```python
sns.set()
sinplot()
```

These are the default arguments for the most commonly used parameters in this function:

* `sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)`

Below, we apply a mix of styles that will suit the visualizations in this lesson.

```python
sns.set(context='notebook', style='ticks', palette=cpal, font_scale=1.2, 
	rc={'lines.linewidth': 1.75, 'figure.figsize': (9, 6)})

sinplot()
```