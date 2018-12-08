import networkx as nx
# import collections


def parse_line(line):
    return True


def get_graph(data):

    G = nx.DiGraph()
    for line in data.splitlines():
        steps = line.split(' ')
        step_1, step_2 = (steps[1], steps[7])
        G.add_node(step_1)
        G.add_node(step_2)
        G.add_edge(step_1, step_2, weight=ord(step_2))
        G.add_path([step_1, step_2], weight=ord(step_2))
    return G


def solve_task_1(data):
    G = get_graph(data)
    return ''.join(nx.lexicographical_topological_sort(G))


def solve_task_2(data):

    G = get_graph(data)
    order = list(nx.lexicographical_topological_sort(G))

    all_work = []
    for work in order:
        all_work = all_work + list(work * (ord(work) - 64))

    # all_work.reverse()

    # w1, w2 = collections.deque(), collections.deque()

    for step in all_work:
        print(step, len(G[step]))

    return 42
