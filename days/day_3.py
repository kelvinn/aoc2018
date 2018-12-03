
def get_matrix(data):
    w, h = 1000, 1000
    matrix = [[0 for x in range(w)] for y in range(h)]

    for line in data.splitlines():
        claim, _, pos, panel = line.split(' ')
        panel_x, panel_y = [int(i) for i in panel.split('x')]
        pos_x, pos_y = [int(i) for i in pos.strip(':').split(',')]

        for row in range(pos_x, panel_x + pos_x):
            for col in range(pos_y, pos_y + panel_y):
                matrix[row][col] = matrix[row][col] + 1

    return matrix


def solve_task_1(data):
    matrix = get_matrix(data)

    # Get total sq in
    total = 0
    for row in matrix:
        for col in row:
            if col >= 2:
                total += 1

    return total


def solve_task_2(data):
    matrix = get_matrix(data)
    for line in data.splitlines():
        claim, _, pos, panel = line.split(' ')
        panel_x, panel_y = [int(i) for i in panel.split('x')]
        pos_x, pos_y = [int(i) for i in pos.strip(':').split(',')]

        total = 0
        for row in range(pos_x, panel_x + pos_x):
            for col in range(pos_y, pos_y + panel_y):
                if matrix[row][col] != 1:
                    total += 1

        if total == 0:
            return claim
