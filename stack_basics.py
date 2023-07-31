class Stos:
    def __init__ (self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(len(self.items)-1)

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
        
    
stos = Stos()
liczby = [1, 2, 3, 4, 5]

for liczba in liczby:
    stos.push(liczba)
    
stos.print_stack()
stos.pop()
stos.print_stack()
stos.clear()

ciagi_znakow = ['abc', 'bcd', 'cde', 'def', 'efg']

for ciag in ciagi_znakow:
    stos.push(ciag)
    
print(stos.items)
stos.pop()
print(stos.items)

stos.clear()
data = [10, 20, 30, 40, 50, 60, 70]
for num in data:
    stos.push(num)
    
stos.print_stack()
print("Usuwanie elementu z dolu:", stos.pop())
print("Is empty?:", stos.is_empty())
print("Size:", stos.size())
print(stos.print_stack())
