import random


def Print_values(a, b, c):
    """Reflect the flowchart shown in Problem 1."""
    if a > b:
        if b > c:
            print(a, b, c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if b > c:
            print(c, b, a)
        else:
            if a > c:
                print(c, a, b)
            else:
                print(c, b, a)


if __name__ == "__main__":
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    print(f"a={a}, b={b}, c={c}")
    Print_values(a, b, c)
