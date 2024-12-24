def count_xmas(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != "X":
                continue

            if i >= 3:
                count += matrix[i - 1][j] == "M" \
                    and matrix[i - 2][j] == "A" \
                    and matrix[i - 3][j] == "S"
            if i < m - 3:
                count += matrix[i + 1][j] == "M" \
                    and matrix[i + 2][j] == "A" \
                    and matrix[i + 3][j] == "S"
            if j < n - 3:
                count += matrix[i][j + 1] == "M" \
                    and matrix[i][j + 2] == "A" \
                    and matrix[i][j + 3] == "S"
            if j >= 3:
                count += matrix[i][j - 1] == "M" \
                    and matrix[i][j - 2] == "A" \
                    and matrix[i][j - 3] == "S"

            if i >= 3 and j >= 3:
                count += matrix[i - 1][j - 1] == "M" \
                    and matrix[i - 2][j - 2] == "A" \
                    and matrix[i - 3][j - 3] == "S"
            if i >= 3 and j < n - 3:
                count += matrix[i - 1][j + 1] == "M" \
                    and matrix[i - 2][j + 2] == "A" \
                    and matrix[i - 3][j + 3] == "S"
            if i < m - 3 and j >= 3:
                count += matrix[i + 1][j - 1] == "M" \
                    and matrix[i + 2][j - 2] == "A" \
                    and matrix[i + 3][j - 3] == "S"
            if i < m - 3 and j < n - 3:
                count += matrix[i + 1][j + 1] == "M" \
                    and matrix[i + 2][j + 2] == "A" \
                    and matrix[i + 3][j + 3] == "S"

    return count


with open("input", "r") as file:
    matrix = [list(line.strip()) for line in file]
    count = count_xmas(matrix)
    print(f"XMAS count: {count}")
