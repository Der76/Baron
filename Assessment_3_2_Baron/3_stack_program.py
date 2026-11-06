# Author: Baron
# Program 3: Stack - Last In, First Out (LIFO)
# Linear data structure: Stack
# The program pushes every letter of a word onto the stack,
# then pops the letters from the top until the stack is empty.
# The last letter pushed is the first letter popped.


def show_stack(letters):
    """Return the stack as text, the top item is the last one on the right."""
    return "[" + ", ".join(letters) + "]"


def get_word():
    """Keep asking until the user types a valid word (letters only)."""
    while True:
        word = input("Enter a word (example: BARON): ").strip()
        if word == "":
            print("Invalid input. The word cannot be empty.")
        elif not word.isalpha():
            print("Invalid input. Please use letters only (no numbers or spaces).")
        else:
            return word.upper()


def main():
    word = get_word()
    stack = []  # the empty stack
    print()

    # Step 1: Push each letter onto the top of the stack
    for letter in word:
        stack.append(letter)  # append() adds to the top
        print("Push " + letter + ":", show_stack(stack))

    print()

    # Step 2: Pop the top letter again and again until the stack is empty
    while len(stack) > 0:
        top = stack.pop()  # pop() removes the top (last) item
        print("Pop " + top + ":", show_stack(stack))

    # Step 3: Show the final result
    print("Result: EMPTY")


main()
