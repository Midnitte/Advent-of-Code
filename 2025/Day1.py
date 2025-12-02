from pathlib import Path
from pprint import pprint as print

# path = Path.cwd() / "2025/Day1input.txt"
# content = path.read_text(encoding="utf-8")
content = "L68\nL30\nR48\nL5\nR6\nL5\nL1\nL99\nR14\nL82"

directions = [line[0] for line in content.splitlines()]
magnitudes = [int(line[1:]) for line in content.splitlines()]

results = [50]

for id, result in enumerate(directions):
    if result == "R":
        results.append(results[-1] + magnitudes[id])
    else:
        results.append(results[-1] - magnitudes[id])

print(results.count(0))