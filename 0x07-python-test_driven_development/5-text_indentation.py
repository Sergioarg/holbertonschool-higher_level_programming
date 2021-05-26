#!/usr/bin/python3
"""Moduele for print text whit two new lines"""


def text_indentation(text):
    """Fuction to add new lines"""

    if (type(text) != str):
        raise TypeError("text must be a string")
    else:
        text_mod = text.translate({46: '.\n\n', 58: ':\n\n', 63: '?\n\n'})
    print(text_mod, end="")
