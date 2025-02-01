def fencing_price(grid: list[list[str]]) -> int:
    total_price = 0
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            area = 0
            perimeter = 0
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                row, col = stack.pop()
                area += 1
                for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                        perimeter += 1
                        continue
                    if grid[row][col] != grid[next_row][next_col]:
                        perimeter += 1
                        continue
                    if visited[next_row][next_col]:
                        continue
                    stack.append((next_row, next_col))
                    visited[next_row][next_col] = True
            total_price += area * perimeter
    return total_price


for filename in ["example", "input"]:
    with open(filename, "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))
        print(f"Fencing price of {filename} = {fencing_price(grid)}")
