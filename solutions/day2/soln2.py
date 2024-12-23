def is_safe(levels: list[int], indices: list[int]) -> bool:
    check_increasing = levels[indices[1]] - levels[indices[0]] > 0
    for i in range(1, len(levels) - 1):
        difference = levels[indices[i]] - levels[indices[i - 1]]
        if check_increasing:
            if difference < 1 or difference > 3:
                return False
        else:
            if difference < -3 or difference > -1:
                return False
    return True


def is_almost_safe(levels: list[int]) -> bool:
    for skip_index in range(len(levels)):
        indices = [i for i in range(len(levels)) if i != skip_index]
        if is_safe(levels, indices):
            return True
    return False


with open("input", "r") as file:
    safe_reports_count = 0
    for line in file:
        levels = [int(level) for level in line.split()]
        if is_almost_safe(levels):
            safe_reports_count += 1

    print(f"Number of almost safe reports: {safe_reports_count}")
