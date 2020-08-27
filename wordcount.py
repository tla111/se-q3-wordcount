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
__author__ = """
Timothy La (tla111)
Received help from Joseph for Problem 1
Received help from Coach John W for Problem 2
Solved Problem 3 on My Own!!!!!
"""

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    new_dict = {}
    with open(filename, "r") as f:
        for line in f:
            new_list = line.split()
            for word in new_list:
                word = word.lower()
                if word not in new_dict:
                    new_dict[word] = 1
                else:
                    new_dict[word] += 1
        return new_dict

# 1. Create an empty dictionary to be used later
# 2. Read the file that gets passed in and store it as f
# 3. Loop over each line in file
#       Split each word of the line and store in a list
#       Loop over each word in the list
#           Change each word to lowercase
#           Option 1: If the word is not a key in new_dict
#               Put 1 as the value of the key
#           Option 2: If the word is a key in new_dict
#               Increment the count of the value
# 4. Return new_dict to be used in other functions


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

# 1. Get the result from the create_word_dict function and store it
# 2. Sort the words in call_dict_func in abc order by the looking at
#   index[0]
# 3. Loop over the keys and value in alphabetical_list_of_tuples
# 4. Print the key and value on each line


def print_top(filename):
    """Prints the top count listing for the given file."""
    # This function would sort the words in the dictionary
    # by the frequency of occurrence
    # Ex: {"the": 5, "he": 4, "she": 3}

    # top 20 of most occurrence
    call_dict_func = create_word_dict(filename)
    sort_top_occurrences = sorted(
        call_dict_func.items(), key=lambda x: x[1], reverse=True)
    new_list = []
    for k, v in sort_top_occurrences:
        if len(new_list) < 20:
            new_list.append(f"{k},{v}")
    print(new_list)

# 1. Get the result from the create_word_dict function and store it
# 2. Sort the values of call_dict_func from descending order
# 3. Loop over the sorted words (sort_top_occurrences)
#       Option 1: If the length of new_list is less than 20
#           Add the value to new_list
# 4. Print out new_list

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
