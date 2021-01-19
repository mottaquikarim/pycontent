# EDA (Exploratory Data Analysis)

## Objectives

>>* Exploding
>>* Joining/Merging 
* Basic Descriptive Statistics
* Groupby Statements
* Key Takeaways

### Import Libraries & Load Data

```python
import pandas as pd
import numpy as np
from scipy import stats
print('import successful')
```

Load the data with `imdbID` as the index and make a copy.

```python
omdb_orig = pd.read_csv('omdb4500_eda.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```


