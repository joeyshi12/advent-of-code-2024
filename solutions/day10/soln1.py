def trailhead_score(i: int, j: int, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    visited[i][j] = True
    stack = [(i, j)]
    while stack:
        row, col = stack.pop()
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                continue
            if visited[next_row][next_col] or grid[next_row][next_col] - grid[row][col] != 1:
                continue
            visited[next_row][next_col] = True
            stack.append((next_row, next_col))

    score = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 9 and visited[row][col]:
                score += 1

    return score

with open("input", "r") as file:
    grid = []
    for line in file:
        grid.append([int(c) for c in line.strip()])

    m, n = len(grid), len(grid[0])
    score_sum = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            score_sum += trailhead_score(i, j, grid)
    print(score_sum)
