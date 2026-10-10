import random


def Matrix_multip(M1, M2):
    """Multiply two matrices using only for loops, * and + operators."""
    rows_M1 = len(M1)
    cols_M1 = len(M1[0])
    cols_M2 = len(M2[0])

    result = []
    for i in range(rows_M1):
        row = []
        for j in range(cols_M2):
            s = 0
            for k in range(cols_M1):
                s = s + M1[i][k] * M2[k][j]
            row.append(s)
        result.append(row)
    return result


if __name__ == "__main__":
    random.seed(42)
    M1 = [[random.randint(0, 50) for _ in range(10)] for _ in range(5)]
    M2 = [[random.randint(0, 50) for _ in range(5)] for _ in range(10)]

    print("M1 =")
    for row in M1:
        print(row)
    print("\nM2 =")
    for row in M2:
        print(row)

    M3 = Matrix_multip(M1, M2)
    print("\nM1 * M2 =")
    for row in M3:
        print(row)
