from utils import soundex
from utils import lev_distance
import os


def sdx_code_map():
    abs_path = os.getcwd()
    with open(os.path.join(abs_path, "dictionary.txt"), "r") as dict_file:
        line = dict_file.readline()
        stack_for_words = {}
        while line:
            sdx_of_word = soundex(line)
            if sdx_of_word in stack_for_words:
                stack_for_words[sdx_of_word].append(line[:-1])
            else:
                stack_for_words[sdx_of_word] = [line[:-1]]
            line = dict_file.readline()
    return stack_for_words


def final_words(str1):
    result = sdx_code_map()
    sdx_of_str1 = soundex(str1)
    for key, values in result.items():
        if key == sdx_of_str1:
            return ",".join(word for word in values if lev_distance(str1, word) <= 2)
