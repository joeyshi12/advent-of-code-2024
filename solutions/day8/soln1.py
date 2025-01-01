class AntennaMap:
    def __init__(self, antenna_positions: dict[str, list[tuple[int, int]]], width: int, height: int):
        self.antenna_positions = antenna_positions
        self.width = width
        self.height = height


def read_input(filename: str) -> AntennaMap:
    """Returns a map from antenna frequency label to positions."""
    with open(filename, "r") as file:
        antenna_positions = {}
        rows = 0
        cols = -1
        for line in file:
            line = line.strip()
            cols = len(line)
            for j, char in enumerate(line):
                if char == ".":
                    continue
                if char not in antenna_positions:
                    antenna_positions[char] = []
                antenna_positions[char].append((rows, j))
            rows += 1
        return AntennaMap(antenna_positions, cols, rows)


def main():
    antenna_map = read_input("input")
    width, height = antenna_map.width, antenna_map.height
    antinode_map = [[False] * width for _ in range(height)]
    for positions in antenna_map.antenna_positions.values():
        for i in range(len(positions)):
            row1, col1 = positions[i]
            for j in range(i + 1, len(positions)):
                row2, col2 = positions[j]
                row_delta = row2 - row1
                col_delta = col2 - col1

                arow1, acol1 = row1 - row_delta, col1 - col_delta
                arow2, acol2 = row2 + row_delta, col2 + col_delta
                if 0 <= arow1 < height and 0 <= acol1 < width:
                    antinode_map[arow1][acol1] = True
                if 0 <= arow2 < height and 0 <= acol2 < width:
                    antinode_map[arow2][acol2] = True

    print(sum(sum(row) for row in antinode_map))


if __name__ == "__main__":
    main()
