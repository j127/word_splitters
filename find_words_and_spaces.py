"""Takes an alphabetic string and returns all words with any adjacent spaces."""
import re


# The text to process. This could be read from a file.
s = 'Saluton, Mondo! Mi estas komputilo.'
print('Original text: {}'.format(s))


def has_leading_space(word, text):
    """Returns True if word has a leading space."""
    word_start = text.index(word)
    return text[word_start-1] == ' '


def has_trailing_space(word, text):
    """Returns True if word has a trailing space."""
    word_start = text.index(word)
    word_end = word_start + len(word)
    return text[word_end] == ' '


def extract_words(text):
    # Extracts words without punctuation
    p = re.compile(r'(\b[a-zA-Z]{1,}\b)')
    words = re.findall(p, text)
    print('Extracted words: {}'.format(words))
    return words


def pad_words(words, text):
    words_with_spaces = []

    for word in words:
        word_index = text.index(word)
        leading_space = has_leading_space(word, text)
        trailing_space = has_trailing_space(word, text)
        print('Word: "{}", Leading: {}, Trailing: {}'.format(word, leading_space, trailing_space))
        if leading_space is True:
            word = ' {}'.format(word)
        if trailing_space is True:
            word = '{} '.format(word)
        words_with_spaces.append(word)
    print('Words with spaces: {}'.format(words_with_spaces))
    return words_with_spaces


def main():
    """Runs the program."""
    pad_words(extract_words(s), s)


if __name__ == '__main__':
    main()

