from core import numeric_core


def number_2_letter(n):
    """Converts a number to its corresponding letter. 1=A, 2=B, ..., 26=Z"""
    if 1 <= n <= 26:
        return chr(n + ord('A') - 1)
    else:
        return None


def solve_cypher(cypher, to_char=True):
    """Solves the cypher by taking the numeric core of each word and converting to a letter."""

    cypher_message = []
    for row in cypher:
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
        cypher_message.append(row_cores)

    for row in cypher_message:
        print(row)
