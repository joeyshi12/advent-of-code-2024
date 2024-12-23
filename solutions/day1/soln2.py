with open("input", "r") as f:
    left_col = []
    right_counts = {}

    for line in f.readlines():
        a, b = line.split()
        a = int(a)
        b = int(b)
        left_col.append(a)
        right_counts[b] = right_counts.get(b, 0) + 1

    result = 0
    for a in left_col:
        b_count = right_counts.get(a, 0)
        result += a * b_count

    print(result)

