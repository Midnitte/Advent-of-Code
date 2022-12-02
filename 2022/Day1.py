import pandas as pd
import os, sys

with open(os.path.join(sys.path[0], 'Day1input.txt'), 'r') as file:
    data = file.read()

# Part 1
data = data.split('\n\n')

data = [list(x.split()) for x in data]

data = pd.DataFrame(data)
data = data.astype(float)
data['Sum'] = data.sum(axis=1, numeric_only=True)
print(data['Sum'].nlargest(n=1))

# Part 2
print(sum(data['Sum'].nlargest(n=3)))
