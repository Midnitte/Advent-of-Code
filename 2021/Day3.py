import pandas as pd
import os, sys

with open(os.path.join(sys.path[0], 'Day3input.txt'), 'r') as file:
    data = file.read()
data = data.split('\n')[:-1]
df = pd.DataFrame([list(e) for e in data])

gamma = df.mode('index').values[:1]
gamma = [''.join(ele) for ele in gamma]
gamma = gamma[0]

epsilon = ''.join(['1' if i == '0' else '0' for i in gamma]) # Convert to the "anti-mode"

power = int(epsilon, 2) * int(gamma, 2)

print(power)
