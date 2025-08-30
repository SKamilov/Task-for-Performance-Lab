import sys
from decimal import Decimal, getcontext


def read_decimals(path: str) -> list[Decimal]:
    with open(path, 'r', encoding='utf-8') as f:
        return [Decimal(x) for x in f.read().split()]


def main() -> None:
    if len(sys.argv) == 1:
        ellipse_file = 'ellipse.txt'
        points_file = 'points.txt'
    elif len(sys.argv) == 3:
        ellipse_file = sys.argv[1]
        points_file = sys.argv[2]
    else:
        raise SystemExit("Usage: python3 task2.py <ellipse_file> <points_file>")

    getcontext().prec = 100

    cx, cy, rx, ry, *rest = read_decimals(ellipse_file)
    a2, b2 = rx * rx, ry * ry

    pts = read_decimals(points_file)
    for i in range(0, len(pts) - 1, 2):
        dx = pts[i] - cx
        dy = pts[i + 1] - cy
        left = (dx * dx) * b2 + (dy * dy) * a2
        right = a2 * b2
        print(0 if left == right else (1 if left < right else 2))


if __name__ == '__main__':
    main()
