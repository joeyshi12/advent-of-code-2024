def read_input(filename: str) -> tuple[list[list[int]], list[list[int]]]:
    with open(filename, "r") as file:
        ordering_rules = []
        for line in file:
            if line.isspace():
                break
            a, b = line.split("|")
            ordering_rules.append([int(a), int(b)])

        updates = []
        for line in file:
            updates.append([int(num) for num in line.split(",")])

        return ordering_rules, updates


def is_valid_update(update: list[int],
                    less_than_rule_map: dict[int, set[int]],
                    greater_than_rule_map: dict[int, set[int]]) -> bool:
    for i, num1 in enumerate(update):
        less_than_rules = less_than_rule_map.get(num1)
        greater_than_rules = greater_than_rule_map.get(num1)

        for j in range(i):
            num2 = update[j]
            if less_than_rules and num2 in less_than_rules:
                return False

        for j in range(i + 1, len(update)):
            num2 = update[j]
            if greater_than_rules and num2 in greater_than_rules:
                return False

    return True


def main():
    ordering_rules, updates = read_input("input")
    less_than_rule_map: dict[int, set[int]] = {}
    greater_than_rule_map: dict[int, set[int]] = {}

    for a, b in ordering_rules:
        if a not in less_than_rule_map:
            less_than_rule_map[a] = set()
        if b not in greater_than_rule_map:
            greater_than_rule_map[b] = set()
        less_than_rule_map[a].add(b)
        greater_than_rule_map[b].add(a)

    middle_page_number_sum = 0
    for update in updates:
        if is_valid_update(update, less_than_rule_map, greater_than_rule_map):
            middle_page_number_sum += update[len(update) // 2]

    print(f"Middle page number sum: {middle_page_number_sum}")


if __name__ == "__main__":
    main()
