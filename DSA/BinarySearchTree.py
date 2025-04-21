#Binary search tree is defined as a searching algorithm used in sorted array.by repeatedly dividing the search interval into half.until desired element is found or thesearch range becomes empty.
#1)Binary tree 2) binary.search tree 3) binary.search.
#2) binary.search tree
#Binary search tree is a binary tree data. tree data structure in which each node has at most two children tree.or node
# Properties or characteristics of.binary search tree 
#1)all nodes in the left  subtree have lesser  values than the node's value.
#2)All noads in the right subtree have greater values than the node's value.
#  (  100(node's value) )
#  |                    |
#  (     50   )      ( 200  )
#  |          |       |     |
#  ( 25 )  ( 70 )   (150) (250)
#  |    |    ^ !>100  ^IT HAVE TO BE LESS THAN THE 200
#  (3) (30)
#Operations of binary search tree.
#search operation:-Is used to fight whether a given dude is present in the binary search tree or not.
#The searching process begins from the root node 
#First, it will check whether binary search tree is empty or not.
#If binary search tree is empty, then the values is not present in the binary search tree.
# If it is not empty, then it will compare the.value of the root node with the given node
# If it is equal That means value is present in the binary search tree,
# If the given value is not equal.Then checkgiven value is less than the root node.or the given value is greater than the root node.
# If the.given value is less than the root node If yes, then we need to search.the left subtree.
# And if the given value is greater than the root node, then we need to search in the right subtree.

#2)Insertion insertion operation is used to add a new node with a given value at the correct position in the binary search tree.
# To insert the new node with the given value. First, we need to check whether binary search fees empty.or not.
# If the binary search tree is empty.then add a new node in the binary search tree. It will become the root node of the binary search tree
# If binary surgery is not empty, then we need to compare the value of the new node and the value of the root node.
# If it is equal, then that means we Are adding a duplicate value
# If it is not equal,And if the new node With the given value. Is greater than the root node That we need to go to the right subtree and add the new node in the binary search tree.
# And if. The new road is less than the root node. Then we need to go to the left subtree and add the new node in the binary search tree.

# 3)Deletion delete operations delete.a note.with the given value from the binary search tree.
# To delete a node from a binary search tree first.we need to check.whether binary search tree is empty or not.
# If it is not present in the binary search tree, it will print a message that the given node doesn't get found in the binary search tree
# If binary search tree is empty, we can delete a node from binary search tree.
# And if binary search tree is not empty, then we need to compare the value.that is given by the user with the node's value.
#If the given value is equal to the node's value, then delete the node.

#4) Traversing the binary search tree is a process of visiting each node in that tree exactly once in a systematic way
# i)Preorder traversal in binary search tree
# First) visit the root node 
# second) traverse the left subtree in preorder.
# 3rd traversy rights subtree
# ii) In order traversal in binary search
# To traverse a non empty binary search tree in order the following operations are to be performed in each node.
# 1st) Traverse the left subtree.
# 2nd) visit the root note 
# 3rd) Traverse, the right subtree. 
# iii)Post order traversals in binary search tree
# Two traverses non empty binary search free in post ordered the following operations are to be performed recursively at each node.
# 1st) Traverse the left subtree. 
# 2nd) Traverse the right subtree.
# 3rd) Visit the root note

#Implement a tree specifically binary search tree and tree is a collection of nodes,
# right? And here I take every node of Binary search tree contains 3 part that is the first part is key or data or value.
# And the 2nd part is left child. And the 3rd part is right childWhile writing the program,
# as I said, We are using class and object concept to implement binary circuits.
# So here, every node of tree will be an object. So here we will create a node like this.
# This is an object. And every node will contain 3 parts. 1 is key. So here we will mention key.
# And here this is the left child. It will contain the link or reference of the left child.
#  If this node does not contain the left child, then the reference will be none.
# Andhere it will contain the link or reference of the right child. And if right child is not present,
# then it will store the reference to none. Here is an example. This is a tree binary search tree.
# This is the root node which contains 10. And this is the left child of this node.
# And this is the right child of this node. And this node does not contain any child.
# And here this node contain two child nodes. So 15 and 100. 15 is the left child and 100 is the right child of twenty.
# So here in our program, we will represent this tree like this here.Every node will be an object. This is the first node,
# and it contains three part 10 500 is the reference of its left child. And 2000 is the reference of its right child. Next,
# coming to this node, it contains key, and it does not contain left node. So that is why the link or reference is none here.
# It does not contain right child. That is why none coming to this node. 20 that is the key,
# 7900 is the left child link or reference And here we can see 3200. That is the link or reference of the right child.
# And both this node does not contain left and right child. That is why we can see none here,
# right?So we are representing three like this in our program. Here, every node will be an object,
# and every object will contain 3 parts, that is key, left child and right chart. Alright. So let's write a program. 
#Implement binary search tree. I'll use only one class.
# If you want, you can use 2 class. That is, you can take a separate class to create a node,
# like we did in the linked list. In the linked list,
# we used class node and class linked list to class to implement linked list.
# But here we'll take only one class. We won't take separate class to create the node.
# So here I will take class. Here I want to implement binary search tree.
# That's why I will take the class name as binary search treeIf you want, you can take any suitable name.
# Class name is little bit lengthy. If you want, you cannot take bst also short form of binary circuitry like this.
# Take a suitable class name. And inside this class, first I will take the initialization method.
# That is, I will take in it method.You need to take two _Next ien it,
# followed by double _In it method is the special method of class.
# And it is called when object is created. When object is created, this method is called automatically.
# No need to call this explicitly to call any other method. I need to mention the object name method name,
# right? But no need to call this method. It is an initialization method. It is a special method of class.
# It will be called automatically when object is created. Andthis method allows the class to initialize the attribute of class.
# And next here, first, I take self parameter.
# If you.observe closely in every method of class,
# the first parameter will be self. Here, self represent the object itself.
# Self is used to represent the instance of the class.
# Instead of self, we can take any name here. The first parameter of every method represent the object itself.
# There is no rule that you need to take that parameter name as self. You can take any name, but most used name is self.
# That's where I will take the first parameter name as self. Follow.by here.
# I am taking this initialization method to initialize the attribute of the class.
# That is, we will create an object from this class, right? As I said in our program, every node is an object.
# So when I create an object, that means I am creating a node.
# And every node contains 3 parts, right, key, left, hand and right child. First,
# I need to initialize that, right? That is why we are taking this initialization method.
# So here I will take next parameter as keyWhat we are doing is, when we create an object,
# we need to mention the key. So when we are creating a node that is an object,
# we need to mention the key of that node. With that, we can create a node like thisSelf key is equal to key.
# We will initialize key. And here for left child, I will take yelchild. Is none.
# Initially we will take it does not contain any left child. And here for our child, that is the right child.
# I will take none. So what we are doing is, first here, we will create an object from this class.
# That means we are creating a node. And at that.time, while creating a node,
# I need to mention the key of that node. And initially I will take Lchild and our child as none.
# So now we are done with the initialization method. Now, if I create an object from this class,
# bst here.I need to pass key. If I did not pass key, I will get error. Because here we can see in the initialization,
# we took keyOk. So I need to mention key here. And here self is nothing but the object itself.
# So here, root. So now, if I print root key like this, and if I execute this here,we can see 10 none and none.
#An object is created. Key is 10. Lchilditional R child is null. Now, if I want, I can create another node,
# that is another object from this class. Then I can make it as left child or right child of the root node,
# or root object like this. If I want to make that as the left child, then I can take root. Lchild is equal.to BST5.
# Now, another object is created, and that object is the last child of the root node. Root object. Now,
# if I print.like this. And if I execute this.here we can see another object After creating this node,
# if I print this.first and then none. Next it is 10.here. Root key is 10 and root L child is this.
# We have leftchild. That's why we are getting this next R child is none and next it was printing root.
# Lchild key. That is Phi root L child is null. Root lchild archit is none so.It is somewhat like this.
# Here you can see the image right.But in our program, we are not adding the elements like this.
# To insert the new element to the tree, we are using insertion operation. And for that,
# we will write the separate method, and that will discuss in the next tutorial.
# So that is it for now. Guys, thank you for watching. Don't forget to subscribe to my channel.
# I will meet your next class. Then take care.And welcome to Amolas Academy Youtube channel.
# We will discussing about implementation of primary search tree using python programming language.
# And in the previous tutorial, we created a class called bst. And in that we took initialization method.
# Whenever we will create a node, every node is an object here.
# So whenever we will create a node, the three fields of that node will be initialized key,
# Y, chain and R child. And while creating an object or a node, we need to mention the data of that node.
# Andtoday, in this tutorial, we will write a method to perform insertion operation.
# While performing the insertion operation, we need to check different conditions or scenario.
# In that first scenario, or condition, is we need to check whether we are inserting the new node to the empty 3.
# That is, before inserting the node, we need to check whether tree is empty or not.

#  (  100(node's value) )
#  |                    |
#  (     50   )      ( 200  )
#  |          |       |     |
#  ( 25 )  ( 70 )   (150) (250)
#  |    |    ^ !>100  ^IT HAVE TO BE LESS THAN THE 200
#  (3) (30)


# 2nd-node[    5100|100|2100                  ]root node
#        |                                    |
#       5100                                 2100
#  1st[NULL|50|NULL       -]           2nd[7900|200|3200]2)All noads in the right subtree have greater values than the node's value.
#                                     |                 |             
#                                    7900              3200
#                              [NULL|150|NULL]     [NULL|250|NULL]IT HAVE TO BE LESS THAN THE 200
#1)all nodes in the left subtree have lesser  values than the node's value.           

class BST:
    def __init__(self,key):#Any method is a special method of class and it is called when object is created.
        self.key = key #When object is created, this method is called automatically. No need to call this explicitly to call any other method. I need to mention the object name dot method name right, but no need to call this method. It is an initialization method. It is a special method of class. It will be called automatically when object is created and this method allows the class to initialize the attribute of class.And next year, first, I take self parameter.
        self.Lchild = None #self represent the object itself. Self is used to represent the instance of the class.The first parameter of every method representing the object itself. 
        self.Rchild = None #There is no rule that you need to take that parameter in a cell. You can take any name, but most used name is self. That's why.here I'm taking this initialization method to initialize the attribute of the class that is will create an object from this class.every node is an object. So when I create an object that means I'm creating a node and every node contains 3 parts right key left hand and right child. 

R1 = BST(69)
print(R1.key)
print(R1.Lchild)
print(R1.Rchild)

R1.Lchild = BST(9)
print(R1.Lchild.key)
print(R1.Lchild.Lchild)
print(R1.Lchild.Rchild)

R1.Rchild = BST(99)
print(R1.Rchild.key)
print(R1.Rchild.Lchild)
print(R1.Rchild.Rchild)
