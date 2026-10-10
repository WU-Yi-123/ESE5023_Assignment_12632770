def Pascal_triangle(k):
    """Print the k-th line of Pascal's triangle (0-indexed)."""
    line = [1]
    for _ in range(k):
        new_line = [1]
        for i in range(len(line) - 1):
            new_line.append(line[i] + line[i + 1])
        new_line.append(1)
        line = new_line
    print(line)


if __name__ == "__main__":
    print("Pascal_triangle(100):")
    Pascal_triangle(100)
    print("\nPascal_triangle(200):")
    Pascal_triangle(200)
