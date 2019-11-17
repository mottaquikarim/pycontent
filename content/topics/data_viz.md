# Data Visualization with Matplotlib & Seaborn

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/chart_types.png)

In this section, we'll go over example code for different types of common visualizations.

==We'll use this dataset!!!!!!!!!!!!!! TBD??????????????==

## Review

Below is a brief review of the key points about data visualization & storytelling from the "Data Science Foundations" section.

* Visualizations serve to quickly explain features and conclusions about data to your stakeholders.
* As such, they should be *simple*, *uncluttered*, and *clearly labeled*. Less is more.
* The best visualizations tell a story about the data by illustrating key points supporting your thesis and conclusions.
* Most importantly, *consider your audience* when crafting your story.

## Foundations of Matplotlib & Seaborn 


==Choosing the right chart for your data is subjective. There are pros and cons to each. Choosing a chart type depends firstly on the data you have. Secondly, it depends on the clearest way to convey your message. The alignment of these two aspects will help you decide what type of visualization to use.
- The chart type you select should accurately represent the variables you are pulling from data in a way that is clearly readable for your audience.
- Visual considerations include: position, color, order, size. 
- With data visualizations becoming increasingly popular, a clean and clear chart goes a long way in conveying a message from a data set.==

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




## Linear Regression






## Resources

* [44 Types of Graphs](https://visme.co/blog/types-of-graphs/)
* [8 Tips for Great Data Viz](https://www.gooddata.com/blog/8-ways-turn-good-data-great-visualizations)
* [Python Graph Gallery](https://python-graph-gallery.com/)
* [Data to Viz Interactive Diagram](https://www.data-to-viz.com/#explore)
* [How to Set a Color w. Matplotlib](https://python-graph-gallery.com/196-select-one-color-with-matplotlib/)
* [Python Colors & Color Palettes](https://python-graph-gallery.com/python-colors/)
* [Data to Viz Visualization Style Tips](https://www.data-to-viz.com/caveats.html)
