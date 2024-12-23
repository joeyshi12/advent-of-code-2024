import re

with open("input", "r") as file:
    match_iter = re.finditer(r"mul\((\d?\d?\d),(\d?\d?\d)\)|do\(\)|don't\(\)", file.read())
    result = 0
    instructions_enabled = True
    for match in match_iter:
        group = match.group()

        if group == "do()":
            instructions_enabled = True
            continue

        if group == "don't()":
            instructions_enabled = False
            continue

        if not instructions_enabled:
            continue

        a, b = match.groups()
        a, b = int(a), int(b)
        result += a * b

    print(result)
