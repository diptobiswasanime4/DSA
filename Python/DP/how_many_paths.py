# how many paths possible to travel from cell a to b in a grid

grid = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

def how_many_paths_rec(grid):
    rows = len(grid)
    cols = len(grid[0])

    return rec_helper(0, 0, rows, cols, grid)

def rec_helper(x, y, rows, cols, grid):
    if (x == rows - 1):
        return 1
    if (y == cols - 1):
        return 1
    return rec_helper(x + 1, y, rows, cols, grid) + rec_helper(x, y + 1, rows, cols, grid)

def how_many_paths_dp(grid):
    rows = len(grid)
    cols = len(grid[0])

    return dp_helper(0, 0, rows, cols, grid)

def dp_helper(x, y, rows, cols, grid):
    if (x == rows - 1):
        return 1
    if (y == cols - 1):
        return 1
    

print(how_many_paths_rec(grid))