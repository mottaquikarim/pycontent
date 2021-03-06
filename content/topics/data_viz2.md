# Data Visualization II: Plotting Examples

## Objectives

In this lesson, we'll review example code for common plots using Pandas, Seaborn, and some elements of Matplotlib. These are the plots we'll learn how to create:

* Histograms
* Box-and-Whiskers Plots
* Bar Charts
* Line Graphs
* Scatterplots

## Environment Preparation

Import libraries...

```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

print('import successful')
```

Load the data...

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_clean_simple.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```

Customize styles...

Below, we apply a mix of styles that will suit the visualizations in this lesson.

```python
color_pal = ['dodgerblue', '#2ecc71', '#bb64ed', '#ffd13b', 'xkcd:tangerine', '#fa62b7']


sns.set(context='notebook', style='ticks', palette=color_pal, font_scale=1.2, 
	rc={'lines.linewidth': 1.75, 'figure.figsize': (9, 6)})
```

## Histograms

Histograms provide numerous insights into a numerical distribution, chiefly the frequency of values. Although they look similar to bar charts, histograms have a distinct purpose. Histograms visualize the frequency of values in a sample of quantitative data, while bar charts compare the values comprising a categorical value. 

<img src="https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/plotly_histogram_fig4.gif" width="750px"/>

[image source](https://plotly.com/chart-studio-help/histogram/#normalizing-a-histogram)

Histograms give you a general sense of:

* How much variability exists in the sample
* Where most of the values lie (e.g. the mode)
* Whether the distribution skews right or left (aka high or low)

### Pandas

`<series>.plot(kind='hist', bins=None)`

Each "bar" in a histogram is called a "bin". The `bins` parameter is optional because the underlying matplotlib function will determine "the best" number of bins to visualize the distribution in question. The plot pulls its color from the color palette we set earlier.

```python
movies['Runtime'].plot(kind='hist')
```

You can change the number of bins to create a smoother shape. Let's also add some descriptive info to our histogram.

```python
movies['Runtime'].plot(kind='hist', bins=50)

# set the title
plt.title('Distribution of Runtime')

# add a label to the x-axis
plt.xlabel('Runtime')

plt.show()
```

### Seaborn

Basic histograms are just as easy with Seaborn's `sns.histplot()`, although there's room to get a little fancier with them. In this course, we won't discuss other types of distributions. For those with more statistical background, you can explore further [here](https://seaborn.pydata.org/tutorial/distributions.html#tutorial-hist).

* `sns.histplot(data, bins='auto', color=None, ax=None)`

For our purposes, simply pass a Series object to the `data` parameter in order to visualize the distribution of a variable. Seaborn will attempt to calculate the ideal number of bins, though you can pass a specific number to the `bins` parameter if you want.

Let's plot the distributions of `imdbRating` and `Rotten Tomatoes` score side by side...

* Like many other Seaborn functions, `sns.histplot()` has an `ax` parameter. This allows you to pass a specific axes object where you want your plot to appear. To gain access to each individual axes object, we have to unpack them into their own variables.
* For the second histogram, we'll pass in a different color to differentiate the variables. Otherwise, each plot would independently pull from the color palette we set earlier.

```python
# Create a 1x2 grid and unpack the axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))

# Add a figure-level title
fig.suptitle('Frequency Distributions for IMDb Rating and Rotten Tomatoes')

# On ax1, plot frequency distribution of audience ratings
sns.histplot(movies['imdbRating'], ax=ax1)

# On ax2, plot frequency distribution of critic ratings in a different color.
sns.histplot(movies['Rotten Tomatoes'], color='#2ecc71', ax=ax2)

plt.show()
```

Just from the shape of these two histograms, we can deduce that, in our sample, critics tend to give more extreme ratings than audiences do!

## Box-and-Whiskers Plots

For a data sample, a box-and-whiskers plot ("box plot" for short) helps you visually quantify the amount of **variability** in your data sample. In other words, if you lined up each data point from a numerical variable in order, variability represents how spread out the points are. The box plot creates a visual summary of just that by leveraging the values of the quartiles in your data sample:

<img src="https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/iqr%3Aboxplot.png" width="750px"/>

[image source](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51)

* The longer the whiskers are, the more variability there is in your sample
* The more narrow the box, the more tightly focused the data points are around the median

### Pandas

The Pandas version of the box plot is simple, but not very pretty.

`<series>.plot(kind='box')`

```python
movies['Runtime'].plot(kind='box')
```

### Seaborn

#### Single Box Plot

`sns.boxplot(x, y, hue=None, data=None, orient=None, color=None, ax=None)`

For many of Seaborn's plotting functions, you separately pass in a dataset to reference and column names from that dataset to use as the plotting variables. That is why `sns.boxplot()` has separate parameters for `x`, `y`, and `data`. 

Let's build a basic box plot for `Runtime` and compare it to the histogram for `Runtime`.

```python
# Create a 1x2 grid and unpack the axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))

# Add a figure-level title
fig.suptitle('Distribution of Movie Runtimes')

# On ax1, create a box plot for Runtime
sns.boxplot(x='Runtime', data=movies, ax=ax1)

# On ax2, create a histogram for Runtime
sns.histplot(movies['Runtime'], ax=ax2)

plt.show()
```

#### Grouped Box Plot w. One Categorical Variable

What if we want to compare the distribution of different groups within a single variable? For example, how does the distribution of `Runtime` compare across languages? 

There are a lot of languages, so first, let's create a subset of the dataframe that includes only the 5 most common languages.

```python
lang_count = movies['Language'].value_counts()
lang_count.head()
```

```python
top_langs = list(lang_count.head().index.values)
top_lang_subset = movies[movies['Language'].isin(top_langs)]
```

When we create the box plot, the `y` parameter takes the categorical variable - `Language`, in our case.

```python
# Create boxplot of Runtime, grouped into Language segments
sns.boxplot(x='Runtime', y='Language', data=top_lang_subset)

# Add a title
plt.title('Distribution of Runtime for Top Movie Languages')
plt.show()
```

#### Grouped Box Plot w. Two Categorical Variables

You can take this one step further by passing a second categorical variable to the `hue` parameter. To illustrate this, we'll create another subset of the data, containing the top 3 languages and top 2 genres. 

```python
genre_count = movies['Genre'].value_counts()
genre_count.head()
```

```python
top_genres = list(genre_count.iloc[:2].index.values)

# take only the top 3 languages for readability in this example
genre_lang_subset = movies[(movies['Language'].isin(top_langs[:3])) &
                           (movies['Genre'].isin(top_genres))]
```

```python
# Create boxplot of Runtime, grouped into Language and Genre segments
sns.boxplot(x='Runtime', y='Language', hue='Genre', data=genre_lang_subset)

# Add a title
plt.title('Distribution of Runtime for Top Movie Languages and Genres')
plt.show()
```

## Bar Charts

Just like pie charts, bar charts visualize a numerical comparison across different categories. Bar charts are always preferable to pie charts because it's harder for people to discern the differences in the areas of the wedges in a pie chart than to compare the height/length of bars. 

### Pandas

`<series>.plot(kind='bar')`

Here's how we would create a bar chart showing the number of movies in each genre:

```python
# Plot a count of movies per genre in a bar chart
movies['Genre'].value_counts().plot(kind='bar')

# Add title
plt.title('Number of Movies by Genre')

# Customize y-axis label
plt.ylabel('Number of Movies')
```

### Seaborn

#### Single Bar Chart Example 1

* `sns.barplot(x, y, hue=None, data=None, estimator=np.mean, ci=95, orient=None, color=None, palette=None, ax=None)`

With the Pandas example above, we had to create the bar chart based off a Series with a specific structure. Each element in the Series corresponded to a bar's label and numerical value. Seaborn's `sns.barplot()` function has some ability to compile the data for you. 

Like other Seaborn functions, you specify the `x` and `y` variables separately. One should be a numeric variable, and the other should be categorical. The `orient` parameter automatically sets itself to `'v'` or `'h'` based on which of the `x` and `y` variables is numeric or categorical. In other words, if you pass the categorical variable to `x`, you get a vertical bar chart. If you pass the categorical variable to `y`, you get a horizontal bar chart. 

Behind the scenes, this is what Seaborn does when you call `sns.barplot()`:

1. Automatically groups the categorical data for you;
2. Applies some calculation to each group based on what mathemtical function you pass to the `estimator` parameter (`np.mean` is the default argument);
3. Plots the resultant values as bars.

Let's say we want to plot the lowest `imdbRating` in each movie `Genre`. Seaborn automatically groups the genres for us. We'd pass `estimator=np.min` to instruct Seaborn to calculate and plot the lowest value in each group.

```python
# In a bar chart, plot the minimum imdbRating in each Genre group
sns.barplot(x='imdbRating', y='Genre', data=movies, 
            estimator=np.min, ci=None)

# Add a title
plt.title('Lowest Movie Rating by Genre')
plt.show()
```

A few notes about the above bar chart:

* If you have a lot of categories, orienting your bar chart horizontally provides better readability.
* Because Seaborn is doing the calculations for you, it also calculates and plots **confidence intervals** in the form of tick marks atop each bar. That's another level of statistical precision that we don't need right now. As such, we pass `ci=None` to remove these.
* Notice that the color palette has changed because the one we defined had fewer colors than this variable has categories (from the `ci` parameter).

#### Single Bar Chart Example 2

Seaborn doesn't always need to leverage the estimator though. If you want to use a calculation that can't be passed to `estimator`, you'll have to do the calculations yourself. Then you'll structure the results so that Seaborn merely needs to plot exactly what it reads out of the object. Because of this lack of calculations, there are also no confidence interval markers on the bars.

Let's recreate the "Number of Movies by Genre" plot we made with Pandas, now using Seaborn. First, we'll prep the data.

```python
genre_count = movies['Genre'].value_counts()
genres = genre_count.reset_index()
genres.rename(columns={'Genre': 'Movies', 'index': 'Genre'}, inplace=True)
genres.head()
```

We reset the index so that we can reference the genre names as a column in the dataframe.

```python
# In a bar chart, plot a count of the movies in each Genre
sns.barplot(x='Movies', y='Genre', data=genres)

# Add a title
plt.title('Number of Movies by Genre')

# Remove the x-axis label
plt.xlabel('')
plt.show()
```

#### Grouped Bar Chart

Just like with boxplots, you can add a second categorical variable into the mix by passing it to the `hue` parameter. In doing so, the grouped bar chart allows you to compare the sub-categories as well as the main categories. This is best explained visually.

In the following example, we'll graph the median `imdbRating` of thriller and horror movies made in the top 3 movie-producing countries. This will ultimately output three groups of two bars each.

First, we'll find the three countries that produce the most movies:

```python
country_count = movies['Country'].value_counts()
top_countries = country_count.head(3).index.values
top_countries
```

Next, we'll create a subset of the data, containing only thriller and horror movies made in one of those countries:

```python
scary = movies[((movies['Genre'] == 'Horror') | (movies['Genre'] == 'Thriller')) &
               (movies['Country'].isin(top_countries))]
```

Now, we'll construct the bar chart. Notice how it automatically generates a legend based on how it compiled the the variable passed to `hue`.

```python
# In a bar chart, plot median imdbRating for each Genre group WITHIN each Country group
sns.barplot(x='Country', y='imdbRating', hue='Genre', data=scary, estimator=np.median, ci=None)

# Add a title
plt.title('Median Rating of Thriller vs. Horror Movies by Country')
plt.show()
```

#### Stacked Bar Chart

In contrast, a stacked bar chart serves to illustrate the proportion of one or more sub-categories within a category. For example, how would we plot the proportion of movies in each of the top 10 genres produced in the U.S.?

First, grab the top 10 most common genres overall:

```python
genre_count = movies['Genre'].value_counts()
genres = genre_count.head(10).reset_index()
genres.rename(columns={'Genre': 'Movies', 'index': 'Genre'}, inplace=True)
genres
```

Next, get a count of U.S.-produced movies in each of those genres:

```python
usa = movies[(movies['Country'] == 'USA') &
             (movies['Genre'].isin(genres['Genre']))]
genres_usa = usa['Genre'].value_counts()
genres_usa = genres_usa.reset_index()
genres_usa.rename(columns={'Genre': 'U.S. Movies', 'index': 'Genre'}, inplace=True)
genres_usa
```

Consolidate these into a single dataframe:

```python
genres['U.S. Movies'] = genres_usa['U.S. Movies']
genres
```

And finally, let's construct this plot. You actually have to layer two bar charts on one axes object. We'll pass a unique `label` to each one and `color`, which will be used to create the figure's legend in a separate command.

```python
# Create a figure with one axes object
fig, ax = plt.subplots()

# In a bar chart, plot the number of movies in each of the top 10 Genres
sns.barplot(x='Movies', y='Genre', data=genres.head(10), label='Total', color='navy')

# In a bar chart, plot the number of U.S.-produced movies in each of the top 10 Genres
sns.barplot(x='U.S. Movies', y='Genre', data=genres.head(10), label='Produced in U.S.', color='dodgerblue')

# Add a title
plt.title('Proportion of Top 10 Movie Genres Made by U.S.')

# Add a legend using the labels passed to each .barplot() function
ax.legend(ncol=2, loc="lower right")

# Remove the x-axis label
plt.xlabel('')
plt.show()
```

## Line Graphs

### Pandas

Line graphs are one of the most common plots because they specifically visualize the trend of a numerical variable over time. In fact, line graphs are the default plot type in the Pandas `.plot()` function.

`<series>.plot()`

Let's prep our data to plot how the average movie ratings have changed YoY (i.e. year over year). To do this, each `Year` is effectively its own group. For each group, we can then find the mean for one or more ratings sources like `imdbRating` and `Rotten Tomatoes`.

```python
# Average critic rating YoY
critics = movies.groupby('Year')['Rotten Tomatoes'].mean()

# Average audience rating YoY
audience = movies.groupby('Year')['imdbRating'].mean()

# Compile both into one dataframe
avg_yrly_ratings = pd.concat([critics, audience], axis=1)
avg_yrly_ratings.round().head()
```

#### One Line

```python
critics.plot()

# Add a title
plt.title('Average Movie Ratings from Critics Over Time')

# Add x- and y-axis labels
plt.xlabel('Year')
plt.ylabel('Rating')
plt.show()
```

#### Multiple Lines

```python
avg_yrly_ratings.plot()

# Add a title
plt.title('Average Movie Ratings Over Time by Source')

# Add x- and y-axis labels
plt.xlabel('Year')
plt.ylabel('Rating')

# Add a legend
ax.legend(('Critics', 'Audience'))
plt.show()
```

### Seaborn

`sns.lineplot(x, y, hue=None, data=None, palette=None, markers=None, estimator=np.mean, ci=95, ax=None)`

Let's repeat these examples using Seaborn. The `sns.lineplot()` function can infer groups and automatically calculate a statistic for each group the same way `sns.barplot()` does, so we don't need the `avg_yrly_ratings` dataframe. Likewise, the default `estimator` argument is also `np.mean`. Since we're going to make use of the `estimator` abstraction, we need to remember to set `ci=None` for the reasons mentioned earlier.

#### One Line

```python
# Build a line graph of mean imdbRating YoY
sns.lineplot(x='Year', y='imdbRating', data=movies, ci=None)

# Add a title
plt.title('Average Audience Movie Ratings Over Time')

# Customize y-axis label
plt.ylabel('Audience Rating')
plt.show()
```

#### Multiple Lines

```python
# Create a figure with one axes object
fig, ax = plt.subplots()

# Plot mean imdbRating YoY
sns.lineplot(x='Year', y='imdbRating', data=movies, ci=None, label='Audience')

# Plot mean Rotten Tomatoes rating YoY
sns.lineplot(x='Year', y='Rotten Tomatoes', data=movies, ci=None, label='Critics')

# Add a title
plt.title('Average Movie Ratings Over Time by Source')

# Customize y-axis label
plt.ylabel('Rating')

# Add a legend using the labels passed to each sns.lineplot() above
ax.legend()
plt.show()
```

## Scatterplots

At its most basic, a scatterplot serves to compare the relationship between two numerical variables. Each point in a scatterplot corresponds to one observation in your sample (e.g. a movie). For each observation, you plot an an (x, y) coordinate using two numerical variables for x and y. 

With scatterplots, you're looking for a general trend in how the values of the y variable change as the values of the x variable increase. However, be careful not to draw conclusions too quickly. Without further statistical analysis, it's hard to make very definitive claims. 

*p.s. There's a LOT more insight scatterplots can offer, but we don't have time to go further into statistics as a class.*

### Pandas

`<series>.plot.scatter(x, y, c=<list of colors>)`

Here's an example, using `imdbRating` for the x variable and `Metascore` for the y variable. (It gets angry if we don't pass a color explicitly to the `c` parameter, so we'll pass one below.) You can see that, generally, `imdbRating` and `Metascore` have some degree of a positive relationship.

```python
movies.plot.scatter(x='imdbRating', y='Metascore', c=['#bb64ed'])
plt.show()
```

In contrast, `Runtime` and `imdbVotes` appear to have little to no connection.

```python
movies.plot.scatter(x='Runtime', y='imdbVotes', c=['#fa62b7'])
plt.ylabel('IMDb Votes in Millions')
plt.show()
```

### Seaborn

`sns.scatterplot(x, y, data=None, ax=None)`

Let's use Seaborn to build a 2x2 grid showing what happens when you flip the x and y variables. This time, we'll compare `imdbVotes` and `imdbRating`, and we'll use a random sample of 20% of the full movie data to make the plot less dense.

```python
# Take a random sample, whose size is 20% of total rows
movies_sample = movies.sample(frac=0.2)

# Create a 1x2 grid of subplots with figure size 15x5
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))

# Add a figure-level title
fig.suptitle('IMDb Votes (in Millions) & IMDb Ratings')

# On ax1, create scatterplot of imdbRating x imdbVotes
sns.scatterplot(x='imdbRating', y='imdbVotes', data=movies_sample, color='dodgerblue', ax=ax1)

# On ax2, create scatterplot of imdbVotes x imdbRating
sns.scatterplot(x='imdbVotes', y='imdbRating', data=movies_sample, color='#2ecc71', ax=ax2)

plt.show()
```

Looking at this side-by-side, we can infer that higher-rated movies tend to get more ratings overall. That *might* mean that people go to IMDb to rate movies they like more often than to give low ratings to movies they hate. This could be a useful starting point to a deeper analysis.

## Key Takeaways

*Note: Parameters with a default argument of None are optional*

**Histogram**

* Purpose: Illustrate the frequency distribution of a numerical variable
* Pandas: `<series>.plot(kind='hist', bins=None)`
* Seaborn: `sns.histplot(a, bins=None, hist=True, kde=True, color=None, ax=None)`

**Box-and-Whiskers Plot**

* Purpose: Highlight the variability in a distribution
* Pandas: `<series>.plot(kind='box')`
* Seaborn: `sns.boxplot(x, y, hue=None, data=None, orient=None, color=None, ax=None)`

**Bar Chart**

* Purpose: Show a numerical comparison across different categories
* Pandas: `<series>.plot(kind='bar')`
* Seaborn: `sns.barplot(x, y, hue=None, data=None, estimator=np.mean, ci=95, orient=None, color=None, palette=None, ax=None)`

**Line Graph**

* Purpose: Show the trend of a numerical variable over time
* Pandas: `<series>.plot()`
* Seaborn: `sns.lineplot(x, y, hue=None, data=None, palette=None, markers=None, estimator=np.mean, ci=95, ax=None)`

**Scatterplot**

* Purpose: Compare the relationship between two numerical variables
* Pandas: `<series>.plot.scatter(x, y)`
* Seaborn: `sns.scatterplot(x, y, hue=None, data=None, estimator=None, ci=95, ax=None)`





