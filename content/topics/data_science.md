# Principles of Data Science

## The What, Why, & Who of Data Science

Whether or not they realize, most people have come into contact with data science in their daily lives. We've seen trending articles on digital news outlets, personalized product recommendations from online stores, and advertisments that seemingly hear our every thought and conversation. But what exactly *is* data science?

#### WHAT
* Acquiring, organizing, and delivering complex data
* Building and deploying machine learning models
* Conducting statistical analyses, including ANOVA, linear models, regression analysis, and hypothesis tests
* Visualizing data distributions, hierarchical clustering, histograms, pie and bar charts, etc.

#### WHY
* Identify hidden patterns, correlations, and outliers to glean meaningful insights.
* Based on these insights, validate assumptions, make predictions, define optimizations, and most importantly make strategic decisions.

#### WHO
Professionals who practice data science for businesses, government institutions, nonprofits, and other organizations might have one of these titles:

* **Machine Learning Engineer**:
	* Work in production code.
	* Identify machine learning applications.
	* Manage infrastructure and data pipelines
* **Data Engineer**:
	* Create an architecture that facilitates data acquisition and machine learning problems at scale.
	* Focus on the algorithm and the analysis rather than the software.
* **Research Scienctist**:
	* Specialized research scientist focused on driving scientific discovery rather than pursuing industrial applications.
	* Backgrounds in both data science and computer science.
	* Determines new algorithmic optimizations, especially in the realm of AI.
* **Advanced Analyst**:
	* Apply descriptive and inferential exploratory data analysis and modeling.

## Applications of Data Science 

Effective data science lives at the intersection of...

<img src="https://4.bp.blogspot.com/-0cbXveb1J_0/V-FtjJZ4rqI/AAAAAAAAMHM/bS32Pio2a1IFOyp5T86S0jiyB-3KAN1iwCEw/s1600/download%2B%25281%2529.png" style="margin: 0 auto; width: 60%; display: block;"/>

That's pretty broad though. What skills in each of these areas are needed for data science specifically? A good data scientist:

* **MATHEMATICS**: Understands statistical concepts and modeling; proficient in R and/or Python
* **COMPUTER SCIENCE**: Has experience in data engineering (i.e. organizing data, running models, visualizing results, etc.); proficient in R and/or Python
* **DOMAIN EXPERTISE**: Understands the business and social context of issue and can ask questions that lead to appropriate approaches and insights

### DISCUSSION: What are some real-world scenarios where people might use data science to solve a problem?

1) **Safer, smarter self-driving cars**
	- Data from sensors, including radars, cameras and lasers, to create a map of its surroundings. 
	- Create a map of its current surroundings such as proximity to other moving or stationary objects like other vehicles, traffic light signals, sirens, pedestrian crosswalk signals, etc.
	- Decisions like when to speed up/down, stop, turn, signal, etc.
2) **Pre-emptive code alerts in the ER**
	- Data from heart monitors, pulse oximeter, arterial lines, ventilators, etc. hooked to patients
	- Find commonalities in biological health indicators preceding a code
	- Identify patients at risk of imminently coding to give doctors an early warning and increase chances of patient revival
3) **Natural disaster prediction**
	- Data from ships, aircrafts, radars, satellites
	- Predict occurrences of natural disasters, the areas to be affected, and (where applicable) the path of the storm
	- Earlier predictions to maximize evacuation potential

## The Data Science Lifecycle

<img src="http://sudeep.co/images/post_images/2018-02-09-Understanding-the-Data-Science-Lifecycle/chart.png" style="margin: 0 auto; width: 100%; display: block;"/>

*Image Source: http://sudeep.co/data-science/Understanding-the-Data-Science-Lifecycle/*

The image above delineates the general steps you would take when you start a data science project. Of course, they're really guidelines because you have to let your results guide you. Sometimes you might skip a step, repeat certain steps, or restart the entire cycle when trying to answer a question.

### 1) BUSINESS UNDERSTANDING

First and foremost, you have to understand your problem:

* Why is it a problem?
* Who is affected by this problem and how?
* Can you quantify the problem and/or its consequences? ("Consequences" might simply be opportunity cost in some cases.)
* What theories do you have about what is causing your problem?
* What ideas do you have about solving your problem?
* How valuable would solving this problem be to each stakeholders and to the group as a whole?
* What kind of data might you want to explore?
* What data is available to you or can you gain access to?

### 2) DATA MINING

This step mainly concerns obtaining the data. You'll have a number of items to consider, including:

* Is there a single source that contains all the data variables you need, or will you have to compile data from different sources?
* Do you have first-party data relating to this problem?
* Is your first-party data enough to help you solve the problem, or do you need to complement it with third-party data?
* Is the data publicly available (and thus available to your competitors, if applicable)?
* Will you need to pay for the data and/or negotiate how much access you will be allowed?
* If you're compiling data from multiple sources, can you accurately align them?

This last point is of crucial importance. You must use contextual logic when compiling variables. For example, you can't evaluate how the weather affects Citibike usage if you compare Citibike rides from 2018 to weather from 2016. You also can't confidently predict a country's employment rate based solely on its GDP. Your sample space of countries has far too many extraneous variables that need to be accounted for, such as their domestically available natural resources, their wealth gap, their population's age distribution, etc.

### 3) DATA CLEANING

Data cleaning is a relatively straightforward phase. During it, your aim is to:

* Standardize data formatting
	* e.g. If states are formatted in different ways ("New York", "NY", and "N.Y."), you should convert them to be consistent
* Remove duplicate data and/or entries containing "NULL" values to avoid unintentionally skewing results
* Remove extreme outliers so that these edge cases don't skew your results.
* Normalize units across variables
	* e.g. Ensure all units use the metric system
* Normalize the scale of variable data to allow for smooth visualizations
* Create dummy variables for categorical vars as a way to quantify your qualitative data

### 4) DATA EXPLORATION

At this point, we want to gain a deeper understanding of the dataset's details and create some meaning to help determine our path forward. This exploration might include (but is certainly not limited to!) the following: 

* Observe descriptive statistics, probably starting with summary statistics for the different variables in the dataset.
* If our goal is to build a confident predictive model, we would start by looking for signs of strong correlation between variables.
* If our goal is to conduct a sentiment analysis, we might evaluate which parts of the data could serve to measure positive and negative sentiments.

As you gain more context about the relationships in the data, you will think of more theories about your problem.

### 5) FEATURE ENGINEERING

This step is where we transition from merely describing and summarizing the data to manipulating and analyzing it. This step always starts with the same question - *What else do you want to know about the dataset?* The answers to this usually pertain to some pre-existing assumption, ostensible relationships (or lack thereof), unexpected values, or anomalies, which you want to investigate further. 

**NOTE!** It is common for this step to reinforce and revisit the prior step as we discover anomalies or intriguing relationships.

### 6) PREDICTIVE MODELING

This is where the magic happens. We won't get into the details of machine learning here. However, the model you create for any data science project will be core source of insights and conclusions. Once you have results, it's time to dig in and think outside the box! Ask yourself questions like: 

* How do our results compare to our initial hypothesis?
* How statistically significant (i.e. accurate) are our predictions?
* Do we have enough information to draw decisive conclusions? If so, what are they?
* Based on our conclusions, what concrete actions do we recommend?

Remember that your results might not be sufficient after only one iteration. They might point you in the right direction, but they won't necessarily answer all your questions sufficiently. You'll probably have to repeat parts of the cycle several times before you can confidently draw conclusions and make recommendations.

### 7) DATA VISUALIZATION (& Data Storytelling)

The single most important takeaway from this walk-through is this - *the value of your results depends directly on how well key stakeholders understand them!* Data science is valuable because of the insights we can discover using it. You can have all the mathematical evidence in the world for those insights, but your stakeholders have to understand their contextual significance and believe they can turn them into strategic, impactful business actions. Otherwise, what value do those insights have?

Now, a data scientist might not present results to clients or high-level managers, but you *do* need to be able to explain results to team members who are not expert data scientists. 

This where the ubiquitous buzz phrase **data storytelling** comes into play. The goal of data storytelling is to convey your message in a way that provokes thoughts and ideas, inspires questions, encourages conversation and brainstorming, and ultimately, ignites action. All this boils down to two core pillars:

1. Honing a cohesive narrative that establishes a thesis
2. Highlighting meaningful key metrics as evidence to support that thesis

Data vizualization is key to this endeavor because it's the easiest way to boil down heaps and mounds of numerical data into a clear message. That As the saying goes, a picture can say a thousand words!

#### Tips for Quality Data Viz

* Focus the message on a central theme. Ensure Your visualizations should aid the progression of your message appropriately.
	* Display the visualization at the appropriate point in your story.
	* If you have more than one visualization in view at a time, position each one contextually, according to natural reading eye movement.
* Some attributes affect our brain more strongly. In order of focus:
	* Position
	* Color
	* Size
* Do not use color for decorative or non-informational purposes. It should be used to highlight key metrics or data points that help support your message.
* Most importantly, *avoid visual clutter like the plague!*
	* Eliminate the legend if it will not detract from understanding.
	* Where you have long, vertical x-axis labels, try flipping the chart if possible.
	* Remove excessive boxes or lines that separate data.
	* Don't graph too many variables in one chart. For instance, ten lines on one chart will be too convoluted to follow!

**HOWEVER, there's always one exception!** Generally, "less is more" surpasses everything else in importance *except for "consider your audience".* You always want to minimize the amount of text on your visualization, but "the minimum" differs based on how much context your audience has. Ultimately, you need to make sure every viewer has enough context to be grounded in the appropriate frame of reference.

If you want, you can see browse through a lot more tips on [Data to Viz's "Caveats" page](https://www.data-to-viz.com/caveats.html).

## Python Tools for Data Science

Now that we understand the process we'll follow, we can jump into applying it with our Python skills. First, we have to set up our environments and ensure we have all the tools we need to conduct a thorough data science analysis. We won't use all of these in this introductory class, but these are the most common across the industry.

* **NumPy** for computational operations on large multi-dimensional arrays and matrices
* **Pandas** for data structuring, manipulation, and analysis
* **Matplotlib** & **Seaborn** for data visualization
* **Scikit-learn** for machine learning
* **Scrapy** for data wrangling via web scraping
* **Jupyter Notebooks** & **Jupyter Lab** for data science integrated development environments (IDEs)