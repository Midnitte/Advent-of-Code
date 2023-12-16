import os
import sys
from pprint import pprint as print

with open(os.path.join(sys.path[0], 'Day2input.txt'), 'r') as file:
    data = file.read()

# Part 1
import re
import pandas as pd

game_data = data.split("\n")
del game_data[-1]

pattern = r"(?=(\d+))"

game_list = []

for row in game_data:
    game_list.append(re.findall(pattern, row))

game_df = pd.DataFrame(game_list)

# WIP: Doesn't account for order of color inputs...
