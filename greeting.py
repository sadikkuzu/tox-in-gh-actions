from __future__ import annotations

import sys


def hello(name: str) -> None:
    print(f"hello {name}")


def main() -> int:
    hello(sys.argv[1])


if __name__ == '__main__':
    raise SystemExit(main())
