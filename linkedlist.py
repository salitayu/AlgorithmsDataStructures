class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    # def __init__(self, data, next):
    #     self.data = data
    #     self.next = next
    def __str__(self):
        return self.data
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
class UnorderedList:
    def __init__(self, head = None):
        self.head = head
    def __len__(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())