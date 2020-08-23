#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Timothy La (tla111), Received help from Joseph"

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    new_dict = {}
    with open("books/small.txt", "r") as f:
        # f.read()
        for line in f:
            new_list = line.split()
            for word in new_list:
                word = word.lower()
                if word not in new_dict:
                    new_dict[word] = 1
                else:
                    new_dict[word] += 1
        return new_dict


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    # This function would print the words in a dictionary line by line
    # {
    # "the": 5
    # "they": 6
    # "house": 3
    # }
    call_dict_func = create_word_dict(filename)
    alphabetical_list_of_tuples = sorted(
        call_dict_func.items(), key=lambda x: x[0])  # x is tuple
    for k, v in alphabetical_list_of_tuples:
        print(f"{k}:{v}")


def print_top(filename):
    """Prints the top count listing for the given file."""
    # This function would sort the words in the dictionary
    # by the frequency of occurrence
    # Ex: {"the": 5, "he": 4, "she": 3}

    # top 20 of most occurrence
    call_dict_func = create_word_dict(filename)
    print(call_dict_func)


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
