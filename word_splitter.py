"""Example of how to split a text file into words.

It doesn't take into account punctuation, but only splits on whitespace.
"""


f = open('text.txt', 'r')
text = f.read()
f.close()

words = text.split()
print(words)

