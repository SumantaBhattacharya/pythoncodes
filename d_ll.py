class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.prevval = None
        self.nextval = None

class DoublyLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def insert_at_end(self, newdata):
        newnode = Node(newdata)
        if self.headval is None:
            self.headval = newnode
            return
        lastval = self.headval
        while lastval.nextval:
            lastval = lastval.nextval
        lastval.nextval = newnode
        newnode.prevval = lastval

# Create a doubly linked list
dllist = DoublyLinkedList()
dllist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link nodes backward
dllist.headval.nextval = e2
e2.nextval = e3
e2.prevval = dllist.headval
e3.prevval = e2

# Insert a new node at the end
dllist.insert_at_end("Thu")

# Print the doubly linked list forward
dllist.listprint()
