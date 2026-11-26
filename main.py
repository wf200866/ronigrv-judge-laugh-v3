import os

# The joke: a bug that shipped on time and a fix that is still one task away
# from even being agreed to be a bug.
JOKE = (
    "The bug shipped on time. The fix is blocked on a task "
    "to decide whether the bug is a bug."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # The sandbox collects the output as another user; 0600 would be unreadable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
