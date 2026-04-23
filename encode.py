import csv
import random
import sys
from collections import defaultdict


def load_lookup(csv_path="dictionary.csv"):
    """Build a char -> [words] lookup table from dictionary.csv."""
    lookup = defaultdict(list)
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            lookup[row["char"]].append(row["word"])
    return lookup


def encode(message, lookup):
    """Encode a plaintext message into a cipher grid using the lookup table.

    Each character in the message maps to a randomly selected word whose
    numeric core resolves to that character. Characters with no candidates
    are represented as '????' in the output.
    """
    rows = []
    for line in message.strip().splitlines():
        words = []
        for char in line.upper():
            candidates = lookup.get(char, [])
            words.append(random.choice(candidates) if candidates else "????")
        rows.append(" ".join(words))
    return rows


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python encode.py <message_file> [output_file]")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        message = f.read()

    lookup = load_lookup()
    rows = encode(message, lookup)
    output = "\n".join(rows)

    print(output)

    if len(sys.argv) >= 3:
        with open(sys.argv[2], "w") as f:
            f.write(output + "\n")
