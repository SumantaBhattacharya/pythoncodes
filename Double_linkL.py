class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  # next reference
        self.pref = None  # previous reference


class Double_ll:
    def __init__(self):
        self.head = None

    def print_ll_FORWARD(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            current = current.nref

    def print_ll_Backward(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            current = self.head
            while current.nref is not None:
                current = current.nref
            while current is not None:
                print(current.data, end="")
                current = current.pref

    def insert_at_end(self, data1, data2=None):
        newnode = Node(data1)
        if data2 is not None:
            newnode = Node((data1, data2))

        if self.head is None:
            self.head = newnode
            return

        lastval = self.head
        while lastval.nref:
            lastval = lastval.nref

        lastval.nref = newnode
        newnode.pref = lastval

# Create a doubly linked list with mixed data types
dllist = Double_ll()
dllist.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link nodes forward
dllist.head.nref = e2
e2.pref = dllist.head
e2.nref = e3
e3.pref = e2

# Insert a new node at the end
dllist.insert_at_end("Thu")
dllist.insert_at_end("Fri", "Friday")

# Print the doubly linked list forward
dllist.print_ll_FORWARD()
print()

# Print the doubly linked list backward
dllist.print_ll_Backward()
