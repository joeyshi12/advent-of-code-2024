import itertools


def read_input(filename: str):
    with open(filename, "r") as file:
        locks = []
        keys = []

        for block_str in file.read().split("\n\n"):
            heights = [0] * 5
            row_strs = block_str.split()

            for i in range(1, 6):
                row = row_strs[i]
                for j in range(5):
                    if row[j] == "#":
                        heights[j] += 1

            if block_str[0] == "#":
                locks.append(heights)
            else:
                keys.append(heights)

        return locks, keys


result = 0
locks, keys = read_input("input")
for lock, key in itertools.product(locks, keys):
    if all(lock[i] + key[i] <= 5 for i in range(5)):
        result += 1

print(result)
