# Data Cleaning

## Objectives


check = pd.read_csv('omdb4500_cleaning.csv', index_col='imdbID')
check.head()


```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

print('import successful')
```

Now, load the data and make a copy. We'll also set "imdbID" as the custom index like we did in the last section, but this time we'll do it by passing it into `.read_csv()`'s `index_col` parameter.

```python
omdb_orig = pd.read_csv('https://raw.githubusercontent.com/mottaquikarim/pycontent/master/content/raw_data/omdb4500_cleaning.csv', index_col='imdbID')
movies = omdb_orig.copy()
print('data loaded successfully')
```