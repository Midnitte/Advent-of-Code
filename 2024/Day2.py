# Part 1
from pathlib import Path
from pprint import pprint as print
import timeit

path = Path.cwd() / "2024/Day2input.txt"
content = path.read_text(encoding="utf-8")


def has_consecutive_repeating_chars(s):
    s = s.split()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def isnt_large_diff(s):
    s = s.split()
    for i in range(len(s) - 1):
        if (abs(int(s[i]) - int(s[i+1])) > 3) & (abs(int(s[i]) - int(s[i+1])) < 1):
            pass
    return True


def is_line_sorted(s):
    if line == ' '.join(sorted(line.split())):
        return True
    elif line == ' '.join(sorted(line.split(), reverse=True)):
        return True
    else:
        return False


def total_calc():
    total = 0
    for line in content.splitlines():
        if isnt_large_diff(line):
            if not has_consecutive_repeating_chars(line):
                total += 1
            else:
                pass
        else:
            pass
    return total

print(total_calc())
