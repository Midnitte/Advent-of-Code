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

# Part 2
import re


match_pat = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
new_results = []


for line in data_list:
    new_results.append([match.group(1) for match in re.finditer(match_pat, line)])


num_dict = {"one": "1","two": "2","three": "3", "four": "4", "five": "5",\
             "six": "6", "seven": "7", "eight": "8", "nine": "9"}
converted_result = []

for index, result in enumerate(new_results):
    for idx, num in enumerate(result):
        if num.isdigit():
            pass
        else:
            new_results[index][idx] = num_dict[num]
    
    converted_result.append(int(result[0] + result[-1]))
print(f"Part Two Result: {sum(converted_result)}")

