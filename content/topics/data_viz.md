# Data Visualization with Matplotlib & Seaborn

>> https://github.com/mottaquikarim/PYTH2/blob/master/src/Topics/nb/data_viz.ipynb

https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972

http://queirozf.com/entries/pandas-dataframe-groupby-examples#groupby-plot-mean-with-error-bars

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/chart_types.png)


>>groupby plot mean with error bars
http://queirozf.com/entries/pandas-dataframe-groupby-examples#groupby-plot-mean-with-error-bars

In this section, we'll go over example code for different types of common visualizations.

## Review

Below is a brief review of the key points about data visualization & storytelling from the "Data Science Foundations" section.

* Visualizations serve to quickly explain features and conclusions about data to your stakeholders.
* As such, they should be *simple*, *uncluttered*, and *clearly labeled*. Less is more.
* Visual considerations include position, color, order, & size.
* The best visualizations tell a story about the data by illustrating key points supporting your thesis and conclusions.
* Most importantly, *consider your audience* when crafting your story.
* The chart type you select should accurately represent the variables you are pulling from data in a way that is clearly readable for your audience.

<img src="../images/plot_elements.png" style="margin: 0 auto; float: right;"/>

## Which Charts Say What?

Choosing the right chart to visualize parts of your data is somewhat subjective. It hinges mainly on:
* The type of data you have
* The message you're trying to convey

**The goal is always to convey your message in the clearest, cleanest way possible.** For reference here is a breakdown of which charts are commonly used to illustrate different statements and/or relationships:


>>https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
>>https://seaborn.pydata.org/tutorial.html

### 



### Correlation


### Composition

Bar chart
Waffle chart
Pie charts* not recommended because it's hard to register the size of the differences
Treemap


## Foundations of Matplotlib & Seaborn

```python
import numpy as np
import pandas pd
from scipy import stats

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print('import successful')
```


## Line Graphs
==- change over time; continuous not discrete
When thinking about using a line chart consider:
- How many lines you'll need on your graph, the more overlapping lines there are, the harder your chart will be to read.
- Consider how many colors you need to use for your lines. Giving each line its own color forces the viewer to scan back and forth from the key to the graph.
- Individual data points can be hard to read, but line charts are good for showing overall trends.==

## Area Charts


## Categorical Comparison

## Bar Charts
- times series data, but discrete not continuous like line graphs

### Vertical

### Horizontal

### Grouped

### Stacked

#### Pie Charts

==As you can see from this example pie charts can be effective for proportions or percentages.When thinking about using a pie chart consider:
- The more variables you have, as in the more slices of your pie you'll have, the harder it is to read.
- Area is _very_ difficult for the eye to read, so if any of your wedges are similarly sized think about a different chart type.
- If you want to compare data, leave it to bars or stacked bars. If your viewer has to work to translate pie wedges into relevant data or compare pie charts to one another, the key points you're trying to convey might go unnoticed.==

## Scatterplots
==frequency & distribution
correlation when you draw a line through it...
Scatterplots are great for data dense visualizations and clusters. They are most effective for trends, concentrations, and outliers. They can be especially useful to see what you want to investigate further.
When thinking about using a scatter plot consider:
- This chart type is not as common so can me more difficult for an audience to read.
- If dots are covering up each other, consider a different chart type.
- A bubble chart is one variation on the scatter plot.
- Scatter plots are a great way to give you a sense of trends, concentrations, and outliers, and are great to use while exploring your data. This will provide a clear idea of what you may want to investigate further.==

### Bubble Charts?????

## Histograms

- Effective for distribution across groups.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/histogram.png)

- Histograms are useful when you want to see how your data are distributed across groups. Important: histograms are not the same thing as a bar chart! Histograms look similar to bar charts, but with bar charts, each column represents a group defined by a categorical variable; and with histograms, each column represents a group defined by a continuous, quantitative variable.
- One implication of this distinction: with a histogram, it can be appropriate to talk about the the tendency of the observations to fall more on the low end or the high end of the X axis.
- With bar charts, however, the X axis does not have a low end or a high end; because the labels on the X axis are categorical - not quantitative.

## Bar Chart vs Histogram

The main difference between a bar chart and histogram is that histograms are used to show distributions of variables while bar charts are used to _compare_ variables.




## Box & Whiskers Plot

sns.boxplot(x='diagnosis', y='area_mean', data=df)


## Linear Regression






## Resources

* [44 Types of Graphs](https://visme.co/blog/types-of-graphs/)
* [8 Tips for Great Data Viz](https://www.gooddata.com/blog/8-ways-turn-good-data-great-visualizations)
* [Python Graph Gallery](https://python-graph-gallery.com/)
* [Data to Viz Interactive Diagram](https://www.data-to-viz.com/#explore)
* [How to Set a Color w. Matplotlib](https://python-graph-gallery.com/196-select-one-color-with-matplotlib/)
* [Python Colors & Color Palettes](https://python-graph-gallery.com/python-colors/)
* [Data to Viz Visualization Style Tips](https://www.data-to-viz.com/caveats.html)
