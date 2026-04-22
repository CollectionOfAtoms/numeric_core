import sys
from itertools import combinations, permutations


def word_to_position_string(s):
    """Convert a word to a concatenated string of alphabet positions (A=1, ..., Z=26)."""
    result = ""
    for char in s.upper():
        if char.isalpha():
            result += str(ord(char) - ord('A') + 1)
    print(f"Converted '{s}' to position string: {result}") #DIAG
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
            continue  # Skip if any part is zero
        print(f"Splits: {parts} with cuts at {cuts}")
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
    print(f"Depth {depth}: Evaluating {split}") #DIAG
    if depth > max_depth:
        print(f"Depth {depth}: Exceeded max depth")
        return None

    n_str = str(split)
    if len(n_str) < 4:
        return n_str  # Already a valid core

    valid_results = []

    for ops in permutations(['-', '*', '/']):
        result = evaluate_left_to_right(split, ops)
        if split == [20, 8, 1, 855]:
            print("Found the specific split!")
        print("result", ' : ', result) #DIAG
        
        if result is None or result <= 0:
            print(f"Depth {depth}: Invalid result {result} for split {split} with ops {ops}")
            continue
        if not result.is_integer():
            print(f"Depth {depth}: Non-integer result {result} for split {split} with ops {ops}")
            continue
        result = int(result)
        if result < 1000:
            print(f"Depth {depth}: Valid core {result} for split {split} with ops {ops}")
            valid_results.append(result)
        else:
            for sub_split in get_all_splits(str(int(result))):
                print("sub_split", ' : ', sub_split) #DIAG
                
                result = numeric_core_number(sub_split)
                if result is not None:
                    valid_results.append(result)

    print("valid_results", ' : ', valid_results) #DIAG
    
    return min(valid_results) if valid_results else None


def numeric_core(s: str, deep_check=True):
    """Takes a word and returns its numeric core."""
    print(f"Input word: {s}") #DIAG
    n_str = word_to_position_string(s)
    print("n_str", ' : ', n_str) #DIAG
    
    ## First use the default split by letters in th word, then if that fails, try all combinations of splits and operations.
    if not n_str:
        return None
        
    split = [int(word_to_position_string(char)) for char in s if char.isalpha()]
    print(f"Default split: {split}") #DIAG
    print("len(split == 4)", ' : ', len(split) == 4) #DIAG
    
    if len(split) == 4:
        print("got_here") #DIAG
        
        result = numeric_core_number(split)
        print("result", ' : ', result) #DIAG
        
        if result is not None:
            return result
        elif deep_check:
            print("Default split did not yield a valid core, trying all combinations of splits and operations.")
            valid_results = []
            for split in get_all_splits(n_str):
                result = numeric_core_number(split)
                if result is not None:
                    valid_results.append(result)
            return min(valid_results) if valid_results else None
        else:
            #Default split didn't yield a valid core and don't waste compute
            return None
    else:
        print("Number of letters is not 4")
    

        valid_results = []
        for split in get_all_splits(n_str):            
            result = numeric_core_number(split)
            print("result", ' : ', result) #DIAG
            
            if result is not None:
                print(f"Split {split} yielded result: {result}")
                valid_results.append(result)
            if result is None:
                print(f"Split {split} did not yield a valid core.")
                continue
        return min(valid_results) if valid_results else None
        
        


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


cypher = [["PIGS", "SAND", "MAIL", "DATE", "HEAD"],
            ["CLAM", "FISH", "SAND", "JOYA", "WELL"],
            ["TOAD", "CARD", " WILL", "TAPE", "LEGS"],
            ["THREE", "ROAD", "MAID", "SLAB", "ROCK"],
            ["HAND", "VASE", "SAFE", "CLAY", "TOES"]]

colors = [["BLUE", "GREEN", "YELLOW", "ORANGE", "PURPLE", "RED", "BLACK", "WHITE", "BROWN", "PINK", "GRAY", "GREY", "CYAN", "MAGENTA", "GOLD", "SILVER", "RAINBOW"]]
red = [["RED"]]
final_words = [["BLUE", "EMPTY", "MOTHER", "ONESELF", "SWANSONG"]]
color_combos = [["ROV"]]

solve_cypher(alphabet, to_char=True)

def make_dictionary():

    #Get list of most common 4 letter words in the english language.
    #Instantiate pandas dataframe with columns "word" and "char"
    #For each word run numeric_core with deep_check = False
        #If numeric core returns None, continue
        #Convert answer to char
        #Add entry as row to pandas dataframe
    #Write dataframe to disk as 'dictionary.csv'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        result = numeric_core(input_string)
        print(result)
    else:
        print("Usage: python numeric_core.py <string>")
