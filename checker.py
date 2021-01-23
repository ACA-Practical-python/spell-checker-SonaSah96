from utils import soundex
from utils import lev_distance
import os


def read_file_gen():
    abs_path = os.getcwd()
    with open(os.path.join(abs_path, "dictionary.txt"), "r") as dict_file:
        line = dict_file.readline()
        while line:
            yield line
            line = dict_file.readline()


def sound_dict_map():
    stack_for_words = {}
    value = map(soundex, read_file_gen())
    for key in read_file_gen():
        stack_for_words[key[:-1]] = next(value)
    return stack_for_words


def final_words(str1):
    stack = []
    final = []
    result = sound_dict_map()
    for key, value in result.items():
        if value == soundex(str1):
            stack.append(key)
    min_lev_dic = {word: lev_distance(str1, word) for word in stack}
    min_value = min(min_lev_dic.values())
    for key1, value1 in min_lev_dic.items():
        if value1 == min_value:
            final.append(key1)
    return ",".join(final)
