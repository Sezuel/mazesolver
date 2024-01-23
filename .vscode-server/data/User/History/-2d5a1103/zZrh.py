def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    letters = letter_counter(words)
    sorted_letters = [letters.keys()]
    sorted_letters.sort*()
    print("--- Being report of books/rankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")


def letter_counter(words):
    letter_count = {}
    for word in words:
        letters = [*word.lower()]
        for letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

main()