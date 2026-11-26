"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single out-of-office auto-reply to /output/entry.txt and prints
it. The line: an employee finally spends the leave days they were too
busy to take last year, all 23 of them; HR has questions; the employee
is, by definition of the message you are reading, not available to
answer them. The joke needs no name, no signature and no setup, and it
stays inside the competition gate of 1 to 160 characters on one line.
"""

import os

# The reply is built from its three beats so the structure stays visible:
# the confession (a backlog of untaken leave), the escalation (HR noticed),
# and the punchline, in which the away message performs itself.
BEATS = (
    "I'm away spending the leave days I was too busy to take last year "
    "\u2014 all 23 of them.",
    "HR has questions.",
    "I am not available to answer them.",
)

ENTRY = " ".join(BEATS)

OUTPUT_PATH = "/output/entry.txt"


def build_entry():
    return ENTRY


def check_entry(text):
    """Fail loudly rather than submit a line the sealed gate would refuse."""
    assert text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 160, "entry exceeds the 160-character gate"
    return text


def write_entry(path=OUTPUT_PATH):
    text = check_entry(build_entry())
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return text


def main():
    print(write_entry())


if __name__ == "__main__":
    main()
