# IE Pandas
---

This is Team C's final project in Advanced Python.

A simple implementation of dataframe functionality

The library is available in [Pypi](https://pypi.org/project/ie_pandas/)

### Installing
---


The easiest way to install ie_pandas is through ```pip```

```python
pip install ie_pandas
```

To use it in your project, you must first import the library

```python
from ie_pandas import Dataframe
```

You can create a frame by the following 4 methods:
* A list of lists
* A numpy array of lists
* A dictionary of lists with keys being column names and values being the values for that column
* A dictionary of numpy arrays (same as with lists)

```python
dictionary = {'c0': [1, 3, 5], 'c1': [7, 6, 2], 'c2': [2, 4, 7], 'c3': [5, 3, 9]}
df = DataFrame(dictionary)
```
#### Functionality
* Create dataframes from list of lists, numpy arrays, dictionaries of lists and numpy arrays
```python
dictionary = {'c0': [1, 3, 5], 'c1': [7, 6, 2], 'c2': [2, 4, 7], 'c3': [5, 3, 9]}
df = DataFrame(dictionary)

# You may optionally pass along two parameters, cols and index
# cols determines the column names (if blank they will be numerical strings)
# index determines the row names (if blank they will be numbers)
df = DataFrame(dictionary, cols = ["col0", "col1", "col2", "col3"], index = ["row1", "row2", "row3"])
```
* Access columns by name
```python
df['column_1']
```
* Access rows by position or by row name
```python
df.get_index(1)
# or
df.get_index('row_1')
```
* Access data like a numpy array by name
```python
df[0:2, 1:3]
```
* Modify dataframe
```python
df[0,0] = 3
```
* Sum, median, mean, min, max methods (only work for numerical columns)
```python
df.mean()
```

Since the underlying object of the dataframe is a numpy array, you may perform aditional functionality like
```python
df[:, 1:2].sum()
```

#### Dependencies

IE_Pandas only requires the following packages:
* Numpy (>=1.16)

However, for development purposes, the following packages are needed:
* Pytest (>= 4.2)
* Pytest-cov (>= 2.6)
* Black (for PEP8 compliance)

### Development
---
For development purposes, you may download the files directly and install the library locally by placing your terminal in the downloaded folder and doing

```python
pip install --editable .[dev]
```

Then, to execute the tests you just need to run

```python
pytest --cov
```

### IE_Pandas Coding Style
---
IE_Pandas complies to PEP8 and uses ```black``` for coding standards

### Versioning
---
[SemVer](http://semver.org/) is used for versioning. 

### License
---
This project is licensed under the MIT License - see the [License](license.txt) file for details