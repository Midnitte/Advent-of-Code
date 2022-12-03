import pandas as pd
import os, sys

with open(os.path.join(sys.path[0], 'Day2input.txt'), 'r') as file:
    data = file.read()
data = pd.DataFrame(list(x.split()) for x in data.split('\n'))
data.columns = ['0', '1']
data.dropna(how='all', inplace=True)
print(data)

score = 0
# Part 1

# A - Rock - X (1)
# B - Paper - Y (2)
# C - Scissors - Z (3)

# Win: 6
# Lose: 0
# Tie: 3
for index, row in data.iterrows():
    if row["0"] == 'A':  # Rock
        if row["1"] == 'Y':  # Paper
            score = score + 2 + 6
        elif row['1'] == 'X':  # Rock
            score = score + 1 + 3
        else:  # Scissors
            score = score + 3 + 0
    elif row["0"] == 'B':  # Paper
        if row["1"] == 'Y':  # Paper
            score = score + 2 + 3
        elif row['1'] == 'X':  # Rock
            score = score + 1 + 0
        else:  # Scissors
            score = score + 3 + 6
    else:  # Scissors
        if row["1"] == 'Y':  # Paper
            score = score + 2 + 0
        elif row['1'] == 'X':  # Rock
            score = score + 1 + 6
        else:  # Scissors 
            score = score + 3 + 3

print(score)

# Part 2

# X - lose - 0
# Y - draw - 3
# Z - win - 6

# A - Rock - (1)
# B - Paper - (2)
# C - Scissors - (3)
score = 0
for index, row in data.iterrows():
    if row["0"] == 'A':  # Rock
        if row["1"] == 'Y': 
            score = score + 1 + 3
        elif row['1'] == 'X': 
            score = score + 3 + 0
        else:
            score = score + 2 + 6
    elif row["0"] == 'B':  # Paper
        if row["1"] == 'Y':
            score = score + 2 + 3
        elif row['1'] == 'X':
            score = score + 1 + 0
        else:
            score = score + 3 + 6
    else:  # Scissors
        if row["1"] == 'Y':
            score = score + 3 + 3
        elif row['1'] == 'X': 
            score = score + 2 + 0
        else: 
            score = score + 1 + 6

print(score)