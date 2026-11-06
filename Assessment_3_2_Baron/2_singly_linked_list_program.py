# Author: Baron
# Program 2: Singly Linked List
# Linear data structure: Singly Linked List
# Each node stores one letter and a link (next) to the following node.
# The program adds every letter to the end of the list,
# then removes the first node (head) one by one until the list is empty.


class Node:
    """One node of the linked list."""
    def __init__(self, data):
        self.data = data  # the letter
        self.next = None  # link to the next node (None means no next node)


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # an empty list has no head

    def add_last(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:  # move to the last node
                current = current.next
            current.next = new_node

    def remove_first(self):
        """Remove the head node and return its letter."""
        removed = self.head.data
        self.head = self.head.next  # the second node becomes the head
        return removed

    def is_empty(self):
        return self.head is None

    def to_text(self):
        """Return the list as text, example: S -> A -> M -> None"""
        if self.head is None:
            return "None"
        text = ""
        current = self.head
        while current is not None:
            text += current.data + " -> "
            current = current.next
        return text + "None"


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
    linked_list = SinglyLinkedList()

    # Step 1: Add each letter as a new node
    for letter in word:
        linked_list.add_last(letter)
    print()
    print("Add:", linked_list.to_text())

    # Step 2: Remove the first node again and again until the list is empty
    while not linked_list.is_empty():
        removed = linked_list.remove_first()
        print("Remove " + removed + ":", linked_list.to_text())

    # Step 3: Show the final result
    print("Result: EMPTY")


main()
