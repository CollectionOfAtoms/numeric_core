import pandas as pd
from wordfreq import top_n_list
from core import numeric_core
from cipher import number_2_letter


def make_dictionary():
    """Build a CSV mapping the ~2000 most common 4-letter English words to their numeric core character."""
    raw = top_n_list('en', 200000)
    four_letter_words = [w.upper() for w in raw if len(w) == 4 and w.isalpha()][:2000]

    rows = []
    for word in four_letter_words:
        result = numeric_core(word, deep_check=False)
        if result is None:
            continue
        char = number_2_letter(result)
        if char is None:
            continue
        rows.append({"word": word, "char": char})

    df = pd.DataFrame(rows, columns=["word", "char"])
    df.to_csv("dictionary.csv", index=False)
    print(f"Dictionary written: {len(df)} entries -> dictionary.csv")
    return df

if __name__ == "__main__":
    make_dictionary()