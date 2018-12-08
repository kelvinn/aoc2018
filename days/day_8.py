
def parse_line(line):
    return True


def traverse_tree(t):

    num_children = t.pop(0)
    num_meta_data = t.pop(0)
    return sum(traverse_tree(t) for _ in range(num_children)) + sum(t.pop(0) for _ in range(num_meta_data))


def solve_task_1(data):
    t = [int(x) for x in data.split()]
    out = traverse_tree(t)

    return out


def solve_task_2(data):

    # if num_children == 0, then sum metadata
    # if num_children > 0, then metadata entries are indexes to children

    return 42
