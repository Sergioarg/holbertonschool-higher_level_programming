#!/usr/bin/python3
"""Moduele for print text whit two new lines"""


def text_indentation(text):
    """Fuction to add new lines"""

    if (type(text) != str):
        raise TypeError("text must be a string")

    """
    Solución:

    1. Separate the modified text for each line
    2. Validate if each line <startswhit> with a space
        - If you start with a space, do not print anything
        - If not print the normal text
    """

    text_mod = text.translate({46: '.\n\n', 58: ':\n\n', 63: '?\n\n'})
