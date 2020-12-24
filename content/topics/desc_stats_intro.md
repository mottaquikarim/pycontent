# An Abridged Intro to Descriptive Statistics

## Overview of Topics

* Summary & Descriptive Statistics
* Definition of a "Variable"
* Distributions & Histograms

>> Measures of Central Tendency
>> Measures of Variability (Spread)
>> Measuring Asymmetry
	>> skewness important bc stats requires vars to be 
>>Measuring Frequency

## Summary & Descriptive Statistics

We'll start by defining some basic stats terms. When speaking about data, a **population** encompasses the *entire* set of items you're interested in, while a **sample** consists of a subset of those items. This is analagous to the difference between all the movies ever made (population) and the movies in our OMDb dataset (sample). Obtaining data on complete populations usually isn't feasible, so most statistical analyses are based on samples.

The heart of every quantitative analysis lies in the data's **descriptive statistics.** Descriptive statistics briefly summarize the data to help understand its makeup and organization.

### What is a "Variable"?

A variable is some measure - either quantitative (numerical) or qualitative (categorical) - related to an entity. When analyzing movies, "imdbRating" is a numerical variable and "Genre" is a categorical variable. Sometimes, a variable's type might seem counterintuitive. For example, the "Year" a movie was released is a categorical variable despite the fact that it's a number.

## Distributions & Histograms

In descriptive statistics, we often talk about a variable's **distribution**. It's easiest to explain distributions by looking at a histogram. Generally speaking, **histograms** represent "how frequently or infrequently certain values occur in a given set of data." In other words, a histogram *visualizes a variable's distribution*.

>><!--<img src="https://plot.ly/static/img/literacy/fig5.gif" style="margin: 0 auto; width:60%"/>
	*Image from Plotly: https://help.plot.ly/histogram/#what-is-a-histogram*-->

Histograms often accompany discussion of distributions because they help provide visual context about a certain metric's relation to the dataset as a whole. 

### Symmetry & Skewness

Everyone is familiar with the bell-curve shape of a symmetrical distribution. However, **skewness** indicates whether and how much the values in a sample fall toward one end of the range. Whether a distribution is skewed depends on the outliers within the sample. Skewness can be roughly evaluated visually by looking at a distribution's histogram. 

As a baseline, this distribution has **no skew**:

![no skew](https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/no_skew.jpg)

A positively skewed distribution has outliers on the higher end of its range. The righthand "tail" on the histogram illustrates this.

**Positive Skew** 

![positive skew](https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/right_skew.jpg)

Conversely, a negatively skewed distribution has outliers on the lower end of its range. The lefthand "tail" on the histogram illustrates this.

**Negative Skew** 

![negative skew](https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/left_skew.jpg)

The magnitude of a distribution's skewness can be calculated as a positive or negative number. The greater the absolute value of this metric is, the more positively or negatively skewed the distribution is.

*Images in this section are from https://analystprep.com/*

### Measures of Central Tendency

When you look at a histogram, the mound is the "central" region. It represents where the average, or most typical, values in the distribution lie. The main measures for this are the mean, median, and mode.

* **`s.mean()`** -- the simple average; 
    * *Downside is that it's greatly affected by outliers in the data!*
* **`s.median()`** -- in a lineup of ordinal data, the median is the middle number or category
* **`s.mode()`** -- the number or category that occurs most often in the dataset
    * Notice that even if this only returns one value, it returns a Series object

**Positive Skew** 

![positive skew](https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/right_skew_central_tendency.jpg)

Conversely, a negatively skewed distribution has outliers on the lower end of its range. The lefthand "tail" on the histogram illustrates this.

**Negative Skew** 

![negative skew](https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/images/left_skew_central_tendency.jpg)


## More Resources

* [Types of Variables](https://statistics.laerd.com/statistical-guides/types-of-variable.php)
