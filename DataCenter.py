import copy
import sys
from functools import reduce

from Control import WordBuilder
from model.Word import *
import csv

# word list.
__word_list = []
# version
version = "0.0.1"


# load one csv file.
def load_files(file_path):

    word_list = []
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        for lines in f:
            line = lines.rstrip()
            list = WordBuilder.build(line)
            word_list = word_list + list

    return word_list


# load wordlist_800.csv.
def load():
    global __word_list
    __word_list = load_files('wordlist_800.csv')


# get list on predicate is true. predicate is bool lambda
def get_list(predicate: object = (lambda x: True)) -> bool:
    return copy.deepcopy(list(filter(predicate, __word_list)))


if __name__ == '__main__':
    load()
