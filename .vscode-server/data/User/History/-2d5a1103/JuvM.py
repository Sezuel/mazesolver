with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
word_count = 0
for word in words:
    word_count += 1
print(word_count)