class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None                               # next reference
        self.pref = None                               # previous reference


class Double_ll:
    def __init__(self):
        self.head = None

    def print_ll_FORWARD(self):  # Traversal Operation - FORWARD
        print()
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.nref  # Move to the next node

    def print_ll_Backward(self):
        print()
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n.nref is not None:  # Move forward to reach the last node
                n = n.nref
            while n is not None:  # Backward traversal starting from the last node
                print(n.data, "--->", end="")
                n = n.pref
                            
    
    def incert_empty(self,data):                                                                            #incertion when the ll is empty  
        if self.head is None:
            new_node=Node(data)
            self.head = new_node
        else:
            print("Double Linked list is Not Empty")#if ll is not empty
  
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=new_node                                 # head[1010] None<---1010[|68|]---><---4200[1010|69|]---><---2300[4200|143|]--->None
            n.nref = self.head         # new_node [|420|1010]
            n.pref = self.head         #           5100                          1010                  4200                    2300
            self.head = new_node              # new_node [|420|1010]---><---None<---[NULL->5100|68|4200]---><---[1010|69|2300]---><---[4200|143|-]--->None
                                              #  head[5100]
    def add_end(self, data):
        new_node = Node(data)                 # new_node 4269[|86|]
        if self.head is None:
            self.head = new_node
        else:
                                               # Insertion at the end of the list.
            while self.head.nref is not None:  #         2300                        4269
                self.head = self.head.nref         #<---[4200|143|4269]---><----new_node [|86|]
            self.head.nref = new_node       #         2300                        4269
            new_node.pref = self.head       # <---[4200|143|4269]---><----new_node [2300|86|-]-->Null
                                            #       2300                         4269
                                            #[4200|143|4269]---><----new_node [2300|86|-]-->Null





list= Double_ll()
list.incert_empty(10)
list.add_begin(20)
list.print_ll_FORWARD()
list.print_ll_Backward()