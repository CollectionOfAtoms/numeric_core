import sys
from core import numeric_core
from cipher import solve_cypher


cypher = [["PIGS", "SAND", "MAIL", "DATE", "HEAD"],
          ["CLAM", "FISH", "SAND", "JOYA", "WELL"],
          ["TOAD", "CARD", " WILL", "TAPE", "LEGS"],
          ["THREE", "ROAD", "MAID", "SLAB", "ROCK"],
          ["HAND", "VASE", "SAFE", "CLAY", "TOES"]]

colors = [["BLUE", "GREEN", "YELLOW", "ORANGE", "PURPLE", "RED", "BLACK", "WHITE", "BROWN", "PINK", "GRAY", "GREY", "CYAN", "MAGENTA", "GOLD", "SILVER", "RAINBOW"]]
red = [["RED"]]
final_words = [["BLUE", "EMPTY", "MOTHER", "ONESELF", "SWANSONG"]]
color_combos = [["ROV"]]

if __name__ == "__main__":
    # NOTE: The original file had `solve_cypher(alphabet, to_char=True)` at module
    # level but `alphabet` was never defined. Moved here and commented out pending
    # clarification of intent. Most likely candidate: solve_cypher(color_combos, to_char=True)
    # solve_cypher(alphabet, to_char=True)

    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        result = numeric_core(input_string)
        print(result)
    else:
        print("Usage: python numeric_core.py <string>")
