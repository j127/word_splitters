"""Example of how to split a text file into words.

Finds alphanumeric words and pads each one with whitespace.
"""
import re


def extract_words(text):
    # Extracts words without punctuation
    p = re.compile(r'(\b[a-zA-Z0-9]{1,}\b)')
    words = re.findall(p, text)
    print('Extracted words: {}'.format(words))
    return words


def pad_words(words):
    padded_words = []
    for word in words:
        padded_words.append(' {} '.format(word))
    return padded_words


def main():
    # Get the text out of the file
    with open('text.txt', 'r') as f:
        s = f.read()
    output = pad_words(extract_words(s))
    print('Output: {}'.format(output))


if __name__ == '__main__':
    main()

