class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__ (self):
        return len(self.qlist)
    def isEmpty(self):
        return len (self) == 0
    def enqueue (self, data, priority):
        entry = PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue (self):
        A =[]
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range (1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = 1
        hasil = self.qlist.pop(s)
        return hasil.item
class PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

S = PriorityQueue()
S.enqueue("Jeruk", 22)
S.enqueue("Tomat", 45)
S.enqueue("Mangga", 32)
S.enqueue("Delima", 18)
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
