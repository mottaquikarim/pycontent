# Data Visualization with Matplotlib & Seaborn

### Objectives

>>* Matplotlib and the building blocks of data visualizations
* Seaborn plotting fundamentals and styles
* Which visualizations to use in different scenarios
* Example code for common charts and diagrams

### Review 

Below is a brief review of the key points about data visualization & storytelling from the "Data Science Foundations" section.

* Visualizations serve to quickly explain features and conclusions about data to your stakeholders.
* As such, they should be *simple*, *uncluttered*, and *clearly labeled*. Less is more.
* Visual considerations include position, color, order, & size.
* The best visualizations tell a story about the data by illustrating key points supporting your thesis and conclusions.
* Most importantly, *consider your audience* when crafting your story.
* The chart type you select should accurately represent the variables you are pulling from data in a way that is clearly readable for your audience.

## Import Libraries & Load Data

```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline # specific to Jupyter Notebooks & Colab*
import seaborn as sns

print('import successful')
```

*`%matplotlib inline` tells Python to draw the figure inline with the code as opposed to making it available only as a downloadable .png file.

Load the data with `imdbID` as the index and make a copy.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_clean_simple.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

## Anatomy of a Plot

<img src="https://files.realpython.com/media/fig_map.bc8c7cabd823.png" style="margin: 0 auto; float: right;"/>

* Figure encompasses the axes as well as all its accompanying parts, i.e. the title, the legend, axis labels, etc.
* Axes (aka subplot) are where the data will be graphed.
* Spines
* Ticks
* Labels
* Legend


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


## Line Graphs

>>built-in datasets: https://github.com/mwaskom/seaborn-data

Show the trend of a numerical variable over time

```python

```


```python

```


```python

```


```python

```


```python

```


```python

```