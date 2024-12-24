import itertools


def read_edges(filename: str) -> list[list[str]]:
    with open(filename, "r") as file:
        edges = []
        for line in file:
            u, v = line.strip().split("-")
            edges.append([u, v])
        return edges
    raise Exception(f"Failed to read {filename}")


def count_valid_sets(matrix: list[list[bool]], id_map: dict[str, int]) -> int:
    count = 0
    for x, y, z in itertools.combinations(id_map.keys(), 3):
        if x[0] != "t" and y[0] != "t" and z[0] != "t":
            continue
        x_id = id_map[x]
        y_id = id_map[y]
        z_id = id_map[z]
        if matrix[x_id][y_id] and matrix[y_id][z_id] and matrix[x_id][z_id]:
            count += 1
    return count


def main():
    edges = read_edges("input")
    node_set = set()
    for u, v in edges:
        node_set.add(u)
        node_set.add(v)

    id_map = {node: i for i, node in enumerate(node_set)}
    nodes_count = len(id_map)
    matrix = [[False] * nodes_count for _ in range(nodes_count)]
    for u, v in edges:
        u_id, v_id = id_map[u], id_map[v]
        matrix[u_id][v_id] = True
        matrix[v_id][u_id] = True

    print(count_valid_sets(matrix, id_map))


if __name__ == "__main__":
    main()
