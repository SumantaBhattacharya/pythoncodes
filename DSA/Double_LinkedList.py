# in python Single linked list is the collection of nodes in which each nodes are connected through links. And in the single linked list, each node contains the data field and only one link. That is the link of the next node. But in the doubly linked list, each node contains the data field and two links. 1 is the link of the next node, another is the link of the previous node. So doubly linked list is the collection of nodes in which every node contains data field and link of the next node, as well as link of the previous node.
# address[prev link|Data next|link]
# None<---1011[|Data|]---><---5400[|Data|]---><---2100[|Data|]--->None
#        node1                 node2               node3
# It is the first node of the linked list. And it doesn't contain any previous node. It will store the link to empty value or none or null.
# this is the Second note node 2 contains the data field link of the next note that is node 3 and link of node 1. That is the previous node. And we have node 3 here. Node 3 contains data field at two links. It contains the link of the previous node, that is node 2 as well as it contains the next node reference as none or null, because we don't have any node after that. So in the doubly linked list, the first node previous references none, and the last node. next reference, next node reference is none or null or empty value.
# the first node reference is stored in the head, and that is the starting point of the linked list. And sometimes the last node of the linked list is called as Tail.
# Also, we'll discuss about three operation that is insertion, or adding notes to the liquid list, deletion or removing nodes from the linked list, as well as traversal operation. It is going through each node of the linked list and printing the data of each node.
# Insertion operation will add the new node to the doubly linked list. We'll see what will happen when we add new node to the linked list. And we can perform this operation in the different positions. That is, we can add the element at the beginning of the linked list, at the end of the linked list, or in between, or middle of the linked list.
# Deletion operation also began delete or remove the node from the doubly linked list in different position, like at the beginning, end,or from the middle, or delete by value will mention which node. it want to delete and thes will delete that using the deletion operation
# and in the traversal operation will go through each node and will print the data of each node
# The list each node contains link of the next node as well as link of the previous node. That's why moving forward and backward in the linked list is easier here. So we will see the forward traversal and backward traversal. So one of the advantage of the doubly linked list over single linked list is in the double linked list moving forward or backward is easier, because each node contains the reference of both the next node and the previous node. But in the single linked list, it contains only reference of the next node. So moving backwards is not.easier, but the disadvantage of the double linked list over the single linked list is we need extra memory to store the tool links in the single linked list. It contains data field and only one link,But in the double linked list, we need to store the 2 links. That's why we need extra memory.

# Incertion At the beginning of the list.
# None<---1010[|68|]---><---4200[|69|]---><---2300[|143|]--->None
# So we have here doubly linked list We have three notes. Data is 10 20 30. And here each node contains two links. This is the first node, and it contains the previous link as none and the next link as the next node link. And the last node contains next node link as none. So for our convenience, firstly,we will take the next node reference as nref next reference. And the previous node reference as pref.In each node.
# Next, You will perform the insertion operation. The first step is common. That is, you need to create the node. With two links and a data field here. This is the data field. You can enter any data, for example, 100. And initially I'll take both the link as none or null. So we created the node here. So whenever I create a node, it will have a reference. So I will take 5000 as its reference. Now, the next step is here. We want to add this node as the first node of the linked list. So for that 1st we need to change the nra of of this. That is the next link reference of the new node. It should store the reference of this node that is 1010 here. It need to point here, becausewhen I add this node as the first node of doubly linked list, then this node becomes the 2nd node, the next node of this new node. And here every node contains the reference of the next node, right? So 1010 need to be stored here.
# None<---1010[|68|]---><---4200[1010|69|]---><---2300[4200|143|]--->None
#        ^
#        |
#  head[1010]

# create new_node                     new_node 5100[|420|]
# new_node.nref = head                new_node 5100[|420|1010]                           new_node copying the head value so that we can linked with the pre_1st_node
# 1st_prev_node = new_node.ref        1010[5100|68|]                                     1010[|68|]--->1010[5100|68|]
# head = new_node_ref                  head[5100]                                         head[1010]--->head[1010]

#           5100                          1010                  4200                    2300
# new_node [|420|1010]---><---None<---[5100|68|4200]---><---[1010|69|2300]---><---[4200|143|-]--->None
#        ^
#        |
#  head[5100]
# steps 1. create a new node
# 2.copy the value of head to the next reference of the new node
# 3. copy the address of the new node to the previous reference of the first node
# 4. finally, copy the address of new_node to the head
# ________________________________________________________________________________________________________

# Incertion At the end of the list.
#           5100                          1010                  4200                    2300
# new_node [|420|1010]---><---None<---[5100|68|4200]---><---[1010|69|2300]---><---[4200|143|-]--->None
# 1.create new_node                                                        new_node 4269[|86|]
# 2.go to last node                                                                                          2300                      2300                        4269
# 3.change the last node next reference to the new_node address/reference  last_node_ref = new_node     [4200|143|4269]        <---[4200|143|4269]---><----new_node [|86|]
#                                                                                                            4269                      2300                        4269
# 4.change the new_node pref refeerence to the address/reference of the previous last node             new_node [2300|86|]     <---[4200|143|4269]---><----new_node [2300|86|-]-->Null
#           5100                                  1010                 4200                      2300                         4269
# new_node Null<--[-|420|1010]---><---None<---[5100|68|4200]---><---[1010|69|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
# ___________________________________________________________________________________________________________________________________________________________________________________________________

# Incertion by its value of the list.
#                                                                           5100                        1010                  4200                    2300                           4269
#                                                       new_node Null<--[-|420|1010]---><---None<---[5100|68|4200]---><---[1010|69|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
# 1.create node                                                                                                   steps                          new_node 4590[|99|]
# 2.GO TO THE PREVIOUS NODE AFTER WHICH YOU ARE ENTERING A NEW NODE                                               create node                    4200[1010|69|2300]--->               4200
# 3. Here I'm taking this node as X, so you need to take X dot in reference as new node.                          x.nref=new_node                4200[1010|69|2300]             [1010|69|2̶3̶0̶0̶  4590]<---new_node 4590[|99|]
# 4. store the address of the previous node to the previous reference of the new node                             new_node.prev=x                4590[4200|99|]                 4200[1010|69|2̶3̶0̶0̶  4590]--->new_node 4590[4200|99|]
# 5. Now,  Store the address/reference of the next node after the new node to the next_reference of the new node. new_node.nref=y                new_node 4590[4200|99|2300]    new_node 4590[4200|99|2300]<---2300[4200|143|4269]
# 6. y.pref = new_node
#                                                                            5100                  1010                  4200    x                            4590                y  2300                           4269
#                                                         new_node Null<--[-|420|1010]---><---[5100|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4590|143|4269]---><----new_node [2300|86|-]-->Null
# ___________________________________________________________________________________________________________________________________________________________

# Deletion operation can remove the nodes from the doubly linked list from different position, that is, at the beginning of the linked list, at the end of the linked list. And can mention the value of the node which we want to delete., we want to delete th Node from the beginning of the linked list. That is nothing but we want to delete the first node, this node To delete the first node, what you have to do is you need to point head to the 2nd node. So here, head is the starting point of the linked list. Now you need to point this head to the second node to remove this node. You need to point this to 2nd node here.
#                     5100                 1010                  4200                                 4590                     2300                           4269
# new_node Null<--[-|420|1010]---><---[5100|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4590|143|4269]---><----new_node [2300|86|-]-->Null
# Deletion operation at the beginning of the linked list    Steps
# 1. point head to the second node                          head=2nd_node_ref                                                                          point head to the second node because head is the starting poing of the linked list
# 2. store the previous link of the second node to null     2nd_node_pref= none                     Null<--1010[-|68|4200]                             remove the previous reference from the second node and instead of giving/ it a reference give/assign it with a null value
#          1010                  4200                                 4590                     2300                           4269
# Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Deletion operation at the end of the linked list
#          1010                  4200                                 4590                     2300                           4269
# Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4590|143|4269]---><----new_node [2300|86|-]-->Null
# 1. go to second last node                                                                                         this is the second last node--->2300[4200|143|4269]
# 2. change the second last node next reference to none         2nd_last_node.nref = null                               2300[4200|143|Null]                                    change the second last node next reference to none so that it it will lost its connection from the last node
# This is the first node. It contains the reference So this is the second node. It contains the reference to none. That means it is the end of the linked list. Now to traverse in the reverse order first, you need to traverse like this. And you need to go to the last node, then you need to go to reverse order. You need to go in the reverse order. That's why this node will be treated as it is removed from the linked list.
# ____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#          1010                  4200                                 4590                     2300                           4269
# Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4590|143|4269]---><----new_node [2300|86|-]-->Null
# Deletion operation by its value of the linked list                                                                    2300[4590|143|4269]              new_node 4590[4200|99|2300]---><---2300[4590|143|4269]---><----new_node 4269[2300|86|-]-->Null
# go to the previous node of the mentioned node.                                                                        suppose  4590[4200|99|2300]      2300[4590|143|4269]--->4590[4200|99|2300]
# we only need to make connection between these two and the work will be done new_node                                                                   4590[4200|99|2300]---><----new_node 4269[2300|86|-]-->Null
# copy prev_node.nref to the next_node.ref                                             next_node.ref=prev_node.nref     new_node 4296[2300|86|-]-->Null  4590[4200|99|4296]---><----new_node 4296[2300|86|-]-->Null
# copy prev_node.ref to next_node_pref                                                 next_node_prev = prev_node_ref   new_node 4296[4590|86|-]-->Null  new_node 4590[4200|99|4296]---><----new_node 4296[4590|86|-]-->Null
#           1010                  4200                               x  4590                 y     4296
# Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|4296]---><----new_node [2300|86|-]-->Null


# create two classes 1. Node class we will have us to create a node Next we created the linked list class.
# And later we added few methods to the linked list class, where each method will do different operation of the singly linked list. For the doubly linked list also, we'll do the same thing. We'll use class concept to write the programme.
# We'll create two class 1 is node class and another one is doubly linked list class. And
# in the doubly linked list class, we'll add methods which will perform different operation of the doubly linked list.
# Class we have initialization method self and data as the parameter. Self load data is equal to data.
# Self. reference is equal to none. That means, when we create a node, data field will be assigned. User will give you the data, and that will be assigned to data field. And reference is taken as null. If I create a node with the data as 10 then I'll get the node like this. Reference will be null by default. Now we need to write the programme for doubly linked list.
# In the doubly linked list, a node contains data field and two links, right? Next node link, as well as previous node link. So now here I need to take a data field and two links.
# So for that, we'll take the first link as N reference, that is the next reference. And for the previous reference, take pref The variable as prf which will represent the previous reference. So I take both the reference as none initially.
# So now, when I create a node with data field as 10 then I will get node like this. We have data filled 10 and the previous reference as none, and the next reference as noneSo this is the initial condition of the node. So now we are done with the node class.
# Next, lets create the doubly linked list class. So I will take the linked list name as doublell For linked list, you can take any suitable name.
# And inside that first, I need to take the initialization method, like we did in the singly linked list. And here also, I need to take the parameter as well, because self parameter is must in every method of the class. Next here, what I want to initialise in the linked list. I want to initialise head right? So I'll take Excel head as none. So initially I am taking the linked list is empty. It is the same with the single linked list, right?
# Initially, we will take the linked list as empty. For that, I need to assign head as none. Head is the starting point of the linked list. If I take that as none, that means linked list is empty.
# Next, we need to add different methods to this. Double linked list class now at.And here every method represent the operation of the doubly linked list. In the previous tutorial, while discussing about the doubly linked list and its operation, we discussed three operation, that is, insertion operation, deletion operation and traversal operation.
# No traversing is the process where we'll go through each node and will print its data. Because doubly linked list contains two links, link to the next node as well as link to the previous node. We can traverse in both forward direction as well as backward direction. So we can have forward traversing operation and backward traversing operation. In the forward traversing operation,
# we'll go to the 1st node and will print its data, and we'll go to the next node, and we'll print its data, and we'll go to the next node, and we'll print the data of that node
# And in the backward traversing operation, we'll start from the last node, and we'll go to the last second last node, like this way. In this direction, so we'll get the data of the nodes in the reverse order. First will get 30 next 20 next 10.
# I'll take the first node as en means I need to take n. self head.
# Head is the starting point of every linked list.
# Now, if I want first note, then I need to take N as self head. So now N is the 1st node.
# Next, I need to print N dot data. The data present in that. After that, we need to go to the next node,So for that, I need to take N as N reference.
# That means here. Now,  After printing its data, we need to go to the next note.
# The reference of the next node is stored here. Here. This is the next node reference,  That's why I need to take N dot reference. That means this is N. Now, next again, I need to print the data. And again, I need to change N value to go to the next node. Right here, I need to print the data entered data of this node. And I need to stop,
# because here we don't have any other node. This is the last node. So we need to repeat these two linesagain and again. That's why I need to include this in a loop. So for that, I use while loop.
# And here I take the while condition as while N is not nonebecause here you can see, this is the last node when N becomes this node, I need to print the data N data, that is 30.
# After that, I will change N value. So now N becomes null. That is, N equal to N dot reference. N dot reference is none. So N becomes none. Now, at that time, I need to stop. That's why I need to take while N is not none. Traversing the doubly linked list and singly linked list in the forward direction is same.
# That's why, in the singly linked list programme, I'll copy this method. This method is used to traverse the singly linked list.
# cheque whether linked list is empty. Because if linked list is empty, there is nothing to print.
# That's why first I need to cheque linked list is empty. If you want to cheque linked list is empty or not, you can cheque self head. If self head is none, that means the linked list is completely empty.
# If it is not, linked list is not empty. That's why here I'll cheque this condition. If self head is none, if print linked list is empty, otherwise take the first node as theyen and print its data like this.
# Here to go to the next node, you need to take N reference,
# because here I changed link name, right? So for the next reference, you need to take N reference
# Kindly programme for singly linked records for insertion operation. That is, how to insert a node when linked list is empty, how to insert a node at the beginning of the linked list, how to insert a node at the end of the linked list, how to insert a node after a given node, and how to insert a new node before the given node. 
# Here in the double linked list programme also, we'll write these five methods for the insertion operation.
# Insert new notes when linked list is completely empty We linked list is completely empty. 
# That means head will point to none. The value of head is none.
# So at that time, the first step is we need to create the node.
# So here, linked list is completely empty. So createA node like this data is 10.
# When I call node class, which we discussed in the previous tutorial, it will create a node with two links. 
# And the default value of 2 links is none. And it will take a data field. So in the programme to create the node, I will use node class like this. Next step, after creating the node, what I need to do is now head is pointing to null. I need to point this to here, right? Head need to point to the new node. 
# So this is the new node So head new node. So when linked list is empty, first step is you need to create the node,
# and you need to point head to the new node. So here we have our programme
# And data. Whenever you write a method to insert the new node to the linked list, you need to take parameter as data, because you are inserting a new node. And in that you need to mention the data field.
# That's why here you need to take data And in this method, first, I will check the linked list is empty or not. So first I will cheque self head is nulllike this. 
# If self head is null, then only I will insert the new node, right? Here we are writing this method to insert the new node at the empty linked list. So first I need to cheque whether linked list is empty or not.
# For that, I need to cheque self id is none or not. If it is none, then create the new node. So I will take new node name as new node, and I will create the new node using node class.
# And here I need to pass the data so it will create a node with both the reference as none and with the data field Next, after creating the node, 
# I need to point head to the new node. So self dot head is new node. Else, if linked list is not empty, i'll just print a message that is linked list is not empty. So entering the new node to the doubly linked list, when linked list is empty, is same as entering the node when singly linked list is empty.
# The code is same. You can compare it with the singly linked list, insert empty method. Ok. 
# So in this way, you can insert the new node when linked list is completely empty
# To add the new note at the beginning of the linked list. While adding the new note at the beginning of the doubly linked list,
# you need to be careful about two things. 1st 1 is whether you are adding the new note to the empty linked list. If you are adding the new node to the empty linked list, 
# then the condition is different. You need to write the separate code for that. And also for non empty linked list, another condition is non empty linked list. In the doubly linked list, if you are adding the new node at the beginning of the linked list then we need to be careful about two things. 
# That is, first, we need to cheque the linked list is empty or not. If linked list is empty, that means whatever node we are adding, that will be the first node of the linked list. 
# And also, that is the only node of that linked list. So we need to write the separate code for that. If it is non empty, then we are adding the element at the beginning of the linked list. So that will become the first node of the doubly linked list.
# So We need to write the separate code for that. So first we'll cheque this condition empty linked list. If the linked list is completely empty, then if you are adding the new node, then what will happen? If linked list is empty,
# that means head will point to none. Now, the first step in the insertion operation is you need to create the node. So to create the node, we will use node class in our programme, like this, and node data, and will create a new node here, a new node will be createdFor example,
# if I take data as 10 will take data as 10 and both the links are pointing to none. Now, after creating the new node, what I need to do is I need to point head to this new noderight? At new node. So this is the code you need to write when you are adding the new node at the beginning of the doubly linked list. 
# When doubly linked list is completely empty. So here in the programme, we need to write the method and begin add at the beginning of the linked list. You need to take cells and data As I said, every insertion method you need to take data as the parameter.
# And here first step is you need to cheque self dot head is none. Before checking linked list is empty or not, double linked list is empty or not. First, i'll create the new mode, like this new node, losing node class, passing data parameter Next I will cheque self head is null. That is linked list is empty. 
# If doubly linked list is empty, that means I need to take self head as new mode. And I need to stop else.
# If doubly linked list is not empty, then we need to write the separate code. Let's see that Let's see that. So if double linked list is not empty, 
# and if I want to add the new node at the beginning of the linked list, first step is create the node like this. 
# When I create the node, it will point to none. Both the link point to none. This is the new node. 
# After that, I need to change the new node. Nrf, this is the nrf. Next link reference. 
# This is the praf previous link reference. First, I need to change this nref new node reference So I'll take new node nref next link reference.
# I need to store this. I want to add this new node at the beginning of the doubly linked list. So this node will become the next node of this node. 
# That's why we need to store the reference of this node in the nref of the new node.
# And where this link reference is stored before adding this node to doubly linked list. This is the first node of this doubly linked list.
# And the 1st node reference will be stored in head, right? So here I need to takehead, head contains 110. So I need to store that here. 
# That's why I'll take new node dot nref is equal to head. Now this link is changed. It will point to here. Next here we can see, this is the doubly linked list. 
# And every node contains previous reference as well as the next reference. And in this node, it should store the reference of this node, right? New node. So I need to change that here. 
# This node need to point to hereWhat is this? Till now, head is pointing to here. This is the first node. We didn't added this node completely to the doubly linked list. 
# So this is the 1st node. So head is pointing to here. That's why, if I want to access this link, this is nothing but selfhead dot pref. Previous reference.
# So this is head now. If I want this link, this is head.praf I want to store the reference of new nodes.
# So I'll take new node Lastly, now we added this node to the doubly linked list.
# So head need to point here. So I'll take self dot head is equal to new node. Point head here. So head is equal to new node. 
# Add just add weekend method of the doubly linked list is different from the add begin method of single linked list. 
# That is because in the doubly linked list, every node contained two reference, previous reference and next link reference. 
# That's why we need to write the separate code. First, we need to check the linked list is empty, double linked list is empty.
# If it is empty, then that means whatever the node we are adding, that is the only node of the doubly linked list. 
# So we need to write the separate code. Otherwise we need to write the separate code.
# Next.let's write the method for addend. That is, we want to add the element at the end of the linked list.
# So for that, I will take the method as add end. I will take cells data. And firstly,I will create the node using node class.#
# Write this that we created the node. Now only adding that to doubly linked list is left. 
# So lets see how to add at the end of the linked list. So first is you need to check the linked list is empty or not.
# Here also you need to do that because if doubly linked list is completely empty, then head this pointing to none. 
# Now if I want to add any element, if you want to add new note at the end of the linked list. 
# But here, linked list is completely empty. 
# It doesn't have any node That means whatever node we are adding that is the first node of the linked list.
# So 1st we need to write the condition for that. We need to check whether linked list is empty. If it is empty, #
# then we need to point head to new node, right? We need to create the new node, and we need to point head to the new node, 
# because that is the first node of the double linked list. Head need to point there. So that is why here also add end first.
# I need to copy this.while adding the element at the end of the linked list. Also, first, 
# I need to check the linked list is empty or not. If it is empty, then I need to point head to the new node.
# So code is same else while adding the element at the end of the linked list. 
# First, we will create the note and will check double linked list is empty or not.
# If it is empty, then we will point head to the new node. If it is not empty, that means it contains few nodes.
# Now, if I want to add new node here, we need to create the node like this. For example, I will take 11.a data.
# And when I create the node using node class, both the nref and prauf will point to the nun.
# Now,what we need to do is to add this new node at the end of the linked list. 
# First, we need to travel to the last node. 1st we need to come here. So to travel to this position,
# I will take 1st node as N here. This is the 1st node. I will take 1st node as N. And to traverse to the next node,
# I will take any code to N dot nref. And using while loop, I will increment the N Value until I reach the last node. 
# I already explained about this while discussing about the add end method in the singly linked list. 
# So you can refer that video. So here.first you need to take the first node as N.
# So the reference of the first node is stored in the head. So you need to take N equal to selfdot head.
# Then you need to using the while loop. You need to traverse to the last node. So here in the while loop,
# you need to take the condition, right? So lets see what is the condition. We need to travel to the last node.
# So we need to stop when N becomes this node. In this node, you can see nref is null.
# So I will take the condition like this when N Dot nraf becomes null. Stop. Stop changing the end value here. 
# I will take young dot nrf 6 not none. If it is not none, then Increment the end value. 
# That is, go to the next node. If it is become none, that means, that means we read the last node. So now stop.
# Come out of the while loop. In this way, you can reach the last node using this next after going to the last node here.
# You.need to change its reference, right? You need to change this reference. It need to point here.
# So this is nothing but N nres. You need to point that to.
# New note, first is NREF is equal to new node. Andalso, new nodes prf need to point to this N. So that's why I will take this is new node, new node dot praf. This is the previous reference link. New node dot prf is equal to N. This reference 300.
# I need to store that here. Here N is nothing but 3000. 00. That is why new node P nref equal to N. So here let's write that outside the while loop can dot nref is equal to new node. Change the nrf of the last node, then.new node previous reference PREF is equal to Gen. So now
# That is how to insert new node after the given node, or before the given node. 
# There are few similarities between these two methods, that is, add after.and add before methods here.
# add after method will add the element or new node after the given node and add before method will add the new node before the given node. 
# Today we will write the code for these two methods. 1st we will see the similarities between the two methods in both the methods.
# First we'll check doubly linked list is empty or not.If doubly linked list is empty, that means we cannot add any new node after the given framework. There is no node present in the double linked list here in the add after and add before method.
# We need to add the new node after the given node or before the given node. If that given node is not present in the double linked list, then how to add the new nodeRight? That's why first we need to check this in both the methods.
# First, we need to check the double linked list is empty or not. If it is empty, print a message. If it is not empty, then traverse to that positionTraverse to give a node.
# So in my program, in both this method, I will take X as the given node. So I need to traverse to X here.
# Go to that node, mention the node. Then in add of the method, add the new node after the X. 
# And in add before, add the new node before X. So these are the steps we need to follow while writing these two methods. 
# So 1st let's write the code for add after method. So here we have our program, class node, class doubly linked list.
# In that we have two methods.for traversal operation, forward traversal and backward traversal. 
# Next we have three method for insert operation.
# Insert Mt, add, begin and add. So Create the add of the method add after 
# I take the method name as add after next, the first parameter itself. 
# Next you need to take data. So we are inserting in a new node. 
# In every node there is a data field, right? So we need to insert a data as well as we need to insert X.
# X is nothing but the given node, after which we need to insert the new node.
# So here I will mention X as the data, data of the node. For example, 
# if my doubly linked list contains 1020 and 30 and if I want to insert the new node after 20 then I will take X as the 20. 
# So here X is the data of the node. Next, first step is we need to check double linked list is empty or not to check the linked list is empty or not.
# We need to use self head is none or not. So I will take if condition and I will check self dot head is none here.
# If it is none, that means linked list is empty, so you can print any message here, like linked list is empty, 
# so you can't insertlike that. You need to write a message. If linked list is empty, 
# that means X is not present in the doubly linked list, right? So that means we cannot insert the new node after X. 
# That's why we need to check this condition. Else, if linked list is not empty, then we need to traverse to the X node, 
# the given node. So now the question is, how to go to the node x So for that, you need to traverse from the beginning. 
# You need to start from the first node here. We have few nodes. So if doubly linked list is not empty, 
# that means it contains one or more nodes, and X can be any node to traverse to that node to reach that node. 
# We need to start from the 1st node. So for that first I will take N equal to selfhead, ok?
# So the first node will become N because the head contains the reference of first nodes.
# So you need to take N equal to self plot head. Then to go to the next node, you need to change the N value like this,
# N equal to N N reference. And we need to check data of every node with the X. 
# Because, as I said, X is the data of the given node. So for that, I will use if condition,
# and I will check like this. If X is equal to N dot data, initially I take the first node as N right? 
# So enter data is nothing but 10. I will compare 10 with the X value. If X equal to equal to N dot data, 
# if it is true, that means we got the X. We found the X. N is pointing to X now, if it is.not if it is not,
# then I need to increment the N Value. I need to go to the next node. Now, N becomes this.
# And again, I need to check X with the end dot data. 20 with the X. If it is true, means we got the X. Otherwise, 
# again, I need to go to the next node, and I need to check the data of that node with the X. 
# I need to compare the data of that node with the X. So we need to repeat this again and again. 
# That is why I need to include this in a while low. And here I need to take condition as while N is not none.
# Until.N becomes none, I need to execute this.here when this node is young, this is the last node here. 
# You can see, first, you need to compare this. That is N dot data, 30 with the X. Whether it is equal, 
# if it is not, then I will increment N value, right? So N becomes none. At that time, I need to stop. 
# That is why here I need to take while N is not none. Chuck, if X is equal to N Dot data, it becomes true. 
# Execute break statement. That is nothing. But we found the X node, that is the given node. 
# Now stop moving to the next node. That is why you need to execute this break statement.
# When you use break statement inside a while, look when that break statement is executed,
# it will come out of the loop. If X is not equal to the end dot data, then you need to go to the next node. 
# So for that, you need to change N value to enter.N reference. 
# In this way, you can move to the X. You can find the X. So here, initially take N is equal to self head.
# Next here, use Y loop and check why N is not none. While N is not null, if it is not nun, 
# you need to check if X is equal to N Dot Theta. You need to use the comparison operator, double equals.
# And if it is true, execute the break statement. If it is not, then go to the next node. 
# So for that, you need to take N equal to N dot in reference.
# Now,here control will come out of the while loop because of two conditions. 
# 1 is because of the execution of this break statement. Or another one is when N becomes none. 
# If N becomes none, it will come out of the loop. Or when we found the X value,
# it will come out of the loop. We need to take that to condition. That's why here I will use if condition,
# and I will check if N is null. If N is null, means we served for X in the entire double linked list,
# but we did not found that. That means, if N is none, given node is not present in the doubly linked list,
# the.ll doubly linked list. Look here. We'll go to every node, and we'll check its data with X.
# We'll compare its data with X. If we found that, it will execute the break statement. 
# If the data of the nodes rint batch with the X, then we'll go to the next node, and we'll compare its data.
# But if X is not present in the doubly linked list, then break statement won't execute. Instead of that, N becomes null. 
# After completing every node, N will reach to the last node. And after comparing its data, N becomes null.
# So at. that time also control will come out of the while loop. So first we need to check that condition. 
# If N is none, that means the given node is not present in the tablet linked list. Else, if.N is not done,
# that means break statement is executed. That means we found the X. Now we know where X is present. Now, 
# N is pointing to X. Now what we need to do? Let's see that. Now, after finding the export we need to do, 
# we need to add the new node after the given node. So for that first step is you need to create the node. 
# So create node using node class next, because every node of the doubly linked list contains previous reference as well as next reference. 
# When you are adding the element of the given node, you need to be careful about one thing, that is,
# whether you are inserting the new node after they last node. You need to write the special condition for this.
# You need to be careful about this scenario, becauseevery node contains previous reference and next reference. 
# Because of that, you need to be careful about this, whether you are inserting the new node after the last node.
# And here next is restcase. Rest nodes, that is, after the 2nd node, after the first node, or after they middle nodes here.
# While writing this method, you need to be careful about 1 thing, that is, 
# you need to check whether you are inserting the node after the last node. I will tell you why. 
# 1st before that, lets create the node here to create the node. I will use node.is equal to node and date. 
# and data pass the data here. Use _So now new node is created. Next,
# let's see what happens if I add a new note after the given node.
# So first, let's take this as X. So now I need to add the new node after.
# Like this is also pointing here after creating the new node, I need to change its previous and next reference,
# right? So for that first piece I need to change this new node NRF.
# I need to store 3200 here, right? You need to point here 3000 point store here.
# What is this? This is reference N dot reference. So now 3200 be stored here after that.
# Let's change the new P reference here. What you need to do you need to store this value.
# 5000. What is 5000? That is. Yeah. So you need to take new node PREF is equal to yeah.
# So first create the new node and change. next. Now before changing this we need to change this. 
# This need to contain the previous node reference. That is nothing but this new node.
# You need to continue node. Now what is this position? This is N is 3200 is nothing but this is dot N reference.
# This is its previous reference. So you need to take north dot north reference dot PRES is equal to new node.
# That's why I told you before changing this, you need to change this here. This note is so end not end of 3200. 
# That is not so. This not becomes end not friends. And in that note, this position is not endorsing dot PF.
# That is equal to you know. So you can store node link. That is 111. next you need to change this. 
# That is N dot in reference this is that this is end dot end reference to store you know here. 
# OK so this is the code but here as I said you need to be careful about one thing by inserting the new not only that is you need to check whether you're inserting of the last let's see what will happen if I insert the new note of the last node.
# So I'll take this as X. So now X and are pointing here. OK X and is pointing here. Now I create a new node first 200.
# Now initially none. Now what you need to do is you need to change that is this you need to take.
# Yeah. So you need to point here to take 3200. So you need to follow this step and you take the NRO that is you need to take new note NRO as NRO. 
# So it will point to none this reference it take to point to new node. So you need to end is equal to new node. 
# So now if you want to add the new node after the last node then you need to write this code this code and this code you don't want this line.
# That's why you be careful about inserting the node after the last node.So to write this code, what I do is, first,
# I like take these two lines. That is, I take new note, nref is equal to node.Pref is equal to yes. Next here, 
# I take this condition. If N Dot nrf is not null, that is because I check if you are inserting the given node or to the rest node. 
# Other than the last node, then you need to write this condition like this. If none that.
# let me inserting the new node after the last node. That's why you need to take the condition like this.
# If N dot nraf is not none. So here you can see, if this is the last node, then here you can see, this is end dot nref. 
# It is null. If it is not null, means it is rest of the node, not the last node. If it is not none,
# then take N.A.Equal to nref F .Prf equal to new node. If you are inserting the new node after the last node,
# this line is not necessary, right? That's why we are taking this condition. Lastly, friends is equal to new node.
# So now we are done here. What I did is first I created the new node. We changed its nraf and prf. 
# Next I will check whether we are inserting the new node after the last node or not. 
# If you are not inserting the given node after the last node, then we need to include this line.
# If you are inserting the given node after the last node, this line is not necessary.
# Lastly, change N.nraf to new node. Next.lets write the method for add before. 
# So for the deletion operation of the double linked list, we'll write three methods, 
# that is, we'll see how to delete a node from the beginning of the double linked list, from the end of the double linked list.
# Also, how to delete the node by value. So we'll discuss about these 3 methods. So 1st we'll discuss about this scenario. 
# That is how to delete a node from the beginning of the linked list, and we'll write the code for that.
# So when you are performing the deletion operation first step is you need to check the linked list is empty or not. 
# Here we are discussing about how to delete a note from the beginning of the linked list. Delete.begin method.
# So first step is you need to check linked list is empty or not. If linked list is empty, 
# that means it doesn't contain any node. So we cannot delete the node at that time, right? So first scenario is this.
# Next, after checking this condition, if doubly linked list is not empty,
# then I need to check whether the doubly linked list contains only 1 node. Because in doubly linked list,
# every node contains 2 links, that is, previous link and the next link. 
# That's why we need to consider this condition also before deleting the node. 
# We need to check whether that node is the only node of the West Linked list. And the. lastly, for the rest case, that is,
# if our doubly linked list contains more than one node. 
# Here we are writing the method for deleting the node from the beginning of the double linked list.
# We can write that method in three steps. In the first step, I need to check linked list is empty or not. 
# If linked list is empty, that means we can't delete any node from that. If linked list is not empty, 
# then I need to check this condition. I need to check whether linked list contain only one node. 
# If.doubly linked list contains only one node, and if I am deleting that, then linked list will become empty, right? 
# That's why I need to check this condition. If this.condition is also false, then I need to check this condition. 
# If it contains two nodes, 3 nodes, 4 nodes, 5 nodes, then I need to write the separate code for this. 
# So first, let's say the first case, how to check linked list is empty or not. We know that, right?
# If self head is null, that means doubly linked list is empty. So if doubly linked list is empty,
# then I will print a message that is doubly linked list is empty, so you can't delete any node from that. 
# So first.let's do this in the python file. So here we have our program, class node, class doubly linked list.
# And in that we have print L that is the forward traversing method. Printll reverse, that is the reverse traversing method.
# Insert empty, add begin, add end, add of the method as well as add before method.
# These are the methods for the insertion operation. Today we'll write the method for deletion.
# I'll take def and I'll take the method name as deletebegin. And here I need to take parameter as cells.
# We don't need any other parameter, because here we are deleting the node from the beginning of the West linked list.
# So we don't need any other parameter. And here the first step is you need to check list.
# or doubly linked list is empty or not. So for that I'll use if condition, and I'll check. Self head is none or not.
# If self head is none, that means doubly linked list is empty. So we cannot delete any node. So dll is empty.
# I'll print this message. W Linkedlist is empty, so I can't delete the node from here. And here I can use return statement. 
# If I use return statement in a method or function, when sulfide becomes done, it will print this message, 
# and it will execute return. That means control will come out of that method, orif you want,
# you can use else also instead of return. You can take else statement here. It's your wish. Ok,
# so now we are done with the first step. Next, let's see the next step. If W Linkedlist is empty, 
# we'll print a message. If it is not empty, then we need to check this condition.
# We need to check whether doubly linked list contains only one node, for example,Here I'll take only one node, ok,
# like this. I'll take data as 100 and I'll take none and none. If doubly linked list contains only one node,
# it will look like this. This is the data field, and both the reference will point to none, and head will point to that node.
# Now, if I delete this note, then head will become null, right? We need to take head as null.
# When only one node is present in the doubly linked list. If I delete that, then I need to point head to none.
# If.doubly linked list contains only one node, that is this node. If I delete this, then double linked list becomes empty.
# empty is nothing but head will point to none, right? So we need to do that. Now the question is,
# how to Chuck Double linked list contains only one node or not? For that, you need to take the condition like this.
# This is the head right, and this is nref. Next link reference. If head .nraf is none,
# that means double linked list contains only one node. Here we can see in this double linked list, it contains 3 nodes.
# This is.head and this is head nref. It contains the reference of the next node, right? If this nraf link contains none,
# that means we don't have any other node after that. That means we have only one node in the double linked list like this.
# If you have only 1 node in the double linked list,
# the nraf of that node will point to noneSo that's why to Chuck Double linked list contains only one node or not.
# I need to check like this, self.head.nref. Next click reference is none.
# If it is none, means the W linked list contains only one node. So so here you need to textelf dot head as none.
# If you want, you can print the message. Also, you can print any message here if you want. Next here, I will take else part.
# If doubling the list is empty, we'll bring this message and will come out of the method.
# If.doubly linked list is not empty, then we'll check this condition.
# We'll check whether double linked list contains only one node.
# If it is true, I'll take self plot head as null and I'll print this message.
# If the double linked list contains more than 1 node,
# then what we need to do when doubly linked list contains more than one node how to delete the 1st node from that.
# So for that, what you need to do is you need to point head to the 2nd node.
# The first step is you need to point head here.because we want to delete this node, right?
# When we delete this node, this will become the first node of the double linked list. So we need to point head here.
# We need to take head equal to this node. 400. What is 400. That is nothing but the nraf, right? So
# here you need to take head, dot, nref. Initially, head was pointing here, right? Now, head is 1010.
# Now I need to point head here. So for that, I will take head.nref, head nref is nothing but 4000.
# So head will point to here. After that, here, this is the first node. Now,
# the previous reference of this need to point to none, right? Now, this is head.
# And the previous reference of this need to point none. So I need to take head dot pref equal to none. OK,
# now the West Linkedlist will start from here. Head. So this is the first node and its previous reference is pointing to none.
# So this will be the first node. After that, it contains the reference of 2700. So it will become the second node.
# Now it contains the reference of none. That means it is the last node of the West linked list.
# This node is treated as it is removed from the double linked list.
# So here first I need to take self dot head is equal to cells..head.nres.
# And next I need to take.self.pref.is equal to none. So now we are done with the delete begin method.
# So lets execute that, and we will see whether it works properly or not. Here we can say, I created the DL1 object.
# And here.already we have 10 and 4 in the doubly linked list. If you want, you can see that.
# And if I execute this here, we can see we have 1094.Now, if I delete the node from the doubly linked list, DL1 delete,
# begin. So it will remove 10 now. So we have only four now in the double linked list.
# If it contains only one node, now our doubly linked list contains only 1 node. Now, if I delete that,
# dll is empty after deleting the node linked list is empty.
# Now, if I comment this also, that means doubly linked list is completely empty. Now, if I try to delete the node from that,
# I will.get this message dll is eMpty. Can't delete.
# We can delete the node from the end of double so when we want to delete the node from.the end of the double linked list
#, we need to check for 3 scenario 3 steps. The first step is you need to check doubly linked list is empty or not.
# It is if doubly linked list is empty, we can't delete any node from that right? And if doubly linked list is not empty,
# then we need to check the double linked list contains only one node. If doubly linked list contains only 1 node,
# and if I delete that, then the double linked list becomes empty.
# So that's why we need to write the separate condition for this case. And lastly,
# for the rest case, that is when double linked list contains two nodes, three nodes, 4 nodes or five nodes,
# how we can delete the last node from that doubly linked list.
# Here we are writing the method to delete the node from the end of the doubly linked list in that the first cases we need to check doubly linked list is empty or not.
# If it is empty, then we can't delete any node from that. And if doubly linked list is not empty,
# then we need to check whether it could. There's only one node. If the doubly linked list is only 1 node,
# and if I delete that, then double linked list becomes empty. That's why we need to check this condition.
# Next,lastly, we need to check this case when doubly linked list contains two nodes, 3 nodes, 4 nodes, 5 nodes like that.
# Let's write the method first. We need to check doubly linked list is empty or not.
# How to check double linked list is empty or not. We need to check self head.
# If it is none, that means double linked list is empty. If doubly linked list is empty, then I will print a message.
# So in the python file here, I will take the method name as delete.end. And I will take the parameter as self.
# We don't need any other parameter here.Then here I will copy this code.like this. That is.Will check the linked list is empty or not.
# So that's why I'm checking self dot head is none. If it is none, i'll print this message and I'll return.
# Next.the first case is done. Next, we need to check how many nodes doubly linked list contains.
# If it contains only 1 node, we need to write the separate code. We need to take self head as null.
# If doubly linked list contains only one node like this, after deleting this node, head need to point to none, right? 
#That's why I need to take self dot head as none. So for this,
# I will copy this code again. Ok,
# here also we are doing the same right in the delete begin method First we'll check linked list is empty or not.
# Next we'll check whether it contains only one node after deleting that self head will point to none and will print a message.
# Next here, I will take else part.In the else part, we'll take the condition when Dublin naked list contains two, 34 or more than one node.
# How to delete the last node at that time? Let's say that. So here we can see we have doubly linked list, which contains three nodes.
# Now, to delete this last node, what we need to do is, first, we need to go to the last node. Here go to the last node.
# So to move to the last node, I will take the 1st node as N is equal to node head. And using while loop,
# I will travel to the last node here. This topping condition for for while is when.this nraf becomes null.
# The node which contains the nraf as none at that node, I need to stop We did that so many times.
# So here I'll take N equal to self dot head. Initially take the first node as N and using Y low.
# And here I will take nraf is not nullWell, next link reference of North is not null.
# Move to the next node. N equal to N dot nref. N becomes the next node. And again,
# we will check this condition. In that node, nraf is none, node not. If it is none,
# that means we reach the last node. If it is not none, that means we need to go to the next node.
# So use this next node link and move to the next node.
# So after executing this while loop, we will reach to the last node here.
# N will point to this now.This is N. Now what we need to do? We need to make this the last node of this N.
# This node, its nrf, need to point to null. It need to point to none like this. We need to make this like this.
# So for this, to access this position, I will take this is N now, and this is the previous node.
# So I will take N pres.So here in the prf, you can see 4000. So this is the previous node of N.
# So this is N dot prf dot for this place. This is the next link reference, that is nrf.
# I will take this as none. So when this is N this is the previous store of that node, that is N prf. 
# And in that this position is not nref. That is why north.pref.nraf equal to none.
# Now this will point to none. So now this node is.node is treated as it is removed from the double linked list.
# When we travel from the first node, this is N. So this is the 1st node. It will print its data, and it will go to the next node.
# It will print its data. And here we can say it contains the reference to none. That is why it will stop.
# This node will be treated as it is removed from the double linked list. So here you need to take N dot pref,
# the previous node of Tennessee, and its next reference is equal to none Now we are done. So let us see how it works.
# So first, I will take both the methods, printll as well as printll reverse. And here I will take delete int.
# Now I will double linked list contains 10 and 4. Now if I call delete end method, it will delete 4.
# So we will get 10.Here you can see 10Now, if I comment this, that means our double linked list contains only one node,
# that is 4. And if I delete that now,doubly linked list is empty after deleting the node.
# And we are getting linked list is empty two times. That is because of this print ll and print ll reverse. And now,
# if I comment this also, and if I execute this, dll is empty, so can't delete. And here we can see linked list is empty message.
# Next we will write the method for delete byvalue scenario. In the delete by value method.
# He'll give you that value of node delete that note. For example, if I take three nodes with 10 20 30 and if you mentioned,
# you want to delete 20 then we need to delete that note. Alright.
# So let's like another for the scenario. Here I take user input as X.
# This user will choose, right? Which node you want to delete that as X.
# And by writing this, you need to be careful about few scenarios or case. The 1st case is when liquid is empty.
# Link is this empty. 2nd case is when it contains only 1 node. And 3rd is, if you want to delete the first node, next is,
# if you want to delete the middle nodes, any nodes, middle nodes. And lastly, the last node, if you want to delete, last node.
# So you need to be careful about this 5 cases while writing this method. Let's say every scenario is 1 by one. First, let's take this case.
# When liquid is this empty.linked list is empty. We cannot delete any node from that,
# right? It is completely empty. So at that time, we'll print a message, like we did in the previous two methods.
# So in the python file, i'll take the method name as delete by value, right? And here I need to take cells and X.
# X is nothing but the which node you want to delete. The data of the node. Next here,
# first step is we need to check the linked list is empty. If it is empty, we need to print a message.
# So I will copy this and here I will paste that. Sofirst here we will check sulfide is none.
# If sulfide is none, that means linked list is empty.
# So I will print this message and I will come out of the method.Using returns next.if linked list is not empty,
# if linked list is empty, we'll print a message.
# If it is not, if it is not empty, next I need to check whether the linked list contains only one node.
# If doubly linked list contains only 1 node, then 1st I need to check whether I want to delete that node or not.
# Here, user will mention the date of the node which he want to delete, right? So I need to compare X with the denote present in the double linked list.
# Now, only one node is present. I need to compare that with the X. If that data is equal,
# then I need to delete that node If it is not equal, then I need to print the message, the enter node is not present in the doubly linked list. 
# That is, I will explain you if the double linked list contains only one node.
# 1st I need to check the data of this node with the X. If it is equal to X, then I need to delete that node.
# If not, X is not present in the doubly linked list. For example, if I enter X as 20 here we can see I will compare 10 with 20.
# It is not equal. Then that means 20 is not present in the double linked list,
# because doubly linked list contains only one node, that is this node. If the data of this node doesn't match with the X,
# that means X is not present in the double linked list.
# So first here, what I need to do is I need to compare X with the head data Self head data, because this is the head.
# If it contains only one node, that means the 1st node. So head is pointing to that node. So I need to check like this.
# If X is equal to head.data If it is true, then I need to make head As none.Else I need to print.The given node is not present in the dwelling linked list.
# So next here, what we need to do, we need to check this condition, whether only one node is present in the West Linked list.
# So for this I will check like this. If in.Is ease none to check whether only one node is present in the double linked list.
# We need to write the condition like this right and here inside this I need to check if X is equal to equal to cells dot head dot Theta.If it is equal,
# that means that is the node we want to delete. If this is true, then I want to delete that first node.
# The only node present in the double linked list. So I need to take self dot head is equal to null.Fine,
# right? Else.but it is not true. Then.X is not present in the double linked list. Ok,And here I will execute freedom statement.
# Next, first, we check the weather linked list is empty. If it is empty, we will print a message.
# Otherwise we will check whether the linked list contains only one node in that wheelchair.
# X matches with the present node. If it matches, we will delete that node. Otherwise we will print the message that is X is not present in the double linked list.
# Next after this. After this, we need to check this condition. We need to check whether we are deleting the first node of the double linked list.
# If the double linked list doesn't contain only 1 node, if it contains more than 1 node, that means I need to check this condition.
# Whether we are deleting the first node of theta play linked list because if we are deleting the 1st node of the West linked list,
# the condition is different. So to do this, to check this, I will check self dot head dot data because the reference of the first node will be stored in the head.
# So self dot head dot data is equal to equal to X. I will check like this. If it is.true, that means I want to delete the first node.
# So to delete the first node I need to point head here and I need to store its reference.
# This node reference as null as we did in the delete begin So here we need to check if self dot head dot data is equal to X,
# whether the X is equal to equal to first node data. If it is 2 that means we want to delete the first node.
# So I need to do this. I need to point head to the selfed dot N reference and I need to take P reference as none.
# If I want to delete the first node,then I need to point the head to the next node of the first node.
# So next node reference will be stored in NRF. So I need to take self dot head is equal to self head NReF.
# Then I need to take the second node previous reference as none Here I need to point head here,
# the reference of this is stored in this nref. So I need to take self head is equal to selfhead dot nres.
# After that, it will point to here. Head will point to this node. Then I need to change this right.
# So I need to take self load head dot pref as none. So we are done with this condition. If it is not the first node,
# if I want to delete the middle nodes of the bra linker list, then how to do that? So for.
# this if I want to delete the middle nodes of double linked list, not the first node, not the last node. Middle nodes,
# then.for that first I need to take your return. And here.I need take N is equal to self dot head.
# And using while loop node nref is not none.I need to check if X is equal to N dot data. If it is true, execute break statement.
# If it is not good, go to the next node. So here, what I am doing is, if I want to delete any middle nodes,
# I will take the first node as N and I will check whether N Dot nref is none. We already checked this node,
# but its ok if we are doing this again. Otherwise, instead of taking N equal to self head,
# you can take N equal to self dot head nrf. You can take this as an and it can begin. Buthere I will not do that.
# I will just take this node as N and we will compare its data with X.
# If it does not match, then I will execute N equal to N dot nrf. I will take this as N and I will again check 20 is equal to X.
# If it is not, then again, I will execute N equal to N dot nraf. I will go to the next node,
# and I will check until we will read the last node. When N becomes this node, ok,hits end .nref is null.
# So it won't check its data with the X, because we are writing this code for middle nodes, not the last node, right?
# That is why here we took the condition as well N dot nref is not none.Here it will again, chuck the first node also,
# but it is ok. As I said, if you don't want to do that, you can take here some head nrf. And you can write this code.
# If X matches with the data of any middle nodes, then execute the break statement. Like we did in the previous tutorials,
# right? Now, the control will come out of this while loop because of two conditions.
# That is when this becomes none ref becomes none. Or when.break statement is executed.
# So here I take the condition for that too. Here, what I will do is, first,
# I will take if N Dot nref is not none. As I said, the control will come out of the Y loop because of the two condition.
# That is when 1 is when N dot nraf becomes null. Otherwise, when the break statement is executed, if N dot nrf is not none,
# that means break statement is executed. That means we form the X. Now N is pointing to thatAt that time,
# what we need to do is here, for example, I want to delete this node. This is X. And N also pointing to here.
# Now I need to change this and this right this reference here. This is yn. So this is N dot pref dot nres.
# So this is the previous node. So N dot pref. And in that this is nref. Next node reference.
#So north.pref.nref is equal to here. I need to store the reference of 2000 00. That is something but N Dot nref.
# And also in this position, this is nothing but this is the next node of N. So north.nref.in this, this is the prf previous reference.
# So equal to here I need to store the reference of 1010. Here it is stored here. That is nothing but N dot pref.
# Here N.Nrf.prf equal to N.prres.nref equal to 10 dot nris. Right next. If end dot nariof is not none,
# that means break statement is executed. If this condition is false,
# that means the control came out of the loop because of this condition. N dot nrf becomes none. So here,
# when N dot nraf becomes none, that means N is pointing to the last node now.
# N dot nres becomes null only when Y points to here. Ok?so now we need to write the condition for this.
# I need to check the data of yarn. That is the last node with the X. I need to compare that,
# whether it matches to the last node. Here we need to write the condition for last node.
# I need to check end dot data is equal to X here. Here inside this, I will take another reef, and I will take N dot.
# Last node data is equal to equal to X. If it is true, if it is true, means I want to delete the last node.
# So to delete the last node, what you need to do is you need to point this as none. You need to take this as none. Sohere,
# N dot previousreference, next reference, as none here, N dot previous node, nref as none. Else, if it doesn't match,
# that means it is not X is not present in the doubly linked list. So now we are done. So here first,
# I need to check whether linked list is empty. If it is not empty,

# Forward traversal operation
# 1. Start From the first node print its data
# 2. move to the second node, print its data
# 3. continue step 2 until last node data is printed

# Backward traversal operation
# 1.Start from the last node, print its data
# 2.Move to the second last note print its data
# 3.Continue step to until the first node data is printed.

#The primary reason for the difference in output between the two sets of code lies in how they handle the modification of the self.head pointer during traversal.

#First Set of Code:
#python
#Copy code
#def print_ll_FORWARD(self):
#    n = self.head
#    while n is not None:
#        print(n.data, "--->", end="")
#        n = n.nref  # Move to the next node
#This code preserves the original self.head pointer by using a separate reference n for traversal. As a result, after the forward traversal, the self.head pointer is still pointing to the first node in the linked list.
#
#Second Set of Code:
#python
#Copy code
#def print_ll_FORWARD(self):
#    while self.head is not None:
#        print(self.head.data, end="")
#        self.head = (self.head.nref)  # Move to the next node
#This code directly modifies the self.head pointer during the forward traversal. As a result, after the forward traversal, the self.head pointer is pointing to None, as it has moved past the end of the linked list.
#
#Recommendation:
#It's generally a good practice to avoid modifying the head pointer during traversal to maintain the integrity of the linked list structure. If you want to preserve the original head pointer, it's better to use a separate reference for traversal, as demonstrated in the first set of code.
#
#Example Usage:
#python
#Copy code
#list = Double_ll()
#list.incert_empty(69)
#list.print_ll_FORWARD()  # Output: 69
#list.print_ll_Backward()  # Output: Linked List is Empty!
#If you need to perform subsequent operations on the linked list, it's crucial to avoid altering the head pointer unexpectedly.

# Quotion don't perform any changes with self head in the traversal operation. Instead, perform the changes on making a duplicate of self dot head like N as we did here.
#list= Double_ll()

#list.print_ll_FORWARD()
#list.print_ll_Backward()
#Linked List is Empty!!
#Linked List is Empty!

#list= Double_ll()
#list.incert_empty(10)
#list.print_ll_FORWARD()
#list.print_ll_Backward()
#10 --->
#<--- 10

#list = Double_ll()
#list.incert_empty(10)
#list.add_begin(20)
#list.print_ll_FORWARD()
#list.print_ll_Backward()
#20 ---> 10
#10 ---> 20

#list = Double_ll()
#list.incert_empty(10)
#list.incert_empty(20)
#list.print_ll_FORWARD()
#list.print_ll_Backward()
#Double Linked list is Not Empty
#10 --->
#10  --->

#list = Double_ll()
#list.add_begin(20)
#list.print_ll_FORWARD()
#list.print_ll_Backward()
#20 --->
#20  --->

#list = Double_ll()
#list.add_end(100)
#list.print_ll_FORWARD()
#list.print_ll_Backward()
#100 --->
#100  --->

# Example Usage:
#list = Double_ll()
#list.add_begin(4)
#list.add_after(10,4)
#list.print_ll_FORWARD()
#list.print_ll_Backward()
#4 --->10 --->
#10 ---> 4 --->
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  # next reference
        self.pref = None  # previous reference

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
                print(n.data,"--->",end="")
                n = n.nref  # Move to the next node

    def print_ll_Backward(self):
        print()
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n.nref is not None:  # Move forward to reach the last node
                n = n.nref

            # Print backward without modifying self.head
            while n is not None:  # Backward traversal starting from the last node
                print(n.data,"---> ", end="")
                n = n.pref

    def incert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Double Linked list is Not Empty")  # if ll is not empty

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
              # Temporary variable for the new node
            new_node.nref = self.head
            self.head.pref =new_node
            self.head = new_node  # Update the head to the new node

    def add_end(self, data):
        new_node = Node(data)  # new_node 4269[|86|]
        if self.head is None:
            self.head = new_node
        else:
            n = self.head  # Temporary variable for traversal
            while n.nref is not None:  # Move forward to reach the last node
                n = n.nref
            n.nref = new_node  # Update the last node's next reference
            new_node.pref = n  # Set the previous reference for the new node

    def add_after(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x == n.data: #4200[1010|69|2300]
                    break
                n=n.nref
            if n is None:
                print("The Given Node Does not Get found in the Double Linked List")
            else:                                        # this method is for incerting a node after the last node thats means n.nref is none 
                new_node = Node(data)      #new_node [|77|]                             | new_node 5240[|77|]    ----------------------------
                new_node.nref = n.nref     #4269[2300|86|-]-->Null nnode [|77|None]     | Null<--5100[-|420|1010]--->new_node 5420[|77|1010]
                new_node.pref = n          #4269[2300|86|-]-->Null nnode [4269|77|None] | Null<--5100[-|420|1010]--->new_node 5420[5100|77|1010] 
                if n.nref is not None:     #Ii will check whether we are inserting the new node after the last node or not. 
                    n.nref.pref = new_node #new_node Null<--5100[-|420|1010]--->new_node 5420[|77|]<---1010[5420|68|4200] If you're not inserting the given node after the last node, then we need to include this line. If you're inserting the given node after the last node, this line is not necessary. 
                n.nref = new_node          #new_node Null<--5100[-|420|1̶0̶1̶0̶. 5420]--->new_node 5420[5100|77|1010]<---1010[5420|68|4200]
                                           #                     5100                  1010                4200                      2300                         4269
                                           # new_node Null<--[-|420|1010]---><---[5100|68|4200]---><---[1010|69|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
                                           #           5100  x          random adress created 5420             y   1010                4200                      2300                         4269
                                           # Null<--[-|420|1̶0̶1̶0̶. 5240]---><---new_node [5100|77|1010]---><---[5420|68|4200]---><---[1010|69|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x == n.data: #if x == self.head
                    break
                n=n.nref
            if n is None:
                print("The Given Node Does not Get found in the Double Linked List")
            else:#check whether we are incerting a new node before the first node or the rest of not node
                new_node = Node(data)      # newnode 6996[|96|]
                new_node.nref = n          #i #           5100  x          random adress created 5420             y   1010                4200                      2300                         4269
                new_node.pref = n.pref     #ii # Null<--[-|420|1̶0̶1̶0̶. 5240]---><---new_node [5100|77|1010]---><---[5420|68|4200]---><---[1010|69|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
                if n.pref is not None:#It will check whether we are inserting the new node before the last node or not/rest of the node.The ndotPReF is none. That means we are inserting a new note before the first node. At that time.
                    n.pref.nref = new_node  #Don't need this statement while inserting the new node before the first node.
                else:#n.pref is None
                    self.head = new_node
                    n.pref = new_node      #iii #4200[1010|69|2300]---><---2300[4200|143|4269]n--->newnode 6996[|96|]--->6996[|96|2300]--->newnode 6996[4200(n.pref)|96|2300(n)]
                                           #4200[1010|69|2300]--->6996[4200|96|2300]<---2300[4200|143|4269]n---->4200[1010|69|2̶3̶0̶0̶  6996(n.pref.nref)]
                                           #4200[1010|69|2̶3̶0̶0̶  6996]--->6996[4200|96|2300]<---2300[4200|143|4269]n---->2300[4̶2̶0̶0̶. 6996|143|4269]n---->
                                           #           5100  x          random adress created 5420             y   1010                4200                           6996               n   2300                         4269
                                           # Null<--[-|420|1̶0̶1̶0̶. 5240]---><---new_node [5100|77|1010]---><---[5420|68|4200]---><---[1010|69|2̶3̶0̶0̶  6996]--->newnode[4200|96|2300]<---[6996|143|4269]---><----new_node [2300|86|-]-->Null         
                                           # this is for the rest cases 
                                           # incerting a new node before the first node
                                           #  newnode 1099[|99|]
                                           #            5100  x          random adress created 5420             y   1010                4200                           6996               n   2300                         4269
                                           # Null<--[-|420|1̶0̶1̶0̶. 5240]---><---new_node [5100|77|1010]---><---[5420|68|4200]---><---[1010|69|2̶3̶0̶0̶  6996]--->newnode[4200|96|2300]<---[6996|143|4269]---><----new_node [2300|86|-]-->Null              
                                           #                 1099                         n     5100  x                       5420                 y   1010                  4200                     6996              2300                      4269
                                           # newnode None--[-(ii)|99|5100 (i)]<---[N̶o̶n̶e̶. 1099(iii)|420|1̶0̶1̶0̶. 5240]---><--- [5100|77|1010]---><---[5420|68|4200]---><---[1010|69|2̶3̶0̶0̶  6996]--->[4200|96|2300]<---[6996|143|4269]---><---- [2300|86|-]-->Null  
    
    def delete_begin(self):                #                    5100                 1010                  4200                                 4590                     2300                           4269
        if self.head is None:              # new_node Null<--[-|420|1010]---><---[5100|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4590|143|4269]---><----new_node [2300|86|-]-->Null
            print(" Double Linked List empty,Not able to delete a node!")                                   
        else:                               # checking whether double linked list contain one node or maore than one node                                     
            if self.head.nref is None:      # the doubly ll is contain only one node
                self.head = None                                                                       # 1. point head to the second node                          head=2nd_node_ref                                                                          point head to the second node because head is the starting poing of the linked list
                print("Double Linked List is Empty After Deleting the Node")                           # 2. store the previous link of the second node to null     2nd_node_pref= none                     Null<--1010[-|68|4200]                             remove the previous reference from the second node and instead of giving/ it a reference give/assign it with a null value
            else:                          # the doubly ll is contain nodes and for deleting the first node
                self.head= self.head.nref  # to go the the after node before the deleting node
                self.head.pref = None      # Now, the pref will be none to make it a first node 
                                           #          1010                  4200                                 4590                     2300                           4269
                                           # Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
    def delete_end(self):                
        if self.head is None:#ll is empty
            print(" Double Linked List empty,Can't delete a node!")
        else:                             #checking whether double linked list contain one node or maore than one node                         
            if self.head.nref is None:    #Null---1010[-|68|]<---head[1010]---->head[]
                self.head = None                                                                           
                print("Double Linked List is Empty After Deleting the Node")
            else:                         #when dll contains more than one node
                n = self.head
                while n.nref is not None:    #if it is none we reached to the last node and it will come out of the loop
                    n = n.nref                          #go to the last node 
                n.pref.nref = None            #         1010                  4200                                 4590                     2300                           4269
                                              # Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null
                                              #          1010                  4200                                 4590                     2300                          
                                              # Null---[-|68|4200] Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|2300]---><---[4200|143|4̶2̶6̶9̶. ]--->Null
    
    def delete_by_value(self,x):
        if self.head is None:                                        #ll is empty
            print(" Double Linked List empty,Can't delete a node!")
        else:                                                        #ll is not empty
            if self.head.nref is None:                               #if you have only node node in ll#Null---[-|68|]#if ll contains only one node check whether you to delete the node or not
                if x == self.head.data:
                    self.head = None                                   #Null---1010[-|68|]<---head[1010]---->head[]                             
                else:
                    print("x doesnot present in Dll")
            else:
                if self.head.data==x:#if this is true you want want to delete the first node#this part if the code executed if x == self.head.data: self.head = None #checking whether we are deleting the first node of the ll or not
                    self.head = self.head.nref # if you have multiple nodes and you want to delete the first node
                    self.head.pref = None          # head[5100]     5100                 5240                  1010                 4200                     2300                           4269
                                               #ii # Null<--[-|420|5240]---><---[5100|77|1010]---><---[5240|68|4200]---><---[1010|69|2300]---><---[4950|143|4269]---><----new_node [2300|86|-]-->Null  
                                               #self.head= self.head.nref  # to go the the after node before the deleting node
                                               #self.head.pref = None      # Now, the pref will be none to make it a first node 
                                               # head[5240]  5240                  1010                 4200                     2300                           4269
                                               #ii # Null[Null|77|1010]---><---[5240|68|4200]---><---[1010|69|2300]---><---[4200|143|4269]---><----new_node [2300|86|-]-->Null  
                else:# if we want to delete the middle node
                    n = self.head
                    while n.nref is not None:
                        if x == n.data:
                            break# if this line does not execute go to the second node
                        n=n.nref
                    if n.nref is not None:# if this line executed if x == n.head: break and we found our specific node
                        n.nref.pref = n.pref                  # new_node 4269[ 2̶3̶0̶0̶. 4590|86|-]-->Null  
                        n.pref.nref = n.nref                  # new_node 4590[4200()|99|2̶3̶0̶0̶. 4269]
                    else:                    # if we want to delete the end node
                                                              #          1010                  4200                                 4590                   n  2300                                                 4269
                                                              # Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200()|99|2̶3̶0̶0̶. 4269]---><---[4590(n.pref)|143(n.data)|4269(n.nref)]---><----new_node [ 2̶3̶0̶0̶. 4590|86|-]-->Null
                                                              #          1010                  4200                               x  4590                 y     4296
                                                              # Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|4296]---><----new_node [4590|86|-]-->Null
                        if n.data == x:                           
                            n.pref.nref = None                                    #new_node 4590[4200|99|4296]---->-new_node 4590[4200|99| 4̶2̶9̶6̶. -]--None
                        else:
                            print("x is not present in DOUBLE LINKED LIST")                                          #          1010                  4200                               x  4590                 y     4296 n
                                                              # Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99|4296]---><----new_node [4590|86|-]-->Null
                                                              #           1010                  4200                               x  4590       
                                                              # Null---[-|68|4200]---><---[1010|69|2̶3̶0̶0̶  4590]---><---new_node [4200|99| 4̶2̶9̶6̶. -]--None
           
# Example Usage:       
list = Double_ll()
#list.incert_empty(19)
#list.add_begin(4)
list.add_end(100)

#list.add_after(10,4)
#list.delete_begin()
#list.delete_by_value(0)
list.print_ll_FORWARD()
list.print_ll_Backward()


# Circular linked list is also a type of linked list. It is the collection of nodes where each nodes is connected through links in such a way that it forms a circle.
# Circular liquid list is a linked list whose notes are connected in such a way that it forms a circle.
#  And circular linked list can be single linked list, or D Linked list. That means we have two types in circular linked list. That is, we can make the singly linked list as circular linked list. So circular, singly linked list. Or we can have circular doubly linked list. We can make single linked list as circular. And also we can make doubly linked list as circular.
# In the circular singly linked list, the last node contains the link of the first node.
#  That is, I'll show the diagram in singly linked list every node contains data Field and a link There's the link or reference of the next node and the last node contains the reference to nune or null.
#  But in a circular signal linked list, the last node will contain the reference or link of the first node.So that's why it will form a circle. 
# this node thi is the first node It contains the reference of this note. And this is the second node, which contains the reference of this node. This is the last node which contains the reference of the 1st node. So here we can see a circle. That's why it is called as circular single linked list.
#             1010          4100         3100
# head[1010] [10|4100]--->[20|3100]--->[30|1010]
#               <-----------------------------
# And in the case of doubly linked list,in the doubly linked list, every node contains the  data field and two links. Here every node contains next node link as well as previous node link. 
# Want to make this doubly linked list circular. Then here in the last node, next link reference should be point to none in the doubly linked list. But here it will point to the first node. It will store the reference of the 1st node. Here you can see. And also.in the first node, the previous reference will contain the reference of the last node. Instead,of containing none or null value, it contains the reference of the last node So now here we can see it is a circle Because circular doubly linked list forms a circle of nodes. You can start from any node, and you can traverse the entire linked list, because it is a circle. So if you start from any point, you can complete the entire circle.
#  <------------------------------------------------------
#     1010                  5100                4200    
# [4200|10|5100]---><---[1010|20|4200]---><---[5100|30|1010]
#   <------------------------------------------------
# But the problem.with the circular doubly linked list is if proper caution is not taken, then it may lead us to an infinite loop, because it does not contain none value or null value. We may not identify this topping condition, and it may leads us to an infinite low. So we need to be careful while dealing with this circular, linked list. 
# circular linked list operations like. I'm sll and doubly linked list here also. We'll discuss about three operations that is insertion, deletion and traversal operation.
# In the insertion operation will add new notes to the linked list in the deletion operation will remove the notes from the linked list. And in the traversal operation, we'll go through each node and will print its data. So let's discuss every operation one by 1.
# First, we'll discuss about the insertion operation.And herefore the demonstration purpose, I'll take the circular, singly linked list. And now, if I want to add any new node to the circular, singly linked list, then how to do that?
# So 1st let me take the 1st condition. That is, if I want to add the new node when the linked list is completely empty, that is when head is pointing to none. If head is pointing to none, that means linked list is empty. If that case, I want to insert the new node to the circular linked list, then first step is 
# you need to create the node. So the first step in insertion operation is we need to create the node like.this you can create the node and here.what you need to do is you need to point the link or reference of this node to here itself. And we need to point head to the new node because this is the circular linked list. The link or reference of this node need to point to itself because it contains only one node. So to form a circle 8 need to point to itself like this. This is how you can insert the new node when linked list is completely empty.
#  Now if linked list contains few nodes at that time.if I want to add the new node So for that, let's take few scenario. That is how to insert at the beginning of the linked list. At the end of the linked list and in middle. So in the insertion operation, we'll discuss about these three scenarios. That is how we can insert the new node at the beginning of the circular linked list. At the end of the circular linked list, and in the middle of the circular linked list. So first we'll discuss about this at the beginning of the circular linked list. 
# So for that 1st step is same, we need to create the new node. So let's create a node like this I'll take a data field. After that, I need to store here the reference of the first node, previous, 1st node. So I need to point this to here. That means here you need to contain 1010 and later head need to point to this, because this is the first node 
# Because this is the first node now.So point head to the new node and. also the last node should contains the reference of the first node. This node now instead of pointing here it need to point here.and it should contains the reference of this node. If I take its reference as 3200 should contain 3 200 here. So if you want to add the new node at the beginning of the circular linked list, first you need to create the node. Next you need to change the reference or link of the newly created node.
#  It should contain the difference of the previous first node and next head need to point to the new node and the last node need to store the reference of the first node. That is the new node in this way. In this way you can add the new node at the beginning of the circular linked list.
#  Next, let us say how to add the new node at the end of the circular linked list. The first step is same. We need to create the node. So let's create the node like this with the data field.
#  Next here, this node should contain the reference of the new node. So this need to point to here, not here. Sohere you should contain the reference of this node. If I take reference as 6000 should contains the reference here. You should store this reference. And also.this node, the newly created node, should point to the first node, right? It should store the reference of first node, that is 3 2. Was it 200 so to add? So to add the new node at the end of the circular linked list, first you need to create the node. Next you need to store the new node reference in the last node of the linked list here and in the new node you need to store the reference of the first node.Now let's discuss about the next scenario. That is how to insert the new node at the middle of the circular scene.Clean linked list. So for that, I will insert here between these two nodes. So for that 1st step is same, create the node. So let's create a node like this, and I will take 500. I will take its reference as 7200. Now here what you need to do is you need to store.So this will become the next node. So 5100. You need to store that. And here you need to change its reference. It need to store the reference of the new node. This need to store the reference of new node that is 7200. Because we are inserting the new node in the middle of the linked list. So it is same as the how we insert the new node in the middle of the single linked list.You need to change its reference and its reference. So in this way, it can perform the insertion operation.
#  Next, lets discuss about the deletion operation. It's about to scenarios. That is how to delete the node at the beginning of the circular linked list. At the end of the circular linked list and in the middle. Or you can call it as delete by value also. So let's discuss about every scenario. First, let's see how to delete the node at the beginning of the circular linked list.
# So we want to delete this node, right? So for this what you need to do is you need to point head to the 2nd node, the next node. After that here in the last node you should store the reference of the this node 2nd node. Not this because we want to delete this node so it need to point to hERE
#About the cover cell operation in the traversal operation, what we'll do is we'll go through every node and will print its data. But in the circular linked list, you need to be careful because we don't have any none or null value to identify the last node right in the single linked list and in the double linked list. The last node will point to the null or null. It will store the reference to null or null. That's why we can identify the last node easily. We can start from the first node, and we can stop in the last node. Butin this circular linked list, last node will not point to null or null, right? That's why we need to start from the next node of the last node. That is nothing but the first node. And we need to print its data, and we need to move to the next node. And we.need to do this until I'll reach the node which contains the reference to the first node, that is the last node. So instead of checking the references node reference is null or null. We need to check. It is equal to the reference stored in head. The first node reference like that, you need to perform the tower cell operation. So this is about the circular linked list and its operation. 


# ADD AT BEGIN [1|]1042
#             1042          1010          4100         3100
# head[1042] [142|1010]--->[10|4100]--->[20|3100]--->[30|1̶0̶1̶0̶  1042]
# ADD AT END [1|]1420
#             1042          1010          4100         3100               1420
# head[1042] [142|1010]--->[68|4100]--->[69|3100]--->[70|1̶0̶4̶2̶. 1420]--->[99|1̶0̶4̶2̶. 1042]
# ADD AT MIDDLE [77|]1077
#             1042                 1010        1077         4100                3100                   1420
# head[1042] [142|1010]---><---[68|̸4̸1̸0̸0̸  1077 ]--->[77|4100]<---[69|3100]---><---[70|1̶0̶4̶2̶. 1420]---><---[99|1̶0̶4̶2̶. 1042]

# DELETE AT BEGIN [1|]1042
#               1010          4100         3100
# head[1010] [10|4100]--->[20|3100]--->[30| 1̸0̸4̸2̸  1010]
# DELETE AT END [1|]1420
#             1042          1010          4100         3100               1420
# head[1042] [142|1010]--->[68|4100]--->[69|3100]--->[70|1̶0̶4̶2̶. 1420]--->[99|1̶0̶4̶2̶. 1042]
#             1042          1010          4100         3100           
# head[1042] [142|1010]--->[68|4100]--->[69|3100]--->[70|  1̸4̸2̸0̸  1042]
# DELETE AT MIDDLE [77|]1077
#             1042                 1010        1077         4100                3100                   1420
# head[1042] [142|1010]---><---[68|̸4̸1̸0̸0̸  1077 ]--->[77|4100]<---[69|3100]---><---[70|1̶0̶4̶2̶. 1420]---><---[99|1̶0̶4̶2̶. 1042]
#             1042                  1077         4100                3100                   1420
# head[1042] [142| 1̸0̸1̸0̸  1077]--->[77|4100]<---[69|3100]---><---[70|1̶0̶4̶2̶. 1420]---><---[99|1̶0̶4̶2̶. 1042]



