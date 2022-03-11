# Task 3
# Something old in a new way :).
# Self-study positional arguments for Python scripts (sys.argv).
# Write a script that takes a list of words (or even phrases)
# Script should ask a user to write something to stdin until user won't provide one of argument phrases.

import sys

arg_list = sys.argv

while True:
    phrase = input("Enter a word or a phrase: ")
    if phrase in arg_list:
        break
