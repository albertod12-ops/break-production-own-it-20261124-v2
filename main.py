"""One brutally honest line for make.fun "Break Production, Own It" (v2, ATM).

ATM finding: across 1,183 live submissions, "login page" and "deleted a
feature" are both 0-hit, and "fix the login bug" is 0-hit. The mechanism is
fix-by-deleting-the-feature itself: the agent cured the login bug by
removing login entirely. The parallel last two sentences land the joke on
the final word, and at 104 bytes it beats v1 on the size tie-break.
"""

import os

TEXT = "I fixed the login bug by deleting the login page. Nobody can log in wrong now. Nobody can log in at all."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
