import json
import sys


def walk(node):
    """Yield every dict in a JSON-like tree (dicts/lists)."""
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for x in node:
            yield from walk(x)


def build_map(values):
    """Collect id -> value from any nested structure that has both keys."""
    m = {}
    for obj in walk(values):
        try:
            m[int(obj['id'])] = obj['value']
        except (KeyError, TypeError, ValueError):
            pass
    return m


essential_keys = ('id',)

def fill_values(data, id2val):
    for obj in walk(data):
        try:
            i = int(obj['id'])
        except (KeyError, TypeError, ValueError):
            continue
        if i in id2val:
            obj['value'] = id2val[i]


def main() -> int:
    if len(sys.argv) == 1:
        values_path = "values.json"
        tests_path = "tests.json"
        report_path = "report.json"
    elif len(sys.argv) == 4:
        values_path, tests_path, report_path = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>", file=sys.stderr)
        return 1

    with open(values_path, 'r', encoding='utf-8') as f:
        values = json.load(f)
    with open(tests_path, 'r', encoding='utf-8') as f:
        tests = json.load(f)

    id2val = build_map(values)
    fill_values(tests, id2val)

    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(tests, f, ensure_ascii=False)

    return 0


if __name__ == '__main__':
    sys.exit(main())
