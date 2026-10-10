import random


def Least_moves(x):
    """Minimum number of double-or-add-1 moves to reach x starting from 1."""
    moves = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x - 1
        moves = moves + 1
    print(moves)


if __name__ == "__main__":
    # Examples from the assignment
    print("Least_moves(2):")
    Least_moves(2)
    print("Least_moves(5):")
    Least_moves(5)

    # Random test
    x = random.randint(1, 100)
    print(f"\nRandom x = {x}")
    print(f"Least_moves({x}):")
    Least_moves(x)
