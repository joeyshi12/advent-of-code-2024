def fencing_price(grid: list[list[str]]) -> int:
    # TODO: finish implementation
    total_price = 0
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(i: int, j: int) -> int:
        area = 0
        edge_positions = []
        stack = [(i, j)]
        visited[i][j] = True
        while stack:
            row, col = stack.pop()
            area += 1
            for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    edge_positions.append((next_row, next_col))
                    continue
                if grid[row][col] != grid[next_row][next_col]:
                    edge_positions.append((next_row, next_col))
                    continue
                if visited[next_row][next_col]:
                    continue
                stack.append((next_row, next_col))
                visited[next_row][next_col] = True

        positions_set = set(edge_positions)
        groups = {}
        curr_group = 1
        for position in positions_set:
            if position in groups:
                continue
            stack = [position]
            groups[position] = curr_group
            while stack:
                curr_pos = stack.pop()
                row, col = curr_pos
                for next_pos in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if next_pos in positions_set and next_pos not in groups:
                        groups[next_pos] = curr_group
                        stack.append(next_pos)
            curr_group += 1

        print(grid[i][j], curr_group - 1, len(edge_positions) - len(positions_set), curr_group + len(edge_positions) - len(positions_set) - 1)
        return area * (curr_group + len(edge_positions) - len(positions_set))

    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            total_price += dfs(i, j)
    return total_price


for filename in ["example"]:
    with open(filename, "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))
        print(f"Fencing price of {filename} = {fencing_price(grid)}")
