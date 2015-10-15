"""Example of how to split a text file into words."""


f = open('text.txt', 'r')
text = f.read()
f.close()

words = []
for word in text.split():
    print(word)
    # or append to a list or whatever you want to do
    words.append(word)

# The list of words
print(words)

