import sys
from core import numeric_core, get_all_splits, numeric_core_number

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python numeric_core.py <word|number>")
        sys.exit(1)

    arg = sys.argv[1]
    if arg.isdigit() and len(arg) >= 4:
        valid = [r for split in get_all_splits(arg) for r in [numeric_core_number(split)] if r is not None]
        print(min(valid) if valid else None)
    else:
        print(numeric_core(arg))
