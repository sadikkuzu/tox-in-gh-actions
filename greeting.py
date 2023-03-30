from __future__ import annotations

import sys


def hello(name: str) -> None:
    print(f"hello {name}")


def main() -> int:
    hello(sys.argv[-1])
    return 0


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
