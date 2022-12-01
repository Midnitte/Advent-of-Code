import pandas as pd
import os, sys

with open(os.path.join(sys.path[0], 'Day3input.txt'), 'r') as file:
    data = file.read()
data = data.split('\n')[:-1]
df = pd.DataFrame([list(e) for e in data])

#Part 1

gamma = df.mode('index').values[:1]
gamma = [''.join(ele) for ele in gamma]
gamma = gamma[0]

epsilon = ''.join(['1' if i == '0' else '0' for i in gamma]) # Convert to the "anti-mode"

power = int(epsilon, 2) * int(gamma, 2)

print(power)

# Part 2
df.columns = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']


# TODO: Refactor into something more pythonic...
mode_1 = [item[0] for item in df.mode('index').values][0]

step1 = df[df['One'] == mode_1]


# Need to filter DF first, before moving to next step...
mode_2 = [item[1] for item in df.mode('index').values][0]
step2 = df[df['Two'] == mode_2]

mode_3 = [item[2] for item in df.mode('index').values][0]
step3 = df[df['Three'] == mode_3]

mode_4 = [item[3] for item in df.mode('index').values][0]
step4 = df[df['Four'] == mode_4]

mode_4 = [item[3] for item in df.mode('index').values][0]
step4 = df[df['Four'] == mode_4]
