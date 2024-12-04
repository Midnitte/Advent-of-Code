# Part 1
from pathlib import Path
#from pprint import pprint as print
import re

path = Path.cwd() / "2024/Day3input.txt"
content = path.read_text(encoding="utf-8")


pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern=pattern, string=content)

results = sum([int(x) * int(y) for x, y in matches])

print(f'Part One: {results}')

# Part 2

# WIP