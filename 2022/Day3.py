import pandas as pd
import os, sys

with open(os.path.join(sys.path[0], 'Day3input.txt'), 'r') as file:
    data = file.read()



# df = pd.DataFrame(data=data.split(), columns=['Raw'])

# def splitdf(s):
#     half, rem = divmod(len(s), 2)

#     return pd.Series(s[:half + rem]), pd.Series(s[half + rem:])

# split_df = df['Raw'].apply(splitdf)

# print(split_df)

left =[]
right = []


for line in data.splitlines():
    half, rem = divmod(len(line), 2)
    left.append(line[:half + rem])
    right.append(line[half + rem:])

diction = {'Left':left,'Right':right}

df = pd.DataFrame(diction)



df['Common'] = df.apply(lambda df: set(df['Left']).intersection(df['Right']).pop(), axis=1)

print(df)



LETTER_VALUES = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, \
            'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
    }
# Part 1 answer
print(sum(LETTER_VALUES[l] for l in df['Common']))