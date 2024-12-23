def is_safe(levels: list[int]) -> bool:
    check_increasing = levels[1] - levels[0] > 0
    for i in range(1, len(levels)):
        difference = levels[i] - levels[i - 1]
        if check_increasing:
            if difference < 1 or difference > 3:
                return False
        else:
            if difference < -3 or difference > -1:
                return False
    return True


with open("input", "r") as file:
    safe_reports_count = 0
    for line in file:
        levels = [int(level) for level in line.split()]
        if is_safe(levels):
            safe_reports_count += 1

    print(f"Number of safe reports: {safe_reports_count}")
