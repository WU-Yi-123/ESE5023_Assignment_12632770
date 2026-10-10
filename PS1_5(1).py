import itertools


def _generate_expressions():
    """Yield all valid expressions formed from 123456789 and their values."""
    digits = "123456789"
    n = len(digits)
    # 0 = join, 1 = '+', 2 = '-'
    for ops in itertools.product("0+-", repeat=n - 1):
        expr = digits[0]
        for i, op in enumerate(ops):
            if op != "0":
                expr = expr + op
            expr = expr + digits[i + 1]
        value = eval(expr)
        yield value, expr


def Find_expression(target):
    """Print every expression that evaluates to target."""
    found = False
    for value, expr in _generate_expressions():
        if value == target:
            print(f"{expr}={target}")
            found = True
    if not found:
        print(f"No solution for {target}")


if __name__ == "__main__":
    print("Find_expression(50):")
    Find_expression(50)

    print("\nCounting Total_solutions for i = 1 to 100 ...")
    Total_solutions = [0] * 101
    for value, _ in _generate_expressions():
        if 1 <= value <= 100:
            Total_solutions[value] = Total_solutions[value] + 1

    max_solutions = max(Total_solutions[1:])
    min_solutions = min(Total_solutions[1:])
    max_numbers = [i for i in range(1, 101) if Total_solutions[i] == max_solutions]
    min_numbers = [i for i in range(1, 101) if Total_solutions[i] == min_solutions]

    print(f"Maximum {max_solutions} solutions for: {max_numbers}")
    print(f"Minimum {min_solutions} solutions for: {min_numbers}")

    # Plot
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 5))
        plt.bar(range(1, 101), Total_solutions[1:], color="steelblue")
        plt.xlabel("Target integer")
        plt.ylabel("Number of solutions")
        plt.title("Total solutions for 123456789 expressions")
        plt.tight_layout()
        plt.savefig("Total_solutions.png")
        print("Plot saved to Total_solutions.png")
    except ImportError:
        print("matplotlib not installed; skipping plot.")
