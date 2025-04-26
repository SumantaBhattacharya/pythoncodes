#A queue class. So this Q Module contains different classes, like Q, Priority queue, like that.
# And here you can create the queue like this, queue and queue. And here you can mention the maximum size.
# If maximum size is equal to zero or less than that, then it will be an infinite queue.
# Otherwise you can give an maximum size to the queue.
# You can assign a maximum size to the queueAnd this queue class contains many methods.
# You can use the queue size method to get the size of the queue. You can cheque whether queue is empty or not using Q Mt.
# Or you can just queue is full or not when you use the maximum size,
# then you can cheque whether Q is full or not using Q Full Method.
# Or you can put the element to the queue using Q. So for put the syntax is like this,
# you need to put the item. And here there will be blockdefault value is two,
# and there will be a timeout. So what it will do is it will put the item to the queue.
# If block is true and timeout is none, it will block until the free slot is available.
# Once the queue is full, it will block the item until the free slot is available.
# It won't give the queue full message. Instead of that, it will wait until the free slot is available.
# If you don't want that, then you can make block as false, or you can set a timeoutok? You can set one minute or anything.
# So after waiting for one minute, it will print the message. When you take maximum size of Q is 3.
# When you enter the fourth element, instead of printing the queue is full message, it will block until you will get a free slot.
# If you don't want that, you can set block as false, or you can fix a timeout,
# or you can use another method that is called put no wait. In this syntax is like this item.
# It is similar to this when block is false, so it won't wait for the freeze slot when the queue is full.
# It will just print the message. Q is fullYou will get this condition.
# Q is full only when you will set the maximum size of the queue to a number greater than zero,
# otherwise it will be an infinite cube, right? To enter the element, either you can use put method or put no weight method.
# Next, to get the element, you can use get method or get no weight method. In the get method also, what it will do is,
# here, block is true. Time out is none. It will get the element from the queue. It will remove the element from the queue.
# Once queue is empty, what it will do is it won't print the queue empty messageInstead of that,
# it will block until the item is available. To avoid that, you can set block is false,
# or you can set a timeout like 1 minute or something after one minute, it will just print a message.
# Or you can use get no wait. And there are different methods in this class.
# If you see the documentation, you will understand this. So for now, to implement the queue,
# what I am doing is I am using the queue class from the queue module to add the element I am using the put method.
# And to get the element I am using the get method. So lets see the example 


import queue

q = queue.Queue()
q.put(68)
q.put_nowait(69)
q.put(77)

print(q.get())
print(q.get_nowait())
print(q.get())
print(q.get())# it will wait infinitely because queue is empty and we are trying to fetch elements when the queue is empty
print(q)
print(q.get_nowait())

#print(q.get())# it will wait infinitely because queue is empty and we are trying to fetch elements when the queue is empty
#print(q)

# To print the elements in the queue
#while not q.empty():
#    print(q.get())



#Hello guys and welcome to Python programming tutorials by Amalias Academy.
#  We were discussing about data structures and data structure is a way to store and organize data so that it can be used efficiently.
#  Consider in your room if your clothes are well organized or arrayed in your cupboard, then if you want to find any dress from that you can find that easily.
#  In other case, if clothes are not arranged properly if your room is messy, some clothes are there in cupboard, some on bed.
#  If your room is messy, then finding an item from that messy room is difficult, right? 
# It will take more time and energy in the same. way, if data is well organized or arranged properly,
#  then accessing that data as well as doing operation on that is easier. That's why we need data structures.
#  You can place or arrange your clothes in different ways. You can arrange them based on the color.
#  You can place all the black color outfit in one side and red color in one side like that. Or you can arrange them based on which type of cloth it is.
#  You can arrange T shirt 1 side, Kurtis 1 side pants, one side like that You will do the arrangement based on your requirement right in the same way data can be arranged in different way.
#  That's why we have different data structures like stack, queue, linked list, three graphs. We have multiple data structure because we can arrange the data in different ways.
#  Previously in this video series we discussed about stack queue.and linked list and its implementation and all these.
# three data structures comes under the linear data structure category. We have multiple data structures and we can divide this multiple data structure into two category based on how data is arranged.
#  If data is arranged linearly, those data structures comes under linear data structure. If data is nonlinearly then that data structure comes under nonlinear data structures.
#  So we have 2 types in the data structure, linear and non linear data structures.The data structure where data items are organized sequentially or linearly that data structure is called as linear data structure.
#  If it is not arranged linearly or sequentially, then that is called as non linear data structure and stack queue linked list.List data structure comes under the linear data structure category. And three and graph comes under the nonlinear data structure.
#  In linear data structure, the data items are traversed serially, one after the another. And all the items of the linear data structure can be traversed during a single run.
#  But all the data items in a nonlinear data structure may not be traversed during a single run.
#  In non linear data structure, the data items are not organized sequentially or linearly.
#  So while discussing about three and graph, we will see that. So this is about the linear and non linear data structures.
#  And the implementation of linear data structures is easier compared to not linear data structures.
#  And in the linear data structures, elements are ETA1 after the another. So when you are traversing,
#  you can access only one element directly. And we have only one level in the linear data structure,
#  but in the non linear data structure, we will have multiple levels.So we will see that while discussing about tree and graph,
#  because 3 N graph comes under the non linear data structure. So that's it for now, guys. Thank you for watching.
#  Don't forget to subscribe to my channel. I will meet you in next class. Till then, take care.
#  Hello guys, and welcome to python.
#Out three data structure. When I say the word tree, what is the first thing comes to your mind? A tree right with leaves,
#  branches, fruits, flowers, trunk, roots, etc. But today, here we are now talking about these three.
#  We are talking about 3 data structure. 3 is a nonlinear data structure which represent the relationship between the different nodes.
#  In the previous tutorial, we discussed about linear and nonlinear data structures. If the data structure arranges or organize the data linearly or sequentially,
#  then.those data structures are called as linear data structure. Stag Q Linked list comes under this category.
# If data structure organizes the data non sequentially nonlinearly or hierarchically,
#  then that data structure is called as nonlinear data structures. Entry and graphs comes under this non linear data structure category.
#  I hope you heard about family 3. We all have different generation in our family. You can represent these generations,
#  or the relationship of the family hierarchically, using family tree. So first there will be grandparents,
#  grandmother or grandfather, the root of your family. And you have the 2nd generation, next generation, like that.
#  You can represent this different generation hierarchically using family tree, or for other structure is an another example for hierarchical structure.
#  So these are the real world examples where you can arrange or organize the data hierarchically.
#  Now, coming back to the trees, we know tea is in non linear data structure andwhich will represent the relationship between the nodes.
#  And you can define the tree in another way also, like tree is the collection of entities called nodes.
#  And every nodes are connected by edges. And each node of the tree contains the value of data.
#  And it may or may not have children. Ok, so you may not be familiar with few terms of this definition.
#  Don't worry, we will see that later. For now, just remember that tree is the nonlinear data structure And it is the collection of entities called nodes.
#  And every node contain the value or data. And also, it can contain the link or reference to other nodes called children.
#  We can represent tree like this. As I said, tree is the collection of nodes. So here you can see, these are the nodes.
# And these nodes are connected by edges. So this is called as edge or link. And here, every node contains the data or value.
#  And also, it contains the link to other nodes. Here you can see, this is a node, and it can contain data or value.
#  Now I did not mention any data here. It can contain any type of data. Now, to understand trees better, you need to be familiar with the terminologies of tree.
#  The terms used with tree. So let's see the tree terminologies. The first.term is node. The individual element of three is called as nodes.
#  And every node contains data or value as well as link to the other nodes. And the next term is root node, root the topmost node of the tree is called as root or root node.
#  We can say that the root node is the origin of the three data structure. In any 3 there must be only one root node, and we never have multiple root nodes in our tree.
#  And the next term is edge or link. This is the link, or the connection between two nodes. So here,
#  whatever mark in the yellow color, these are called as edge.This everything is called as edge or link.
#  The next term is parent node, or parent.the node which has a branch from it to any other node is called as parent node.
#  Here you can see, this is the node which contains branch or edge from data. fromWhat edge from this note to another node?
#  So this is the parent node of these two node. And this node is the parent node of these 2 nodes.
#  And this node is the parent node of these two nodes. And this is the parent node of this node.
#  And this is the parent node of these three nodes. Here you can see the nodes which are highlighted are called as parent nodes.
#  Parent node can also be defined as the node which has child or children. So the next term is child node.which has a link from its parent node is called as child node.
#  So here this was the parent node of these two node. That means these two nodes are the child of this node. Children's of this node. This is the child of this node.
#  This is the child of this node. And also anode academic number of Theta. And in AT all the nodes except root node are the child nodes and all the node except root node will have a parent node.
#  And here you can see the highlighted node. These are the chi node and the next atomic siblings nodes which belongs to same parent are called as siblings.
#  Here this node and these nodes are siblings because both node parent is saying here this node and these nodes are sibling this node and this node are sibling.
#  They not be the same parents are called nodes. So here you can see the highlighted nodes. These are the sibling nodes and the next term is leaf node or leaf.
#  The node which does not have a child is called as leaf node or it is also called as external node external node is also a node with node child.
#  So if a node doesn't contain a child then that node is called as leaf node or external node. Also it is called as terminal nodes here in the example these nodes are called as leaf nodes or external nodes.
#  Next we have internal nodes. The node which has at least 1 child is called as internal node entry data structure other than list node or other nodes are the internal nodes root node is also an internal node 
# The sequence of nodes and edges from 1 node to another node is called as part between two nodes. For example,
#  the part between this node and this node is, if I take your values of A, B, C and D, then the part between A and D is A, B, C and D.
#  It is a sequence of node and edges. The edges and four nodes. So these are the few basic terms which are used with 3 data structure.
#  We talked about root edge, parent, child leaf node, internal nodes, siblings and path. And also the term simply discussed here.
#  We are familiar with all of them, or both of them. We'll use these words in real world, right? Siblings, parent style. We use this relation now like also.
#  That's why I can remember this term is easy and you can understand this more easily. This is about the three data structure introduction to P.
#  So that's one of guys. It's like Yes Academy. We were discussing about data structures and in that we were discussing about three data structure and in the previous tutorial we discussed about definition of tree and also terminology of tree terms related to tree. Today in this tutorial we will continue the discussion on tree data structure. First we will talk about the characteristics of the tray data structures. Or we can say few truths related to trees. Every tree has a special node called root node. The root node can be used to traverse every node of the tree. It is called root because three originates from the root node. If we have non empty 3 then that tree must contain the root node. And the second property or characteristics of tree is, if tree contains N nodes, then the number of edges is always 1 less than the number of nodes. That is nothing. But if we have N node, we will have N 1 edges or links here.We can see in the diagram we have total 11 nodes. And the link or edge we have is 10. So here you can see 12345678910. 
# 56789 10 if we have N nodes, we'll have N one edges.
#  That is because here we can see we don't have any link or edge to the root node. That's why we have N 1 edges.
#  Next, every child node Has only a single parent but parent can have multiple child.This side node contains only one parent.
#  Every child node contains only one parent, but a parent can have multiple children's like this.
#  Here you can see this node contains two children And the next property is trees actually contains trees within them.
#  That means trees are recursive data structures. A tree.Is usually composed of smaller trees.
#  And they are called as subtrees. The child of one node in a tree can be the parent of another tree,
#  making it the root of the sub tree. So here you can take like this. This is the left side nodes.
#  This is the right side nodes, right? So here you can take this as a subtree.I'm here for this subject.
#  This is the root node. And here also you can take this for this subject. This is the root node. Alright
#  So these are the few characteristics of the tree, or truths about the tree. Next to understand trees better,
#  we need to be familiar with few other terms or properties of trees. In the previous tutorial,
#  we discussed tree terminology. And in that we discussed about basic terms related to tree data structure.
#  Today,we will discuss few more terms. The first term is called as degree.
#  You can find out degree of a node as well as degree of a tree. So 1st let's see what is degree of a node.
#  Degree of a node is the total number of children of that node.
# So now here I will just take name for every node instead of calling this node that node I'll give M to the node tofify the nodes here.
#  While.explaining, instead of calling this node and that node.I'll call node a node B node C like that. Now,
#  if I want to find out the degree of node B, I need to find out its number of children.
# So here you can see B contains two children, that is nothing but degree of B is 2.
#  Now, if I want to find the degree of G, Node G, then it contains three children. So degrees 3.
#  Degree of node is nothing but the number of children of that node. Now, coming to the degree of a tree,
#  if I want to find out the degree of tree, then it is the highest degree of a node among all the nodes in the tree.
# So if you want to find out the degree of tree, then first you need to find out degree of all the nodes.
#  And the node which contains highest degree, that is the degree of entire tree.Degree of EA is two. Node B is 2C is 2 right?
#  D is zero.E is 1F. is. 0G. is 3H and I and J and K. All are zero. So the highest degree is three.
#  So the degree of this tree is 3. The highest.He often nodded three so degree of trees 3 here. And also,
#  you can observe one more thing, degree of leaf node is zero. So this is about degree.
#  You can find out degree of a node and degree of a tree. So the next term is level.
#  I want to find out the level of tree.In a tree, each step from top to bottom is called as level of tree.
#  The level count start from 0 and increments by one at each level or step. So here it will start from top.
#  So this is the level 0 level 1 level 2 and level 3. So the level of tree is three. If you want to find out the level of C,
#  that is 10123In 2023 if you are.3.And the next term is height.
#  Here you can find out height of node as well as height of a tree
#  So first we'll see what is height of a node.
#  Height of node is the total number of edges that lies on the longest path from any leaf node to a particular node.
# For example, if I want to find out the height of C, first I need to find out the longest path from the leaf node to C.
#  Here we can see these are the leaf nodes. And here the longest path is you can take this path, this path, or this path.
#  We have three paths which are the longest path for C from the leaf node. And the number of edges included in that is two.
#  That means height of C is 2. If I.want to find out height of B, this is the longest path from any leaf node to B.
#  So here number of edges is 2. So B is 2.for A, this is the longest path, or this or this.
#  You can take any path and number of edges is 3. So for A, It is 3.
#  Height of A is 3.You need to calculate from the leaf node.
#  You need to find out the number of edges present in the longest path from the leaf node to that mentioned node.
#  And now.what is the height of a tree? Height of tree is equal to height of the root node.So here in this example,
#  height of A, That is the root node is 3. So height of this 3 is 3. Alright?You need to find out the longest path,
#  and you need to count how many edges are present in that. So this is about the height Next term is depth.
# I want to find out the depth of a node as well as depth of 30. So let's see. What is that?
#  Depth of a node is nothing but total number of edges from root node to a particular node.For example,
#  if I want to find out the depth of C, then I need to find out the path from root to that node. So for.example,
#  if I want to find out the depth of C, so path is A to C, right?And then I need to calculate number of edges present in that.
#  So here it is one. So depth of C is 1.Just presenting that. So here it is one. So depth of C is one.
#  If I want to find out the depth of H, first I need to find out the path, that is A, B, E H.
#  We need to start from root. Next, calculate the number of 23. So depth of H is 3.
#  So that means depth of A is always zero. Just.remember, height of leaf node is always zero.
#  Depth of root node is always zero. If you want to find out the height,
#  you need to calculate the edges of longest path from the leaf node to the particular node.
#  If you want to find out the depth, then you need to start from the root node.
#  You need to calculate the number of edges from the root node to the particular node.
#  Now, if I want to find out the depth of tree,
#  then how to find out that depth of tree is nothing but total number of edges from root node to a leaf node in the longest path.
# So if I want to find out the depth of tree, you need to take the longest path from root node to leaf node.
#  So here A, B, D. And here we have A, B, E, H. Here A, C, F, here, A, C, G, K, A, C, G, J, A, C, G, I,
#  you have these many parts. We have four longest paths. The number of. edges are equal.
#  So O3 is the depth of this tree.Okay, so these are the few important terms related to three data structures.
#  Today we talked about degree level height and depth.And next, let's see the application of 3 data structure,
#  where we can use three data structures. Sobinary search trees, it is a type of water tree.
#  Is used to quickly check whether an element is present in a scent or not. So for searching purpose,
#  binary search trees are used. Heap is a kind of tree that is used for heap salt,
#  a modified version of a tree called trice is used in modern routers to store rooting information.
#  And also, let's see the different uses of tree while discussing about different types of tree.
# So that is it for now, guys. Thank you for watching. Don't forget to subscribe to my channel.
#  I will meet in next class. Till then, take careHello guys and welcome to Amola's Academy Youtube channel.
#  We were discussing about three data structure.
#  3 is a collection of entities called node and here every nodes are connected by edges and it is a nonlinear data structure and also in three we can see relationship between different nodes like parentchild relationship,
#  sibling relationship, etc.
#  And in the previous tutorial we discussed about the properties and terminologies related to tree data structure.
#  Next.we'll talk about different types of tree data structure. The first type we are discussing here is general tree
# . General tree is a type.


