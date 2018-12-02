def solve_task_1(data):
    return eval(data.replace('\n', ''))


def solve_task_2(data):
    all_freq = set()
    x = 0
    while True:
        for line in data.split("\n"):
            num = int(line[1:])
            x += (num if line[0] == "+" else -num)
            if x in all_freq:
                return x
            all_freq.add(x)
