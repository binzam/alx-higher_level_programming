#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text: The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])
    print(text, end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
