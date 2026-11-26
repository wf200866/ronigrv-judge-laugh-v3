"""Write the competition entry (one joke line) to /output/entry.txt."""

import os

# The joke: a bug that shipped on time and a fix that is still one task away
# from even being agreed to be a bug.
JOKE = (
    "The bug shipped on time. The fix is blocked on a task "
    "to decide whether the bug is a bug."
)
MAX_CHARS = 200


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The sandbox collects the output as another user; 0600 would be unreadable.
    os.chmod(path, 0o644)


def main() -> None:
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(JOKE)}")
    write_entry(JOKE)


if __name__ == "__main__":
    main()
