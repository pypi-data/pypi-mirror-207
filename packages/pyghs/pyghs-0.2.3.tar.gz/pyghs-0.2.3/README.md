# GHS

Storage csv file in github repository.

## Installation

```bash
pip install pyghs
```

## Usage

```python
from ghs import GHS
import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

# Create a GHS instance
ghs = GHS("YOUR_GITHUB_REPOSITORY", "YOUR_GITHUB_TOKEN")
# Create a csv file in github repository
ghs.create("test.csv", df)

# Get a csv file from github repository
df = ghs.get("test.csv")
print(df)
```

This prints:

```bash
   a  b
0  1  4
1  2  5
2  3  6
```
