class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linkedlist(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data,"-->",end="")
                self.head = self.head.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head 
        while n is not None:
             if x==n.data:
              break
             else:
              n=n.ref
        if x is None: #if the data of linked list isnt found then it will print thr message
              print("node is not present in the linked list")
              
        else:
            new_node=Node(data) 
            new_node.ref=n.ref
              #there is a difference between new_node and new_node.ref is that  new_node implies the link part of the previous node and new_node.ref implies the reference of the forward node 
            n.ref=new_node

   


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(100)
LL1.add_after(200,10)#i want to add 200 after 100
LL1.add_end(68)

LL1.print_linkedlist()
