import re

def has_leading_space(word):
    """Returns True if word has a leading space."""
    word_start = text.index(word)
    return text[word_start-1] == ' '

def has_trailing_space(word):
    """Returns True if word has a trailing space."""
    word_start = text.index(word)
    word_end = word_start + len(word)
    return text[word_end] == ' '

# The text to process
text = 'Saluton, Mondo! Mi estas komputilo.'
print('Original text: {}'.format(text))

# Extracts words without punctuation
p = re.compile(r'(\b[a-zA-Z]{1,}\b)')

words = re.findall(p, text)
print('Extracted words: {}'.format(words))

words_with_spaces = []

for word in words:
    start = text.index(word[0])
    end = text.index(word[len(word)-1])

    word_index = text.index(word)

    leading_space = has_leading_space(word)
    trailing_space = has_trailing_space(word)
    print('Word: {}, Leading: {}, Trailing: {}'.format(word, leading_space, trailing_space))
    if leading_space is True:
        word = ' {}'.format(word)
    if trailing_space is True:
        word = '{} '.format(word)
    words_with_spaces.append(word)

print('Words with spaces: {}'.format(words_with_spaces))

