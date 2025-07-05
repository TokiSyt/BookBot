import string
from typing import Dict

alphabet: Dict[str, str] = {letter: letter for letter in string.ascii_lowercase}


def organization(text: str, user_input: str) -> None:
    letter_counts = letters_counted(text)

    if user_input == "all":
        for letter in alphabet:
            count = letter_counts.get(letter, 0)
            print(
                f"The letter {letter} appears {count} times."
                + ("\n" if letter != "z" else "")
            )
    elif user_input in alphabet:
        count = letter_counts.get(user_input, 0)
        print(f"The letter {user_input} appears {count} times.")


def words_option() -> str:
    while True:
        checker_words = input(
            "Do you wish to see how many words this script contain in total? (y/n)\n"
        ).lower()
        if checker_words in {"y", "n"}:
            return checker_words
        print('Please enter "y" or "n".')


def letters_option() -> str:
    while True:
        checker_letters = input(
            """\nRegarding a letters count, how many letters do you wish to see:
    Zero - No letters.
    All - All letters.
    Single letter from A to Z - That letter count.
    
    Answer here: """
        ).lower()

        if checker_letters in alphabet or checker_letters in {"zero", "all"}:
            return checker_letters
        print('Please enter "Zero", "All", or a single letter from the alphabet.')


def get_book_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main() -> None:
    book_path = "shrek.txt"
    book = get_book_text(book_path)

    checker_words = words_option()
    checker_letters = letters_option()

    print("\n--- Begin report of Shrek Script ---\n")

    if checker_words == "y":
        counted_words(book)
    else:
        print("Words count display skipped.\n")

    if checker_letters == "zero":
        print("Letters count display skipped.")
    else:
        organization(book, checker_letters)

    if checker_words == "n" and checker_letters == "zero":
        print("No information to print.")

    print("\n--- End report ---")


def counted_words(text: str) -> None:
    word_count = len(text.split())
    print(f"{word_count} words found in the selected document.\n")


def letters_counted(text: str) -> Dict[str, int]:
    text = text.lower()
    letter_counts: Dict[str, int] = {}

    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts


if __name__ == "__main__":
    main()
