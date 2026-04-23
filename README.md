# Numeric Core

A cipher toolkit built around the **numeric core** puzzle mechanic from the video game [Blue Prince](https://store.steampowered.com/app/1569580/Blue_Prince/).

## How it works

Each letter in a word is converted to its alphabet position (A=1, B=2, ... Z=26), producing a list of four numbers. Those numbers are then combined using arithmetic operations (subtraction, multiplication, division) applied left-to-right across all permutations until the result is a positive whole number less than 1000. The smallest such result is the **numeric core**. That number maps back to a letter (1=A, 2=B, ..., 26=Z), allowing words to encode characters.

```
PIGS → [16, 9, 7, 19] → 16 * 9 - 7 / 19 ... → 19 → S
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Tools

### `cipher.py` — Decode a cipher

Reads a grid of words (one row per line, words space-separated) and resolves each word to its numeric core character. Unresolvable words print as `?`, and punctuation passes through unchanged.

```bash
python cipher.py <input_file> [output_file]
```

**Example** — decode `cipher.txt`:
```
$ python cipher.py cipher.txt
```

---

### `encode.py` — Encode a message

Reads a plaintext message and encodes each character as a randomly selected word from the dictionary whose numeric core resolves to that character. Spaces in the input become line breaks in the cipher. Punctuation passes through as-is.

```bash
python encode.py <message_file> [output_file]
```

**Example** — encode `message.txt` containing `HELLO WORLD`:
```
$ python encode.py message.txt

HEAT EVER LEGS LEGS OBEY
WEST OBEY ROAD LEGS DULY
```

Decoding that output with `cipher.py` recovers the original message.

---

### `dictionary.py` — Rebuild the word dictionary

Generates `dictionary.csv`, a lookup table mapping the most common 4-letter English words to their numeric core characters. Used internally by `encode.py`.

```bash
python dictionary.py
```

---

### `numeric_core.py` — Single-word CLI

Computes the numeric core of a single word.

```bash
python numeric_core.py <word>
```

```
$ python numeric_core.py PIGS
19
```

## File structure

```
core.py          # Numeric core computation engine
cipher.py        # Decode cipher grids
encode.py        # Encode plaintext messages
dictionary.py    # Regenerate dictionary.csv
numeric_core.py  # Single-word CLI
dictionary.csv   # Pre-built word → character lookup table
```
