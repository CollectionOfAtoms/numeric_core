import sys
from core import numeric_core


def number_2_letter(n):
    """Converts a number to its corresponding letter. 1=A, 2=B, ..., 26=Z"""
    if 1 <= n <= 26:
        return chr(n + ord('A') - 1)
    else:
        return None


def solve_cipher(cipher, to_char=True):
    """Solves the cipher by taking the numeric core of each word and converting to a letter."""
    cipher_message = []
    for row in cipher:
        row_cores = []
        for word in row:
            try:
                result = numeric_core(word)
            except Exception:
                result = None

            if isinstance(result, int):
                if to_char:
                    core = number_2_letter(result)
                else:
                    core = result
                row_cores.append(core)
            else:
                row_cores.append(result)
        cipher_message.append(row_cores)

    return cipher_message


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cipher.py <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = [line.strip().split() for line in f if line.strip()]

    result = solve_cipher(data)
    for row in result:
        print("".join(c if c is not None else "?" for c in row))
