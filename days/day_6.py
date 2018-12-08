
def get_distance(coord, dest):
    return abs(int(coord[0]) - dest[0]) + abs(int(coord[1]) - dest[1])


def closest(coord, max_x, max_y, points):
    closest = [(), max_y * max_x]
    for dest in points:

        distance = get_distance(coord, dest)
        if closest[1] > distance:
            closest = (dest, distance)
        elif closest[1] == distance:
            closest = (None, distance)
    return closest


def is_safe_coord(coord, points):
    total = 0
    for dest in points:
        distance = get_distance(coord, dest)
        total += distance

        if total >= 10000:
            return False
    return True


def solve_task_1(data):

    coords = [line.split(', ') for line in data.splitlines()]

    points = [[int(coord[0]), int(coord[1])] for coord in coords]

    max_x = max(x[0] for x in points)
    max_y = max(x[0] for x in points)

    all_coords = [[int(x), int(y)] for x in range(0, 400) for y in range(0, 400)]

    counted_coords = {str(key): {'total': 0, 'tainted': False} for key in points}
    counted_coords.update({'None': {'total': 0, 'tainted': False}})
    for coord in all_coords:
        closest_point, distance_to_point = closest(coord, max_x, max_y, points)
        counted_coords[str(closest_point)]['total'] = counted_coords[str(closest_point)]['total'] + 1
        if any([True for p in coord if p in [0, max_x, max_y]]):
            counted_coords[str(closest_point)]['tainted'] = True

    valid = {k: v for k, v in counted_coords.items() if v['tainted'] is False}
    ranked = sorted(valid.items(), key=lambda x: x[1]['total'], reverse=True)

    return ranked[0][1]['total']


def solve_task_2(data):
    coords = [line.split(', ') for line in data.splitlines()]

    points = [[int(coord[0]), int(coord[1])] for coord in coords]

    all_coords = [[int(x), int(y)] for x in range(0, 400) for y in range(0, 400)]

    safe_coords = []
    for coord in all_coords:
        if is_safe_coord(coord, points):
            safe_coords.append(coord)

    return len(safe_coords)
