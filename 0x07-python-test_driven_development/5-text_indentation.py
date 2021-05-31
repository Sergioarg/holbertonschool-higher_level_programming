#!/usr/bin/python3
"""Moduele for print text whit two new lines"""


def text_indentation(text):
    """Fuction to add new lines"""

    if (type(text) != str):
        raise TypeError("text must be a string")
    text_mod = text.translate({46: '.\n\n', 58: ':\n\n', 63: '?\n\n'})

    text_mod = text_mod.splitlines()
    for i, line in enumerate(text_mod):
        if (i != 0):
            print("")
        print(line.strip(), end="")
