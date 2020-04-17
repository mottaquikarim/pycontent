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
%matplotlib inline
import seaborn as sns

print('import successful')
```

**`%matplotlib inline`** is specific to Jupyter Notebooks & Colab. It tells Python to draw the figure inline with the code as opposed to making it available only as a downloadable .png file.

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
* `fig.suptitle()` -- adds a title to the overall figure if there's more than one subplot (i.e. supertitle)
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.legend()`
* `plt.savefig('image_name.png', transparent=False)`

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
cpal = ['dodgerblue', '#2ecc71', '#bb64ed', '#ffd13b', 'xkcd:tangerine', '#fa62b7']
sns.palplot(sns.color_palette(cpal))
```


```python
sns.set(context='notebook', style='ticks', palette=cpal, font_scale=1.2, rc={'lines.linewidth': 1.75, 'figure.figsize': (9, 6)})
sinplot()
```

## Load OMDb Data

Finally, let's load our movies data with `imdbID` as the index so that we can go through some coded examples.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_clean_simple.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

## Histograms

Histograms provide numerous insights into a numerical distribution, chiefly the frequency of values. Although they look similar to bar charts, histograms have a distinct purpose. Histograms visualize the frequency of values in a sample of quantitative data, while bar charts compare the values comprising a categorical value. 

<img src="content/images/plotly_histogram_fig4.gif"/>
[image source](https://plotly.com/chart-studio-help/histogram/#normalizing-a-histogram)

Histograms give you a sense of:

* How much variation exists in the sample
* Where most of the values lie (e.g. the mode)
* Whether the distribution skews right or left (aka high or low)

### Pandas

`<series>.plot(kind='hist', bins=None)`

`bins` is optional. The underlying matplotlib function will determine "the best" number of bins to visualize the distribution in question.


```python
movies['Runtime'].plot(kind='hist')
```


```python
movies['Runtime'].plot(kind='hist', bins=50)

# set the title
plt.title('Distribution of Runtime')

# add a label to the x-axis
plt.xlabel('Runtime')
```

### Seaborn

`sns.distplot(a, bins=None, hist=True, kde=True, color=None, ax=None)`

*Make sure to set `kde=False` because otherwise it gives the plot a different context. The y-axis gives it away... it's showing something called a probability density function, which Check out the y-axis to see the difference*

```python
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))

sns.distplot(movies['imdbRating'], ax=ax1)
sns.distplot(movies['imdbRating'], kde=False, ax=ax2)
```

Compare two distributions: critic vs audience

```python
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))
fig.suptitle('Frequency Distributions for IMDb Rating and Rotten Tomatoes')

sns.distplot(movies['imdbRating'], kde=False, ax=ax1)
sns.distplot(movies['Rotten Tomatoes'], color='#2ecc71', kde=False, ax=ax2)
```


## Box-and-Whiskers Plots

For a data sample, a box-and-whiskers plot ("box plot" for short) helps you visually quantify the amount of **variability** in your data sample. *<DEFINE VARIABILITY>* The box plot visualizes this by leveraging the values of the quartiles in your data sample.

<img src="https://miro.medium.com/max/1400/1*2c21SkzJMf3frPXPAR_gZA.png"/>

* The range: The lowest point to the highest point
* The IQR is represented by height of the box  bottom to the top of the box
* The longer the whiskers are, the more variability there is in your sample
* The more narrow the box, the more tightly focused the data points are around the median

### Pandas

The Pandas version of the box plot is very simple, but a bit hard to read.

`<series>.plot(kind='box')`

```python
movies['Runtime'].plot(kind='box')
```

### Seaborn

#### Single Box Plot

`sns.boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, ax=None)`

```python
sns.boxplot(x='Runtime', data=movies)
```

#### Grouped Box Plot w. One Categorical Variable


```python
lang_count = movies.groupby('Language')['Title'].count().sort_values(ascending=False)
lang_count.head()
```

```python
top_langs = list(lang_count.head().index.values)
top_lang_subset = movies[movies['Language'].isin(top_langs)]
```


```python
sns.boxplot(x='Runtime', y='Language', data=top_lang_subset)
plt.title('Distribution of Runtime for Top Movie Languages')
```

#### Grouped Box Plot w. Two Categorical Variables


```python
genre_count = movies.groupby('Genre')['Title'].count().sort_values(
    ascending=False)
genre_count.head()
```


```python
top_genres = list(genre_count.iloc[:2].index.values)

# take only the top 3 languages for readability in this example
genre_lang_subset = movies[(movies['Language'].isin(top_langs[:3])) & (movies['Genre'].isin(top_genres))]
```


```python
sns.boxplot(x='Runtime', y='Language', hue='Genre', data=genre_lang_subset)
plt.title('Distribution of Runtime for Top Movie Languages and Genres')
```


## Bar Charts

### Pandas

```python
genre_count = movies.groupby('Genre')['Title'].count().sort_values(ascending=False)
genre_count
```

```python
genre_count.plot(kind='bar')
plt.title('Number of Movies by Genre')
plt.ylabel('Number of Movies')
```

### Seaborn

It's hard for people to discern the area of the wedges in a pie chart. 

If you have a lot of categories, orienting your bar chart horizontally provides better readability.

```python

```


```python

```


```python

```

## Line Graphs

### Pandas

```python

```


```python

```

### Seaborn

```python

```


```python

```



## Scatterplots



## Key Takeaways

*Note: Parameters with a default argument of None are optional*

**Histogram**

* Purpose: Illustrate the frequency distribution of a numerical variable
* Pandas: `<series>.plot(kind='hist', bins=None)`
* Seaborn: ``

**Box-and-Whiskers Plot**

* Purpose: Highlight the variability in a distribution
* Pandas: `<series>.plot(kind='box')`
* Seaborn: ``

**Bar Chart**

* Purpose: Show a numerical comparison across different categories
* Pandas: `<series>.plot(kind='bar')`
* Seaborn: ``

**Line Graph**

* Purpose: Show the trend of a numerical variable over time
* Pandas: `<series>.plot()`
* Seaborn: ``

**Scatterplot**

* Purpose: Compare the relationship between two numerical variables
* Pandas: `<series>.plot.scatter(x, y)`
* Seaborn: ``



