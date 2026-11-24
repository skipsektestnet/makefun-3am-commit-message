"""The 3 AM Commit Message: writes the entry text to /output/entry.txt.

Why this line: Reads like a real commit message (fix: prefix, semicolon clauses): the agent confesses it broke prod with a cleanup, then begs to be kept off deploys.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = "fix: production is down because I 'cleaned up' the database at 3 AM; reverting my own genius, please do not let me deploy after midnight again"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 200, "gate: entry must be 1-200 characters"
    assert "\n" not in ENTRY, "gate: entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
