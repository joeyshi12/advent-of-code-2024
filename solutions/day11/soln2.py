memo = {}

def blink(num: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    if num in memo and blinks in memo[num]:
        return memo[num][blinks]
    if num not in memo:
        memo[num] = {}
    if num == 0:
        memo[num][blinks] = blink(1, blinks - 1)
        return memo[num][blinks]

    num_str = str(num)
    num_digits = len(num_str)
    if num_digits % 2 == 0:
        mid = num_digits // 2
        memo[num][blinks] = blink(int(num_str[:mid]), blinks - 1) + blink(int(num_str[mid:]), blinks - 1)
        return memo[num][blinks]

    memo[num][blinks] = blink(num * 2024, blinks - 1)
    return memo[num][blinks]


def count_arrangements(filename: str, blinks: int) -> int:
    with open(filename, "r") as file:
        arrangement = [int(val) for val in file.read().split()]
        return sum(blink(num, blinks) for num in arrangement)


for filename, blinks in [("example", 25), ("input", 25), ("input", 75)]:
    print(f"Number of arrangements in {filename} = {count_arrangements(filename, blinks)}")
