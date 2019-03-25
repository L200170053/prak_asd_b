class node(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def cariLinkedList(self, dicari):
        curNode = self
        while curNode is not None:
            if curNode.next != None:
                if curNode.data != dicari:
                    curNode = curNode.next
                else:
                    print ("Data", dicari, "ada dalam Linked List")
                    break
            elif curNode.next == None:
                print ("Data", dicari, "tidak ada dalam Linked List")
                break
a = node(45)
menu = a
a.next = node (9)
a = a.next
a.next = node (17)
a = a.next
a.next = node (23)

menu.cariLinkedList(9)
menu.cariLinkedList(22)
