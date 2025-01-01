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


# Note: this is very slow
def main():
    disk_layout = read_input("input")
    j = len(disk_layout) - 1  # Pointer at the end of a block
    while j > 0:
        if disk_layout[j] == -1:
            j -= 1
            continue

        # Find size of block
        id = disk_layout[j]
        size = 0
        while disk_layout[j - size] == id:
            size += 1

        # Find free space larger than size
        i = 0
        while i < j:
            if disk_layout[i] != -1:
                i += 1
                continue

            # Find size of free space
            free_space_size = 0
            while i + free_space_size < len(disk_layout) and disk_layout[i + free_space_size] == -1:
                free_space_size += 1

            if free_space_size >= size:
                for k in range(size):
                    disk_layout[j - k], disk_layout[i + k] = disk_layout[i + k], disk_layout[j - k]

            i += free_space_size

        j -= size

    result = 0
    for i, id in enumerate(disk_layout):
        if id != -1:
            result += i * id
    print(result)


if __name__ == "__main__":
    main()
