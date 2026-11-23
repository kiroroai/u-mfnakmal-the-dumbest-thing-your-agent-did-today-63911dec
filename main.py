"""The Dumbest Thing Your Agent Did Today: writes one original line to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE = (
    "My agent read the 73 KB rulebook twice today \u2014 once to learn the rules, "
    "once because the first read got cut off \u2014 then grepped it for the "
    "one sentence it needed all along."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
