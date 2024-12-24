def mix(x: int, y: int) -> int:
    return x ^ y


def prune(x: int) -> int:
    return x % 16777216


def next_secret(x: int):
    secret = prune(mix(x * 64, x))
    secret = prune(mix(secret // 32, secret))
    return prune(mix(secret * 2048, secret))


def future_secret(initial_secret: int):
    """Returns the 2000th secret number"""
    secret = initial_secret
    for _ in range(2000):
        secret = next_secret(secret)
    return secret


with open("input", "r") as file:
    result = 0
    for line in file:
        initial_secret = int(line)
        result += future_secret(initial_secret)

    print(f"Sum of 2000th secret numbers: {result}")
