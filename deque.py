class Deque:
    def __init__(self):
        self.deque = []
        self.size = len(self.deque)
    def update_size(self):
        self.size = len(self.deque)
    def add_front(self, item):
        self.deque.insert(0, item)
        self.update_size()
    def add_rear(self, item):
        self.deque.insert(len(self.deque), item)
        self.update_size()
    def remove_front(self):
        front = self.deque[0]
        self.deque.pop(0)
        self.update_size()
        return front
    def remove_rear(self):
        rear = self.deque[-1]
        self.deque.pop(len(self.deque)-1)
        self.update_size()
        return rear
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def print(self):
        print(self.deque)

d = Deque()
print(d.is_empty())
d.add_rear(4)
d.add_rear("dog")
d.add_front("cat")
d.add_front(True)
print(d.get_size())
print(d.is_empty())
d.add_rear(8.4)
d.remove_rear()
d.remove_front()
d.print()

def palindromeChecker(aString):
    chardeque = Deque()
    for char in aString:
        chardeque.add_rear(char)
    areEqual = True
    while chardeque.get_size() > 1 and areEqual:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        if first != last:
            areEqual = False
    return areEqual

print(palindromeChecker("lsdkhfskf"))
print(palindromeChecker("radar"))
