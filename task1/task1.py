import sys

def get_path(n, m):
    numbers = list(range(1, n + 1))
    path = []
    pos = 0

    while True:
        path.append(numbers[pos])

        steps = m - 1
        for _ in range(steps):
            pos += 1
            if pos == n:
                pos = 0

        if pos == 0:
            break

    return "".join(map(str, path))


def main():
    if len(sys.argv) == 5:
        n1, m1, n2, m2 = map(int, sys.argv[1:])
    else:
        # подставьте свои значения
        n1, m1, n2, m2 = 6, 3, 5, 4

    path1 = get_path(n1, m1)
    path2 = get_path(n2, m2)

    print(path1 + path2)


if __name__ == "__main__":
    main()