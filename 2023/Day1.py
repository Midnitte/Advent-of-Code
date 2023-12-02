"""On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number."""

import os
import sys
from pprint import pprint as print

with open(os.path.join(sys.path[0], 'Day1input.txt'), 'r') as file:
    data = file.read()

# Part 1
data_list = data.split("\n")
del data_list[-1]
results = []

for line in data_list:
    line_nums = [x for x in line if x.isdigit()]
    result = (line_nums[0] + line_nums[-1])
    results.append(int(result))

print(f"Part One Result: {sum(results)}")

