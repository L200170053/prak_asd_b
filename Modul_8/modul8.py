class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue (self):
        assert not self.isEmpty(), "Antrian Kosong"
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[0]
    def getRearMost (self):
        assert not self.isEmpty() , "Antrian sedang kosong"
        return self.qlist[-1]

a = Queue()
a.enqueue(31)
a.enqueue(11)
a.enqueue(41)
a.enqueue(81)

print (a.dequeue())
print (a.dequeue())

print (a.getFrontMost())
print (a.getRearMost())


