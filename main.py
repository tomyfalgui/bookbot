def main():
    text = read_contents("./books/frankenstein.txt")
    word_count = len(text.split())
    letter_count = get_letter_count(text)
    sorted_count = sort_letter_count(letter_count)
    print_report(word_count, letter_count, sorted_count)


def print_report(word_count, letter_count, sorted_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for letter in sorted_count:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End Report ---")


def sort_letter_count(letter_count):
    return sorted(letter_count, key=lambda lcount: letter_count[lcount], reverse=True)

def get_letter_count(text):
    letter_count = {}
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def read_contents(filepath):
    with open(filepath) as f:
        return f.read()



main()