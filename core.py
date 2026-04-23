from itertools import combinations, permutations


def word_to_position_string(s):
    """Convert a word to a concatenated string of alphabet positions (A=1, ..., Z=26)."""
    result = ""
    for char in s.upper():
        if char.isalpha():
            result += str(ord(char) - ord('A') + 1)
    return result


def get_all_splits(n_str, num_parts=4):
    """Yield all ways to split n_str into exactly num_parts non-empty substrings."""
    n = len(n_str)
    if n < num_parts:
        return

    for cuts in combinations(range(1, n), num_parts - 1):
        parts = []
        prev = 0
        for cut in cuts:
            parts.append(int(n_str[prev:cut]))
            prev = cut
        parts.append(int(n_str[prev:]))
        if any(part == 0 for part in parts):
            continue
        yield parts


def evaluate_left_to_right(numbers, ops):
    """Evaluate numbers left-to-right with ops. Returns None on division by zero."""
    result = float(numbers[0])
    for num, op in zip(numbers[1:], ops):
        if op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if num == 0:
                return None
            result /= num
    return result


def numeric_core_number(split, depth=0, max_depth=15):
    """Recursively find the numeric core: smallest positive whole number < 1000."""
    if depth > max_depth:
        return None

    n_str = str(split)
    if len(n_str) < 4:
        return n_str  # Already a valid core

    valid_results = []

    for ops in permutations(['-', '*', '/']):
        result = evaluate_left_to_right(split, ops)

        if result is None or result <= 0:
            continue
        if not result.is_integer():
            continue
        result = int(result)
        if result < 1000:
            valid_results.append(result)
        else:
            for sub_split in get_all_splits(str(int(result))):
                result = numeric_core_number(sub_split)
                if result is not None:
                    valid_results.append(result)

    return min(valid_results) if valid_results else None


def numeric_core(s: str, deep_check=True):
    """Takes a word and returns its numeric core."""
    n_str = word_to_position_string(s)

    ## First use the default split by letters in the word, then if that fails, try all combinations of splits and operations.
    if not n_str:
        return None

    split = [int(word_to_position_string(char)) for char in s if char.isalpha()]

    if len(split) == 4:
        result = numeric_core_number(split)
        if result is not None:
            return result
        elif deep_check:
            valid_results = []
            for split in get_all_splits(n_str):
                result = numeric_core_number(split)
                if result is not None:
                    valid_results.append(result)
            return min(valid_results) if valid_results else None
        else:
            return None
    else:
        valid_results = []
        for split in get_all_splits(n_str):
            result = numeric_core_number(split)
            if result is not None:
                valid_results.append(result)
        return min(valid_results) if valid_results else None
