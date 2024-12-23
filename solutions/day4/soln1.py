def count_xmas(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    # TODO
    return 0


with open("example", "r") as file:
    matrix = [list(line.strip()) for line in file]
    count = count_xmas(matrix)
    print(f"XMAS count: {count}")
