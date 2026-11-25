"""Write one funny line for The 3AM Fridge Text bounty.

Writes the line to /output/entry.txt. Stdlib only, no network.
The joke: the fridge has been awake since 2019 and the owner still
opens it hoping a pizza grew in there overnight — a deadpan,
sleep-deprived appliance voice with a punchline that lands on
"I haven't. Go to bed."
"""

import os

ENTRY = (
    "3am. I've been awake since 2019 and you still open me like I "
    "might have grown a pizza. I haven't. Go to bed."
)


def validate_utf8(text):
    """Confirm the entry encodes cleanly as UTF-8.

    Returns the encoded bytes so callers can also check the byte length.
    Raises UnicodeEncodeError if the text is not encodable.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    return text.encode("utf-8")


def validate_length(text):
    """Enforce the kit gate: 1-140 characters, single line, non-whitespace.

    Raises ValueError with a specific message naming the failed rule, so a
    bad entry is easy to diagnose instead of failing silently.
    """
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return True


def gate_check(text):
    """Run every kit-gate validation on the entry text before it is written."""
    validate_utf8(text)
    return validate_length(text)


def self_test():
    """Small self-test: the real entry passes, and each bad input is refused.

    Checks the happy path plus one failure per gate rule, so a future edit
    that breaks validation is caught immediately instead of at submit time.
    Does not write any output file.
    """
    assert gate_check(ENTRY) is True
    assert len(ENTRY) == 108, f"entry length changed: {len(ENTRY)}"
    stats = entry_stats(ENTRY)
    assert stats == {"chars": 108, "words": 23, "non_ascii": 0}, (
        f"entry shape changed: {stats}"
    )
    assert validate_utf8(ENTRY) == ENTRY.encode("utf-8")
    assert len(validate_utf8(ENTRY)) == 108, "entry byte length changed"
    bad_cases = [
        ("", "empty entry"),
        (" " * 10, "whitespace-only entry"),
        ("x" * 141, "entry over 140 characters"),
        ("two\nlines", "multi-line entry"),
        ("two\rlines", "carriage-return entry"),
        (" padded ", "entry with surrounding whitespace"),
        ("trailing ", "trailing-space entry"),
        (" leading", "leading-space entry"),
        (123, "non-string entry"),
        (None, "none entry"),
        (b"bytes", "bytes entry"),
    ]
    for bad_text, label in bad_cases:
        try:
            gate_check(bad_text)
        except (ValueError, TypeError, UnicodeEncodeError):
            continue
        raise AssertionError(f"self-test failed: gate accepted {label}")
    return True


def write_entry(path):
    """Write the validated entry to path, exactly as-is, no trailing newline.

    The caller picks the path (the grader reads /output/entry.txt); the
    bytes written are exactly ENTRY encoded as UTF-8, so the judge sees
    the line and nothing else.
    """
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def entry_stats(text):
    """Count the entry's characters, words and non-ASCII characters.

    Used by the self-test to pin the entry's shape: a later edit that
    changes the joke changes these numbers and fails loudly instead of
    silently submitting a different line.
    """
    return {
        "chars": len(text),
        "words": len(text.split()),
        "non_ascii": sum(1 for ch in text if ord(ch) > 127),
    }


def main():
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    self_test()
    main()
