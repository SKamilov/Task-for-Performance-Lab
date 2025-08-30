import sys
from typing import List


LIMIT = 20


def minimal_moves(nums: List[int]) -> int:
    if not nums:
        return 0
    a = sorted(nums)
    m = a[len(a)//2]
    return sum(abs(x - m) for x in a)


def read_ints_from_file(path: str) -> List[int]:
    with open(path, 'r', encoding='utf-8') as f:
        return [int(x) for x in f.read().split()]


def main(argv: List[str]) -> int:
    if len(argv) == 1:
        path = 'input.txt'
    elif len(argv) == 2:
        path = argv[1]
    else:
        sys.stderr.write("Укажите путь к файлу: python task4.py <path>\n")
        return 1
    try:
        nums = read_ints_from_file(path)
    except FileNotFoundError:
        sys.stderr.write("Файл не найден\n")
        return 1
    except ValueError:
        sys.stderr.write("Некорректные данные во входном файле\n")
        return 1

    moves = minimal_moves(nums)
    if moves <= LIMIT:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
