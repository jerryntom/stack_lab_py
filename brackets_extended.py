class Stos:
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


def check_brackets_ext(ciag):
    nawiasy = Stos()
    nawiasy_odwrocone = {'(': ')', '[': ']', '{': '}'}

    if len(ciag) == 0:
        return False

    for znak in ciag:
        if znak in '([{':
            nawiasy.push(znak)
        elif znak in ')]}' and not nawiasy.is_empty():
            if znak == nawiasy_odwrocone[nawiasy.items[len(nawiasy.items) - 1]]:
                nawiasy.pop()
        else:
            nawiasy.clear()
            return False

    if nawiasy.is_empty():
        return True
    else:
        nawiasy.clear()
        return False


dane = input("Wprowadz ciag okraglych, kwadratowych i klamrowych nawiasow:")
print(check_brackets_ext(dane))
