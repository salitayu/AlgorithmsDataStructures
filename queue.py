class Queue:
    def __init__(self):
        self.queue = []
        self.size = len(self.queue)
    def update_size(self):
        self.size = len(self.queue)
    def enqueue(self, item):
        self.queue.append(item)
        self.update_size()
    def dequeue(self):
        dequeued = self.queue.pop(0)
        self.update_size()
        return dequeued
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def print(self):
        print(self.queue)

q = Queue()
print(q.get_size())
print(q.is_empty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size)
print(q.is_empty())
q.enqueue(8.4)
q.dequeue()
q.print()
q.dequeue()
q.print()
print(q.size)

# hot potato
def hotPotato(users, times):
    queue = Queue()
    for user in users:
        queue.enqueue(user)
    while queue.size > 1:
        for i in range(0, times):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

# printing tasks
import random
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self, currenttime):
        return currenttime - self.timestamp
def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size))
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
for i in range(10):
    simulation(3600, 10)