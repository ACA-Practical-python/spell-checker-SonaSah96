from utils import lev_distance
from utils import soundex
from checker import final_words


def rep():
    print("Choose from options:\n 1.Levenshtein\n 2.Soundex\n 3.Spell correction")
    answer = input("Type 1,2 or 3: ")
    if answer == "1":
        str1 = input("First string: ")
        str2 = input("Second string: ")
        print(f'Levenshtein distance for  "{str1}" and "{str2}" is "{lev_distance(str1,str2)}"')
    elif answer == "2":
        input_str = input("Input string: ")
        print(f'Soundex code for "{input_str}" is "{soundex(input_str)}"')
    else:
        misspelled_word = input("Write misspelled word: ")
        print(f'Possible options: {final_words(misspelled_word)}')


rep()