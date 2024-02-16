class Stack:
    def __init__(self):  # Konstruktor
        self.items = []

    def push(self, item):  # Dodawanie elementu
        self.items.append(item)

    def pop(self):  # Usuwanie elementu
        if self.is_empty():
            return None

        return self.items.pop(len(self.items) - 1)

    def peek(self):
        if self.is_empty():
            return None

        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return 1

        else:
            return 0

    def print_stack(self):
        for elem in self.items:
            print(elem, end=' ')

        print()


def check_brackets_ext(seq):
    brackets = Stack()
    brackets_reversed = {'(': ')', '[': ']', '{': '}'}

    if len(seq) == 0:
        return False

    for char in seq:
        if char in '([{':
            brackets.push(znak)
        elif char in ')]}' and not brackets.is_empty():
            if char == brackets_reversed[brackets.items[len(brackets.items) - 1]]:
                brackets.pop()
        else:
            brackets.clear()
            return False

    if brackets.is_empty():
        return True
    else:
        brackets.clear()
        return False


data = input("Wprowadz ciag okraglych, kwadratowych i klamrowych nawiasow:")
print(check_brackets_ext(data))
