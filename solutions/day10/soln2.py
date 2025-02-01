def trailhead_rating(i: int, j: int, grid: list[list[int]]) -> int:
    rating = 0

    m, n = len(grid), len(grid[0])
    stack = [(i, j)]
    while stack:
        row, col = stack.pop()
        if grid[row][col] == 9:
            rating += 1
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                continue
            if grid[next_row][next_col] - grid[row][col] != 1:
                continue
            stack.append((next_row, next_col))

    return rating


def rating_sum(filename: str) -> int:
    with open(filename, "r") as file:
        grid = []
        for line in file:
            grid.append([int(c) for c in line.strip()])

        m, n = len(grid), len(grid[0])
        rating_sum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                rating_sum += trailhead_rating(i, j, grid)
        return rating_sum


filenames = ["example", "input"]
for filename in filenames:
    print(f"Rating sum of {filename} = {rating_sum(filename)}")
