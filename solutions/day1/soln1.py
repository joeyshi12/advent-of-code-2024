with open("input", "r") as f:
    left_col = []
    right_col = []

    for line in f.readlines():
        a, b = line.split()
        left_col.append(int(a))
        right_col.append(int(b))

    left_col.sort()
    right_col.sort()

    result = 0
    for a, b in zip(left_col, right_col):
        result += abs(a - b)

    print(result)
