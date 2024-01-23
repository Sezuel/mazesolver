with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
letter_count = {}
for letter in words:
    letter_count[letter] += 1

print(len(file_contents))
print(letter_count)