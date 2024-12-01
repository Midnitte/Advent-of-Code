# Part 1
from pathlib import Path
from pprint import pprint as print

path = Path.cwd() / "2024/Day1input.txt"
content = path.read_text(encoding="utf-8")

firstColumn = sorted([int(line.split()[0]) for line in content.splitlines() if line.strip()])
secondColumn = sorted([int(line.split()[1]) for line in content.splitlines() if line.strip()])

def distanceCalc(r1, r2):
    return abs(r1-r2)

total = 0
for index, _ in enumerate(firstColumn):
    total += distanceCalc(firstColumn[index], secondColumn[index])


print(f'Distance Total: {total}')

# Part 2
## Similarity Scores

def simScore(r1, r2):
    return r1 * r2.count(r1)

similarScore = 0
for index, _ in enumerate(firstColumn):
    similarScore += simScore(firstColumn[index], secondColumn)

print(f'Similarity Score: {similarScore}')
