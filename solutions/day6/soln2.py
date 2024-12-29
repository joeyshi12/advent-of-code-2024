from typing import Optional


class Guard:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.direction = "U"

    def rotated_direction(self):
        match self.direction:
            case "U":
                return "R"
            case "R":
                return "D"
            case "D":
                return "L"
            case "L":
                return "U"
            case _:
                raise Exception(f"Invalid direction {self.direction}")

    def next_position(self):
        match self.direction:
            case "U":
                return (self.row - 1, self.col)
            case "R":
                return (self.row, self.col + 1)
            case "D":
                return (self.row + 1, self.col)
            case "L":
                return (self.row, self.col - 1)
            case _:
                raise Exception(f"Invalid direction {self.direction}")


class DirectionalVisitMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.up_visited_map = [[False] * width for _ in range(height)]
        self.right_visited_map = [[False] * width for _ in range(height)]
        self.down_visited_map = [[False] * width for _ in range(height)]
        self.left_visited_map = [[False] * width for _ in range(height)]

    def has_visited(self, i: int, j: int, direction: Optional[str] = None) -> bool:
        if direction is None:
            return self.up_visited_map[i][j] \
                or self.right_visited_map[i][j] \
                or self.down_visited_map[i][j] \
                or self.left_visited_map[i][j]

        match direction:
            case "U":
                return self.up_visited_map[i][j]
            case "R":
                return self.right_visited_map[i][j]
            case "D":
                return self.down_visited_map[i][j]
            case "L":
                return self.left_visited_map[i][j]
            case _:
                raise Exception(f"Invalid direction {direction}")

    def set_visited(self, i: int, j: int, direction: str):
        match direction:
            case "U":
                self.up_visited_map[i][j] = True
            case "R":
                self.right_visited_map[i][j] = True
            case "D":
                self.down_visited_map[i][j] = True
            case "L":
                self.left_visited_map[i][j] = True
            case _:
                raise Exception(f"Invalid direction {direction}")

    def copy(self):
        visited_map = DirectionalVisitMap(self.width, self.height)
        visited_map.up_visited_map = [row.copy() for row in self.up_visited_map]
        visited_map.right_visited_map = [row.copy() for row in self.right_visited_map]
        visited_map.down_visited_map = [row.copy() for row in self.down_visited_map]
        visited_map.left_visited_map = [row.copy() for row in self.left_visited_map]
        return visited_map


def read_input(filename: str) -> tuple[int, int, list[list[bool]]]:
    with open(filename, "r") as file:
        guard_position = None
        obstruction_map = []

        i = 0
        for line in file:
            line = line.strip()
            obstruction_map.append([char == "#" for char in line])
            for j, char in enumerate(line):
                if char == "^":
                    guard_position = (i, j)
            i += 1

        if guard_position is None:
            raise Exception("Failed to find guard position")

        return *guard_position, obstruction_map


def is_in_walk_cycle(start_row: int,
                     start_col: int,
                     obstruction_map: list[list[bool]]) -> bool:
    height, width = len(obstruction_map), len(obstruction_map[0])
    guard = Guard(start_row, start_col)
    visit_map = DirectionalVisitMap(width, height)
    while True:
        next_row, next_col = guard.next_position()
        if next_row < 0 or next_row >= height or next_col < 0 or next_col >= width:
            return False
        if obstruction_map[next_row][next_col]:
            guard.direction = guard.rotated_direction()
            visit_map.set_visited(guard.row, guard.col, guard.direction)
            continue
        if visit_map.has_visited(next_row, next_col, guard.direction):
            return True
        guard.row = next_row
        guard.col = next_col
        visit_map.set_visited(next_row, next_col, guard.direction)


# For debugging purposes
def print_visited_map_with_obstacle(visit_map: DirectionalVisitMap,
                                    obstruction_map: list[list[bool]],
                                    obstacle_row: int,
                                    obstacle_col: int):
    height, width = len(obstruction_map), len(obstruction_map[0])
    for i in range(height):
        row = []
        for j in range(width):
            if obstacle_row == i and obstacle_col == j:
                row.append("O")
                continue
            if obstruction_map[i][j]:
                row.append("#")
                continue
            if not visit_map.has_visited(i, j):
                row.append(".")
                continue
            if not visit_map.has_visited(i, j, "L") and not visit_map.has_visited(i, j, "R"):
                row.append("|")
            elif not visit_map.has_visited(i, j, "U") and not visit_map.has_visited(i, j, "D"):
                row.append("-")
            else:
                row.append("+")

        print("".join(row))
    print("\n")


def main():
    start_row, start_col, obstruction_map = read_input("input")
    result = 0
    for _, row in enumerate(obstruction_map):
        for j, has_obstacle in enumerate(row):
            if has_obstacle:
                continue
            row[j] = True
            if is_in_walk_cycle(start_row, start_col, obstruction_map):
                result += 1
            row[j] = False
    print(result)


if __name__ == "__main__":
    main()
