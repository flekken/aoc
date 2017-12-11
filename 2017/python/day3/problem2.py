def get_neighbour_sum(grid, x, y):
    neighbours = 0
    if (str(x) + str(y - 1)) in grid:
        neighbours += grid[str(x) + str(y - 1)]
    if (str(x) + str(y + 1)) in grid:
        neighbours += grid[str(x) + str(y + 1)]
    if (str(x + 1) + str(y)) in grid:
        neighbours += grid[str(x + 1) + str(y)]
    if (str(x - 1) + str(y)) in grid:
        neighbours += grid[str(x - 1) + str(y)]
    if (str(x - 1) + str(y + 1)) in grid:
        neighbours += grid[str(x - 1) + str(y + 1)]
    if (str(x - 1) + str(y - 1)) in grid:
        neighbours += grid[str(x - 1) + str(y - 1)]
    if (str(x + 1) + str(y + 1)) in grid:
        neighbours += grid[str(x + 1) + str(y + 1)]
    if (str(x + 1) + str(y - 1)) in grid:
        neighbours += grid[str(x + 1) + str(y - 1)]
    return neighbours


def find_prev_number(target):
    grid = dict()
    grid["00"] = 1
    movement = 1
    x = 0
    y = 0
    # while current number < target number:
    while True:
        # right
        for _ in range(1, movement + 1):
            y += 1
            grid[str(x) + str(y)] = get_neighbour_sum(grid, x, y)
            if grid[str(x) + str(y)] > target:
                return grid[str(x) + str(y)]
        # up
        for _ in range(1, movement + 1):
            x -= 1
            grid[str(x) + str(y)] = get_neighbour_sum(grid, x, y)
            if grid[str(x) + str(y)] > target:
                return grid[str(x) + str(y)]
        movement += 1
        # left
        for _ in range(1, movement + 1):
            y -= 1
            grid[str(x) + str(y)] = get_neighbour_sum(grid, x, y)
            if grid[str(x) + str(y)] > target:
                return grid[str(x) + str(y)]
        # down
        for _ in range(1, movement + 1):
            x += 1
            grid[str(x) + str(y)] = get_neighbour_sum(grid, x, y)
            if grid[str(x) + str(y)] > target:
                return grid[str(x) + str(y)]
        movement += 1


target_number = 361527
print(find_prev_number(target_number))
