# Author: Baron
# Program 1: Array (Python list)
# Linear data structure: Array / List
# The program adds every letter of a word into an array,
# then removes the letters one by one from the front until the array is empty.


def show_array(letters):
    """Return the array as text, example: [S, A, M]"""
    return "[" + ", ".join(letters) + "]"


def get_word():
    """Keep asking until the user types a valid word (letters only)."""
    while True:
        word = input("Enter a word (example: Baron): ").strip()
        if word == "":
            print("Invalid input. The word cannot be empty.")
        elif not word.isalpha():
            print("Invalid input. Please use letters only (no numbers or spaces).")
        else:
            return word.upper()


def main():
    word = get_word()
    array = []  # the empty array

    # Step 1: Add each letter of the word to the array
    for letter in word:
        array.append(letter)
    print()
    print("Add:", show_array(array))

    # Step 2: Remove the first letter again and again until the array is empty
    while len(array) > 0:
        removed = array.pop(0)  # pop(0) removes the item at the front
        print("Remove " + removed + ":", show_array(array))

    # Step 3: Show the final result
    print("Result: EMPTY")


main()
