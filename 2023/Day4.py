import os
import sys
from pprint import pprint as print

with open(os.path.join(sys.path[0], 'Day4input.txt'), 'r') as file:
    data = file.read()

# Part 1

import pandas as pd
import numpy as np

rows = data.split("\n")[:-1]
cards = [row.split("|")[0] for row in rows]
cards = [s.replace('Card', '') for s in cards]
cards = [s.replace(':', '') for s in cards]
cards = [s.strip() for s in cards]
cards = [' '.join(s.split()) for s in cards]
# cards = pd.DataFrame(cards)
# cards.columns = cards.iloc[0]
# cards = cards.iloc[1:]


win_nums = [row.split("|")[1] for row in rows]
win_nums = [row.split() for row in win_nums]
# win_nums = pd.DataFrame(win_nums)
# win_nums.columns = win_nums.iloc[0]

results = []
for index, value in enumerate(cards):
    results.append(set(value).intersection(set(win_nums[index])))

counts = [len(s) for s in results]

def counts_to_score(num):
    if num > 0:
        i = 1
    else:
        i = 0
    for x in range(num):
        i = i*i
    return i

score = [counts_to_score(x) for x in counts]

print(f"Part 1 Score: {sum(score)}")

# WIP - score too low...
