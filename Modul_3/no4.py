#NOMER 4#
class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

    def mencetak():
        curr = head
        while curr != None:
            print(curr.Data)
            if curr.Next == None:
                curr = curr
                break
            else:
                curr = curr.Next
        print("\n")
        while curr != None:
            print(curr.Data)
            curr = curr.Prev
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.Next = head
        head.Prev = newNode
        head =newNode
        return head

    def simpulAkhir(head):
        curr = head
        while curr != None:
            if curr.Next == None:
                newNode = doubly_linked(365)
                curr.Next = newNode
                newNode.Prev = curr
                return curr
            else:
                pass
            curr = curr.Next
        return curr
