class Guard:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.__direction = "U"

    def rotate(self):
        match self.__direction:
            case "U":
                self.__direction = "R"
            case "R":
                self.__direction = "D"
            case "D":
                self.__direction = "L"
            case "L":
                self.__direction = "U"
            case _:
                raise Exception(f"Invalid direction {self.__direction}")

    def next_position(self):
        match self.__direction:
            case "U":
                return (self.row - 1, self.col)
            case "R":
                return (self.row, self.col + 1)
            case "D":
                return (self.row + 1, self.col)
            case "L":
                return (self.row, self.col - 1)
            case _:
                raise Exception(f"Invalid direction {self.__direction}")


def read_input(filename: str) -> tuple[Guard, list[list[bool]]]:
    with open(filename, "r") as file:
        guard = None
        obstruction_map = []

        i = 0
        for line in file:
            line = line.strip()
            obstruction_map.append([char == "#" for char in line])
            for j, char in enumerate(line):
                if char == "^":
                    guard = Guard(i, j)
            i += 1

        if guard is None:
            raise Exception("Failed to find guard position")

        return guard, obstruction_map


def move_and_count_visited_positions(guard: Guard,
                                     obstruction_map: list[list[bool]]) -> int:
    height, width = len(obstruction_map), len(obstruction_map[0])
    visited_map = [[False] * width for _ in range(height)]
    visited_map[guard.row][guard.col] = True

    while True:
        row, col = guard.next_position()
        if row < 0 or row >= height or col < 0 or col >= width:
            break
        if obstruction_map[row][col]:
            guard.rotate()
            continue
        guard.row = row
        guard.col = col
        visited_map[guard.row][guard.col] = True

    return sum(sum(row) for row in visited_map)


def main():
    guard, obstruction_map = read_input("input")
    print(move_and_count_visited_positions(guard, obstruction_map))


if __name__ == "__main__":
    main()
