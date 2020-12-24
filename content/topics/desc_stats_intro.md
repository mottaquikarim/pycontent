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

Everyone is familiar with the bell-curve shape of a symmetrical distribution. However, **skewness** indicates whether and how much the values in a sample fall toward one end of the range. 

![positive skew](https://github.com/mottaquikarim/pycontent/blob/master/content/images/right_skew.jpg)

The shape of a skewed distribution depends on outliers, which are extreme observations, both negative and positive.

Images in this section are from https://analystprep.com/


### Measures of Central Tendency

When you look at a histogram, the mound is the "central" region. It represents point where the average, or most typical, values lie in the distribution.

Estimate where the "center" of the data is 

provide info about the typical/average values in a data sample
tendency for values to gather around the middle of the set
>>represents the center point or typical value of a dataset. These measures indicate where most values in a distribution fall and are also referred to as the central location of a distribution. You can think of it as the tendency of data to cluster around a middle value.


show box & whiskers plot
mean
median
mode
iqr


## More Resources

* [Types of Variables](https://statistics.laerd.com/statistical-guides/types-of-variable.php)
