from datetime import datetime, timedelta
from collections import Counter
import operator


def parse_line(line):

    line = line.replace(']', '').replace('[', '').split(' ')

    if 'Guard' in line:
        return {'d': line[0], 't': line[1].split(':')[1], 'name': line[3], 'action': line[4]}
    else:
        return {'d': line[0], 't': line[1].split(':')[1], 'action': line[2]}


def get_guards_and_frequencies(data):

    # Clean the data and sort
    clean = []
    for line in data.splitlines():
        clean.append(line.replace(']', '').replace('[', '').split(' '))

    clean.sort()

    # Get start/end dates
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(clean[0][0], date_format)
    end_date = datetime.strptime(clean[-1][0], date_format)

    # Build dict of all possible sleep dates
    all_dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    guard_sleep_days = {i: [] for i in all_dates}

    guards = {}
    guards_freq = {}

    for shift in clean:
        dt = datetime.strptime(shift[0], date_format)
        if shift[2] == 'Guard':
            name = shift[3]
        elif shift[2] == 'falls':
            start_sleep = shift[1].split(':')[1]
        elif shift[2] == 'wakes':
            end_sleep = shift[1].split(':')[1]
            sleeping = range(int(start_sleep), int(end_sleep))
            guard_sleep_days[dt] = guard_sleep_days[dt] + [i for i in sleeping]
            guards[name] = len([i for i in sleeping]) + guards.get(name, 0)
            guards_freq[name] = Counter([i for i in sleeping]) + guards_freq.get(name, Counter())

    sorted_x = sorted(guards.items(), key=operator.itemgetter(1))

    return sorted_x, guards_freq


def solve_task_1(data):
    sorted_x, guards_freq = get_guards_and_frequencies(data
                                                       )
    return int(sorted_x[-1][0].strip('#')) * int(guards_freq[sorted_x[-1][0]].most_common()[0][0])


def solve_task_2(data):
    sorted_x, guards_freq = get_guards_and_frequencies(data)

    highest = ('name', 0, 0)
    for guard, c in guards_freq.items():
        if c.most_common()[0][1] > highest[1]:
            highest = (guard, c.most_common()[0][1], c.most_common()[0][0])

    return int(highest[0].strip('#')) * highest[2]
