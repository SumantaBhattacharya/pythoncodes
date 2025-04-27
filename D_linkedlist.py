#Linked Lists
#A linked list is a linear data structure, in which the elements are not stored at.it is the collection of nodes.In which each node is connected through links Each node contains data field and only one link of the next node.
#contiguous memory locations. The elements in a linked list are linked using pointers
#It is basically chains of nodes, each node contains
#information such as data and a pointer to the next node
#in the chain. In the linked list there is a head pointer,
#which points to the first element of the linked list, and if
#the list is empty then it simply points to null or nothing.
'''Why linked list data structure needed?
Here are a few advantages of a linked list that is listed below, it will help
you understand why it is necessary to know.

•Dynamic Data structure: The size of memory can be allocated or de-
allocated at run time based on the operation insertion or deletion.

•Ease of Insertion/Deletion: The insertion and deletion of elements are
simpler than arrays since no elements need to be shifted after insertion
and deletion, Just the address needed to be updated.
•Efficient Memory Utilization: As we know Linked List is a dynamic data
structure the size increases or decreases as per the requirement so this
avoids the wastage of memory.
•Implementation: Various advanced data structures can be implemented
using a linked list like a stack, queue, graph, hash maps, etc.
Types of linked lists

1.Single-linked list
2.Double linked list
3.Circular linked list

Insertion in a Linked List

Inserting element in the linked list involves reassigning the pointers from the existing
nodes to the newly inserted node. Depending on whether the new data element is getting
inserted at the beginning or at the middle or at the end of the linked list, we have the
below scenarios.

Inserting at the Beginning

This involves pointing the next pointer of the new data node to the current head of the
linked list. So the current head of the linked list becomes the second data element and
the new node becomes the head of the linked list.

Inserting at the End
This involves pointing the next pointer of the the current last node of the
linked list to the new data node. So the current last node of the linked list
becomes the second last data node and the new node becomes the last node
of the linked list.

Inserting in between two Data Nodes

This involves changing the pointer of a specific node to point to the new
node. That is possible by passing in both the new node and the existing node
after which the new node will be inserted. So we define an additional class
which will change the next pointer of the new node to the next pointer of
middle node. Then assign the new node to next pointer of the middle node.

Removing an Item

1.Traverse the linked list to find the node that you want to remove and the previous node.

2.Update the nextval of the previous node to point to the node after the one you want to remove.

Double/ Doubly Linked List

A doubly linked list (DLL) is a special type of linked list in which
each node contains a pointer to the previous node as well as
the next node of the linked list.

Advantages of Doubly Linked List over the singly linked list:
•A DLL can be traversed in both forward and backward directions.
•The delete operation in DLL is more efficient if a pointer to the node
to be deleted is given.
•We can quickly insert a new node before a given node.
•In a singly linked list, to delete a node, a pointer to the previous node
is needed. To get this previous node, sometimes the list is traversed. In
DLL, we can get the previous node using the previous pointer.

Disadvantages of Doubly Linked List over the singly linked list:

•Every node of DLL Requires extra space for a previous pointer.

•All operations require an extra pointer previous to be maintained. For example, in
insertion, we need to modify previous pointers together with the next pointers.

Dll Each node contains a data field and two links one is the link(link of the next and previous node

<---[previous link | data | next link]-->

<---1011[previous(node reference) link(None) | data(field) | next(node) link]node1--><---5400[previous link | data | next link]node2--><---2100[previous link | data | next link]node3-->None(null or empty value)(last node of the ll is called tail)
     ^
head[1011]starting point of the LL

4	29-Aug-2023	Write Python program to perform the following operation.	1-Sep-2023	No soft-copy submission is allowed
		i) Create a double Linked List.		
		ii) Append a node in an existing double linked list.		
		iii) Insert a node at the beginning of an existing double linked list.		
		iv) Insert a node in between two nodes of an existing double linked list.		
		v) Remove a node from the beginning of an existing double linked list.		
		vi) Remove a node in between two nodes of an existing double linked list.		
		vii) Remove a node from the end of an existing double linked list.	

5	08-Sep-2023	Write Python program to perform the following operation.	15-Sep-2023	No soft-copy submission is allowed
		i) Create a circular Linked List.		
		ii) Append a node in an existing circular linked list.		
		iii) Insert a node at the beginning of an existing circular linked list.		
		iv) Insert a node in between two nodes of an existing circular linked list.		
		v) Remove a node from the beginning of an existing circular linked list.		
		vi) Remove a node in between two nodes of an existing circular linked list.		
		vii) Remove a node from the end of an existing circular linked list.			

      in dll moving forward or baclward is easier  
      dll each node contain the reference of both the next and previous node
      dll we need extra memory to store the two links i.e extra memory
      sll only contain the link of the next node
                                                                ---------------------------------------------------------------------
      ------------------------------------------------------------------------------                               
<---1010[previous link(None) | data | next link(4200)]--><---4200[previous link(1010) | data | next link]--><---2300[previous link(4200) | data(30) | next link(none)-]-->
     ^
head[1010]

In the forward traversal operation
1.Start from First node, print it's data 
second) move to the second node print its data. 
3rd continue Step 2 until last node Data is printed.

while n is not none:#n is the current node
n(prev_node_ref)=self.head
print(n.data)
n(prev_node_next_ref)=n.ref(next_node_ref)

for the backward traversal operation
1.Start from First node, print it's data 
2.move to the second last node print its data.
3.continue Step 2 until last node Data is printed.

incerting at the beginning
create a node
both the link as null
it will have a reference
new_node_next_ref=head
1stnode_prev_ref=new_node_ref
head=ref_new_node

incerting at the end
create a node
both the link as null
it will have a reference
go to last node
last_node_ref=new_node
new_node_pref_ref=last_node

incerting at the end
create a node
both the link as null
it will have a reference
go to last node
go to previous node after which u are entering new node
previous_node_prev_ref = new_node_ref
new_node_prev_ref= previous_node_ref
new_node_next_ref=next_node_ref
next_node_prev_ref=new_node_ref

delete the first node
head=next_node
next_node_pref_ref=null

delete the end node
go to second last node
prev_node_next_ref=null

delete any node by value
go to previous node of the mentioned node 
prev_node_next_ref= last_node_ref
last_node_prev_ref=prev_node_ref

class Node:
def __init__(self, int_data=None,str_data=None):

self.int_data = int_data
self.str_data = str_data
self.prevval = None
self.nextval = None

class DoublyLinkedList:
def __init__(self):
self.headval = None
def listprint(self):
printval = self.headval
while printval is not None:
print(f"Int: {printval.int_data}, Str:

{printval.str_data}")

printval = printval.nextval

def insert_at_end(self, int_data, str_data):
newnode = Node(int_data, str_data)
if self.headval is None:
self.headval = newnode
return
lastval = self.headval
while lastval.nextval:
lastval = lastval.nextval
lastval.nextval = newnode
newnode.prevval = lastval

# Create a doubly linked list with mixed
data types
dllist = DoublyLinkedList()
dllist.headval = Node(10, "Ten")
e2 = Node(20, "Twenty")
e3 = Node(30, "Thirty")

# Link nodes forward
dllist.headval.nextval = e2
e2.nextval = e3
e2.prevval = dllist.headval
e3.prevval = e2

# Insert a new node at the end
dllist.insert_at_end(40, "Forty")
# Print the doubly linked list
dllist.listprint()
'''
class Node:
    def __init__(self, int_data=None, str_data=None):
        self.int_data = int_data
        self.str_data = str_data
        self.prevval = None
        self.nextval = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(f"Int: {printval.int_data}, Str: {printval.str_data}")
            printval = printval.nextval

    def insert_node_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nextval = self.head
            self.head.prevval = new_node
            self.head = new_node

    def insert_at_end(self, int_data, str_data):
        newnode = Node(int_data, str_data)
        if self.head is None:
            self.head = newnode
            return
        lastval = self.head
        while lastval.nextval:
            lastval = lastval.nextval
        lastval.nextval = newnode
        newnode.prevval = lastval


# Create a doubly linked list with mixed data types
dllist = DoublyLinkedList()
dllist.head = Node(10, "Ten")
e2 = Node(20, "Twenty")
e3 = Node(30, "Thirty")

# Link nodes forward
dllist.head.nextval = e2
e2.nextval = e3
e2.prevval = dllist.head
e3.prevval = e2

# Insert a new node at the end
dllist.insert_at_end(40, "Forty")

# Print the doubly linked list
dllist.listprint()

# Create a doubly linked list
dllist1 = DoublyLinkedList()
dllist1.head = Node("Mon")
e2_1 = Node("Tue")
e3_1 = Node("Wed")

# Link nodes forward
dllist1.head.nextval = e2_1
e2_1.nextval = e3_1
e2_1.prevval = dllist1.head
e3_1.prevval = e2_1

# Insert a new node at the end
dllist1.insert_at_end("Thu", "Thursday")
# Print the doubly linked list forward
dllist1.listprint()
