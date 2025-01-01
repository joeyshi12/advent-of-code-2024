def read_input(filename: str) -> list[tuple[int, list[int]]]:
    with open(filename, "r") as file:
        equations = []
        for line in file:
            test_value, values_str = line.split(": ")
            equations.append((
                int(test_value),
                [int(value) for value in values_str.split()]
            ))
        return equations


def is_valid_configuration(test_value: int, values: list[int]) -> bool:
    stack = [(values[0], 1)]
    while stack:
        acc, i = stack.pop()
        if i < len(values):
            stack.append((acc + values[i], i + 1))
            stack.append((acc * values[i], i + 1))
            continue

        if acc == test_value:
            return True

    return False


def main():
    equations = read_input("input")
    result = 0
    for test_value, values in equations:
        if is_valid_configuration(test_value, values):
            result += test_value
    print(result)


if __name__ == "__main__":
    main()
