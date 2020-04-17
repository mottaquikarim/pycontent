# Data Visualization

### Objectives

In this lesson, we'll discuss what plotting capabilities are available with Pandas, Matplotlib, and Seaborn. We'll combine a cherry-picking of features that will allow you to create common plots with elegance, but relative ease. Here is a summary of points we'll cover:

>>
* A review of qualitative data viz best practices
* The anatomy of a plot and the building blocks of data visualizations
	* Seaborn plotting fundamentals and styles
* Which visualizations to use in different scenarios
* Example code for common charts and diagrams using Pandas, Seaborn, and elements of Matplotlib

### Review 

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

### Importing Plotting Libraries

```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline # specific to Jupyter Notebooks & Colab*
import seaborn as sns

print('import successful')
```

*`%matplotlib inline` tells Python to draw the figure inline with the code as opposed to making it available only as a downloadable .png file.

## Anatomy of a Plot

The underlying elements of a plot:

<img src="https://files.realpython.com/media/fig_map.bc8c7cabd823.png" style="margin: 0 auto; float: right;"/>
[image source](https://realpython.com/python-matplotlib-guide/#the-matplotlib-object-hierarchy)

* The **Figure** encompasses the axes as well as all its accompanying parts, i.e. the title, the legend, axis labels, etc.
* If you have a grid/matrix of graphs in a single figure, we call each cell in the grid a **Subplot**. 
* When you create a subplot, it automatically creates an **Axes** object. This is where the data actually gets graphed.
* Spines refer to the outlines of the axes (bottom (x-axis), left (y-axis), top, and right)
* **Ticks** are the periodic marks on the x and y axes.
* You should also include a **Title** and **Labels** for the x and y axes. 
* A **Legend** (not pictured above) is used to define  different colors or shapes on a single graph as different categories or segments of data.

With matplotlib, many of the above objects must be created manually BEFORE plotting the data. With Pandas and Seaborn, the figure, axes, and often the labels are created implicitly when you plot the data. 

```python
fig = plt.figure(figsize=(7,7))
```


```python
fig, ax = plt.subplots() # default args are nrows=1, ncols=1
```


```python
fig, ax = plt.subplots(nrows=2, ncols=2)
```

```python
fig, ax = plt.subplots(figsize=(7, 7))
```


```python
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
```

You CAN combine certain matplotlib functions to your Pandas and Seaborn plots to add some customization. The main ones you'll use are:

* `plt.title()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.legend()`

## Setting Seaborn Figure Styles

Write a function for a special sine wave graph. This is straight from the seaborn tutorial and just so that we can have a way to illustrate styles without loading a dataset.

```python
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()
```

### Color Palettes

* `sns.color_palette()` -- create a `_ColorPalette` object

>>This function can accept preset palettes or a list of HEX colors in string format e.g. '#3399FF'
	>> find list of pre-existing seaborn options https://seaborn.pydata.org/tutorial/color_palettes.html

```python
BrBG = sns.color_palette('BrBG')
print(type(BrBG))
```

* `sns.palplot()` -- prints an image of whatever color palette is passed to it

```python
sns.palplot(BrBG)
```

* `sns.setpalette()` -- pass a `_ColorPalette` object to use it with all the plots you subsequently create

```python
sns.set_palette(BrBG)
sinplot()
```

### Axes Styles

* `sns.set_style(style='ticks')` -- styles the axes

Options include `ticks` (default), `darkgrid`, `whitegrid`, `dark`, or `white`

```python
sns.set_style('whitegrid')
sinplot()
```

* `sns.set_context(context='notebook', font_scale=1, rc={'lines.linewidth'}: 1.5})`

4 preset contexts, in order of relative size, are 'paper', 'notebook', 'talk', and 'poster'

```python
sns.set_context('talk', font_scale=1.5, rc={'lines.linewidth': 3})
sinplot()
```

### Combining Style Settings

* `seaborn.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)`

```python
sns.set()
sinplot()
```

```python
cpal = ['#3399FF', '#dbb409', '#b43df7', '#2ecc71', '#fa62b7', '#ff8e30', '#e63565']
# sns.palplot(sns.color_palette(cpal))
```


```python
sns.set(context='notebook', style='ticks', palette='BrBG', font_scale=1.2, rc={'lines.linewidth': 1.75, 'figure.figsize': (9, 6)})
sinplot()
```

## Graphs by Purpose

* Histograms: Show the distribution of a numerical variable
* Box-and-Whisker Plots: Show the distribution of a variable, highlighting the quartiles and outliers
* Line plots: Show the trend of a numerical variable over time
* Bar plots: Show a numerical comparison across different categories

Finally, let's load our movies data with `imdbID` as the index so that we can go through some coded examples.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_clean_simple.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

## Histograms

<img src="content/images/plotly_histogram_fig4.gif"/>

```python

```


```python

```

## Box-and-Whiskers Plots

<img src="https://miro.medium.com/max/1400/1*2c21SkzJMf3frPXPAR_gZA.png"/>

```python

```


```python

```

## Bar Plots


```python

```


```python

```

## Line Graphs

>>built-in datasets: https://github.com/mwaskom/seaborn-data


```python

```


```python

```

## Scatterplots



## Key Takeaways


