from collections import Counter
import difflib


def solve_task_1(data):
    two = 0
    three = 0

    for row in data.splitlines():
        hist = Counter(row)
        if list(hist.values()).count(2) >= 1: two += 1
        if list(hist.values()).count(3) >= 1: three += 1
    return two * three


def solve_task_2(data):
    highest = {'score': 0, 'a': None, 'b': None}
    for a in data.splitlines():
        for b in data.splitlines():
            if a != b:
                seq = difflib.SequenceMatcher(None, a, b)
                d = seq.ratio()
                if d > highest['score']:
                    highest = {'score': d, 'a': a, 'b': b}

    common = [value for value in highest['b'] if value in set(highest['a'])]
    return ''.join(common)
