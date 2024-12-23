import re

with open("input", "r") as file:
    match_iter = re.finditer(r"mul\((\d?\d?\d),(\d?\d?\d)\)", file.read())
    result = 0
    for match in match_iter:
        a, b = match.groups()
        a, b = int(a), int(b)
        result += a * b
    print(result)
