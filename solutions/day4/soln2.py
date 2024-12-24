def count_xmas(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if matrix[i][j] != "A":
                continue
            is_first_cross_valid = (matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S") \
                or (matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M")
            is_second_cross_valid = (matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S") \
                or (matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M")
            count += is_first_cross_valid and is_second_cross_valid
    return count


with open("input", "r") as file:
    matrix = [list(line.strip()) for line in file]
    count = count_xmas(matrix)
    print(f"X-MAS count: {count}")
