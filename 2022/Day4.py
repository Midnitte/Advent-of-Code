import os, sys
from pprint import pprint

with open(os.path.join(sys.path[0], 'Day4input.txt'), 'r') as file:
    data = file.read()

# def f(s):
#     return sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))]))
#          if '-' in i else [int(i)]) for i in s.split(',')), [])

# data_list = data.split()
# data_list = [entry.split(",") for entry in data_list]
# data_list = [f(value) for entry in data_list for value in entry]

# count = 0
# for i, j in enumerate(data_list[:-1]):
#     if set(j).issubset(data_list[i+1]):
#         count += 1
#     elif set(data_list[i+1]).issubset(j):
#         count += 1

# print(count)
list_of_vals = [line.split(",") for line in data.split("\n") if line.split(",") != ['']]
#print(list_of_vals)

def split_to_range(l):
    list_vals = l
    for x, y in enumerate(list_of_vals):
        for i, s in enumerate(x):
            values = s.split("-")
            values = [int(v) for v in values]
            list_vals[x[i]] = list(range(values[0], values[1]+1))

    return list_vals

print(split_to_range(list_of_vals))


