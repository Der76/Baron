# Author: Baron
# Program 4: Queue - First In, First Out (FIFO)
# Linear data structure: Queue
# The program enqueues every letter of a word at the rear,
# then dequeues the letters from the front until the queue is empty.
# The first letter added is the first letter removed.

from collections import deque  # deque makes removing from the front fast


def show_queue(letters):
    """Return the queue as text, the front is the first item on the left."""
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
    queue = deque()  # the empty queue
    print()

    # Step 1: Enqueue each letter at the rear of the queue
    for letter in word:
        queue.append(letter)  # append() adds to the rear
        print("Enqueue " + letter + ":", show_queue(queue))

    print()

    # Step 2: Dequeue the front letter again and again until the queue is empty
    while len(queue) > 0:
        front = queue.popleft()  # popleft() removes the front item
        print("Dequeue " + front + ":", show_queue(queue))

    # Step 3: Show the final result
    print("Result: EMPTY")


main()
