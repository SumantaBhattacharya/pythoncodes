# Two ways to maintain a list in memory 1) Arrays 2) Linked List
# Types of Linked list
# 1) Single linked list : Navigation is Forward only
# 2) Double Linked list: Forward and backward navigation is possible
# 3) Circular linked list: Last element is linked to the First element
# 1) Single Linked List is a list made up of nodes that consist of two parts i) Data ii) Link
# Linked List is made up of nodes. a node contains the actual data and contains the address of next node of the list i.e link
# Suppose, we want to store a list of numbers 23,54,78,90
# we need to create 4  different nodes because we have four different numbers to store
# we need to Create a list of four different nodes.
# Each note contains the address or refference of the next node of the linked list
# In order to access the first node Of the linked list,we need a pointer.with the help of point, we can access the any node of the list.
# In Barton Lingleste is not a building data structure.
# Linked list is a chain of nodes
# Starting point of single Linked list is called head.
# Last node of single linked list stores the reference to empty value.


class Node:
    def __init__(self, data):  # Here we will don't consider reference as a parameter.
        self.data = data
        self.ref = None  # Instead of taking null value, we will take the keyword none. It is for empty value


# node1=Node(10)
# print(node1)#It will give the reference of the newly created object.


# In class we dont need to use parenthesis.That is circular open bracket circular close bracket
class LinkedList:  # To link or connect the individual nodes. We need to create another class that is linked list class.
    def __init__(self):
        self.head = None  # we are creatibg a head of linked list and assigning a value to it i.e None

    # Initially linked list will be completely empty.
    # If the head is none then.we are adding a empty node in a link list.

    # Traversal Operation
    # > Start with the head of the linked list
    #   Access the data if the head is not null
    #  > Go to next node access node data
    #  > Continue until last node
    #  > Traversal
    # i) LINKED list is empty
    # self.head is None
    # print( " LINKED list is empty")
    # ii) If it is not empty
    # self.head.data = 10 or n=self.head n.data=10
    # self.head.ref = 1410 or n.ref= 1410
    # print(n.data)
    # n=n.ref # to go to the next node of the Linked list from the first to second
    # n.data = 20
    # n.ref= 1375
    # print(n.data)
    # n=n.ref
    # n.data = 30
    # n.ref= 2100
    # print(n.data)
    # n=n.ref
    # n.data = 41
    # n.ref= NULL
    # print(n.data)
    # we use for loop when we know how many times we need to execute the loop body
    # we use while loop when we know the stopping condition
    # here we will use while loop because we know the stopping condition that is n=null

    def print_linkedlist(
        self,
    ):  # Run me performing traversal operation. We don't need to mention the data or the reference.
        if self.head is None:
            print("Linked list is empty")
        else:  # self.head is not None:
            while self.head is not None:  # if Linked list is not empty
                print(self.head.data)
                self.head = (
                    self.head.ref
                )  # to go to the next node of the Linked list from the first to second

    # Add or insert operation
    # at the beginning
    # at the end
    # between nodes
    # at the beginning
    #  1) create Node
    #  create a method name
    def add_begin(
        self, data
    ):  # Whenever we are inserting a note into a linked list, we always need to mention the data parameter.
        # It will create a node with the data field and link, or the reference, as the none value.
        new_node = Node(
            data
        )  # We are creating a object from the node class.Initially, it was none
        new_node.ref = (
            self.head
        )  # What ever stored in self.head copy that as in the link part of the new_node.ref
        self.head = new_node
        # Whatever the reference stored in new node store that in the self.head

    # When we are inserting a note at the end, we need to check first whether.the linked list is empty or not.
    # If the link list is empty, then we need The reference of the new note to the head of the link list. And if suppose the linked list is not empty,then we need to go to the last node until we find The link part as none.
    # at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
        while n.ref is not None:
            n = (
                n.ref
            )  # Now, we are.in last node, pointing to none the link part.We will continue reassign The n value until we will get n.ref(link) as none in the link part. here the n is storing the reference of the last node
        n.ref = new_node

    def add_after(
        self, data, x
    ):  # it can be the first node, x is the data feild it is required when we are incerting a node between a linked list
        n = self.head  # the first node become n
        while (
            n is not None
        ):  # WHEN THE LINKED LIST IS NOT EMPTY. it will go from the first node to another
            # we are expecting x as a mark for new node suppose there the linked list is like [10|2100]1010 --> [20|3300]2100 --> [30|]3300 and we want to add a node like this [40| ]4800 after [30|]3300 and before [20|3300]2100 we are giving a value to x and checking if it matches with data value or not if it matches then we found a selected node which before we will incert the new node
            if x == n.data:
                break
            else:
                n = (
                    n.ref
                )  # when we find our selected node we will end / out from the loop
        # if it does not matches we are going to next node after that to find our selected node basically we are incrementing the n value
        if x is None:
            print("node is not present in the linked list")

        else:
            new_node = Node(
                data
            )  # we know where to incert the node now so we are creating a node here. it is initially point to none
            new_node.ref = (
                n.ref
            )  # as we know the reference of the previous node is the adress of the forward node .n is the reference(link) of the previous node and connected to the adress part of the forward node to it
            # so what we are doing is now we are copying the link part of the previous node to the new node i.e the link part now it is pointing to the next node
            n.ref = new_node  # Here we are changing the link part of the previous node from the reference of the new node


# in between
# i) After a Node
# ii) Before a Node
# Incerting a node in between the nodes of the linked list
# incerting a node after an existing node


LL1 = LinkedList()
LL1.add_end(100)
LL1.add_after(200, 100)
LL1.print_linkedlist()
''' Link list has two main benefits over an array we don't.We don't need to prelocate space, and two is insertion is easier
Link list traversal equal to order of N or O(n)
Accessing element by value = O(n)
                                     Array           LL
Indexing                             O(1)            O(n)
Insert or delete element at start    O(n)            O(1)
insert or delete element at end      O(1)-amortized  O(n)
insert element in middle             O(n)               '''
