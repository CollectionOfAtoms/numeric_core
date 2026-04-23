import sys
from core import numeric_core
from cipher import number_2_letter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python numeric_core.py <word|number>")
        sys.exit(1)

    arg = sys.argv[1]
    if arg.isdigit():
        print(number_2_letter(int(arg)))
    else:
        print(numeric_core(arg))
