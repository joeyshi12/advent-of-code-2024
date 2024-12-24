def read_edges(filename: str) -> list[list[str]]:
    with open(filename, "r") as file:
        edges = []
        for line in file:
            u, v = line.strip().split("-")
            edges.append([u, v])
        return edges
    raise Exception(f"Failed to read {filename}")


def find_maximal_clique(matrix: list[list[int]],
                        id_map: dict[str, int]) -> list[str]:
    """Brute-force searches a maximal clique in a graph and returns the result."""
    nodes = list(id_map.keys())

    def __search(clique: list[str], index: int) -> list[str]:
        if index == -1:
            return clique
        u = nodes[index]
        row = matrix[id_map[u]]
        clique1 = __search(clique, index - 1)
        if all(row[id_map[v]] for v in clique):
            clique2 = __search(clique + [u], index - 1)
            return clique1 if len(clique1) > len(clique2) else clique2
        return clique1

    return __search([], len(nodes) - 1)


def main():
    edges = read_edges("input")
    node_set = set()
    for u, v in edges:
        node_set.add(u)
        node_set.add(v)

    id_map = {node: i for i, node in enumerate(node_set)}
    matrix = [[False] * len(id_map) for _ in range(len(id_map))]
    for u, v in edges:
        u_id, v_id = id_map[u], id_map[v]
        matrix[u_id][v_id] = True
        matrix[v_id][u_id] = True

    maximal_clique = find_maximal_clique(matrix, id_map)
    maximal_clique.sort()
    print(",".join(maximal_clique))


if __name__ == "__main__":
    main()
