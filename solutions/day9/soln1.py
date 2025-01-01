def read_input(filename: str) -> list[int]:
    with open(filename, "r") as file:
        disk_map = file.read().strip()
        disk_layout = []
        for i in range(0, len(disk_map), 2):
            id = i // 2
            file_str = disk_map[i:i+2]
            blocks_count = int(file_str[0])
            disk_layout.extend([id] * blocks_count)
            if len(file_str) == 2:
                free_blocks_count = int(file_str[1])
                disk_layout.extend([-1] * free_blocks_count)
        return disk_layout


def main():
    disk_layout = read_input("input")
    i, j = 1, len(disk_layout) - 1
    while i < j:
        if disk_layout[i] != -1:
            i += 1
            continue
        if disk_layout[j] == -1:
            j -= 1
            continue
        disk_layout[i], disk_layout[j] = disk_layout[j], disk_layout[i]
        i += 1
        j -= 1

    result = 0
    for i, id in enumerate(disk_layout):
        if id != -1:
            result += i * id
    print(result)


if __name__ == "__main__":
    main()
