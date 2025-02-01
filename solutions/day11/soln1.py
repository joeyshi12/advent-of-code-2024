def blink(arrangement: list[int]) -> list[int]:
    result = []
    for num in arrangement:
        if num == 0:
            result.append(1)
            continue
        num_str = str(num)
        num_digits = len(num_str)
        if num_digits % 2 == 0:
            mid = num_digits // 2
            result.append(int(num_str[:mid]))
            result.append(int(num_str[mid:]))
            continue
        result.append(num * 2024)
    return result


def count_arrangements(filename: str, blinks: int) -> int:
    with open(filename, "r") as file:
        arrangement = [int(val) for val in file.read().split()]
        for _ in range(blinks):
            arrangement = blink(arrangement)
        return len(arrangement)


for filename, blinks in [("example", 25), ("input", 25)]:
    print(f"Number of arrangements in {filename} = {count_arrangements(filename, blinks)}")
