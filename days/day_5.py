import string

lower_upper = list(zip(list(string.ascii_lowercase), list(string.ascii_uppercase)))
upper_lower = list(zip(list(string.ascii_uppercase), list(string.ascii_lowercase)))
ALL_PAIRS = ['%s%s' % pair for pair in lower_upper + upper_lower]


# First implementation. Super slow.
def pop_pairs(data):

    for i in range(0, len(data)):
        if i < len(data) - 1 \
                and data[i] != data[i+1] and (data[i].upper() == data[i+1] or data[i].lower() == data[i+1]):
            data.pop(i+1)
            data.pop(i)
            return data, True
    return data, False


# Faster implementation
def find_and_pop(data):

    for pair in ALL_PAIRS:
        if data.count(pair):
            return data.replace(pair, ''), True
    return data, False


def solve_task_1(data):

    cont = True
    while cont:
        data, cont = find_and_pop(data)
    return len(data)


def solve_task_2(data):

    lu_list = list(zip(list(string.ascii_lowercase), list(string.ascii_uppercase)))

    all_letters = []

    for l, u in lu_list:
        temp_data = data
        temp_data = temp_data.replace(l, '').replace(u, '')
        cont = True
        while cont:
            temp_data, cont = find_and_pop(temp_data)
        print(l, u, len(temp_data))
        all_letters.append(len(temp_data))

    return min(all_letters)
