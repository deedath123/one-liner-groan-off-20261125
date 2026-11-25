"""The One-Liner Groan-Off — make.fun entry.

A single groan-worthy one-liner: a dad, a microwave, and a daughter who
has heard quite enough. The entry is stored in ENTRY, validated by
validate(), and written to /output/entry.txt by main().
"""

ENTRY = "My daughter caught me talking to the microwave. 'Dad, it can't hear you.' 'Exactly — that's why I keep pushing its buttons.'"


def validate(entry):
    """Reject blank entries, entries over 140 UTF-8 characters, and entries
    containing newline or control characters."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if len(entry.encode("utf-8")) > 140:
        raise ValueError("entry exceeds 140 UTF-8 characters")
    for ch in entry:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("entry must not contain newline or control characters")
    return True


def confirm_entry_is_tight(entry):
    """Reject entries with stray whitespace or invisible characters:
    leading/trailing whitespace, any newline or carriage return, any
    character whose Unicode category starts with 'C', or any run of
    two or more consecutive whitespace characters."""
    import re
    import unicodedata

    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must not contain newline or carriage return")
    for ch in entry:
        if unicodedata.category(ch).startswith("C"):
            raise ValueError("entry must not contain control, format, surrogate, or private-use characters")
    if re.search(r"\s{2,}", entry):
        raise ValueError("entry must not contain consecutive whitespace")
    return True


def main():
    validate(ENTRY)
    confirm_entry_is_tight(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        stored = f.read()
    if stored != ENTRY.encode("utf-8"):
        raise ValueError("stored entry bytes differ from ENTRY")
    print("entry written to /output/entry.txt")


if __name__ == "__main__":
    main()
