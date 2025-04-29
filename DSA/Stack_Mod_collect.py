# We'll see how to implement stack using different modules. So first here we'll discuss about collections module.
# In the collections module, there is a class called deque.
# And we can use this class as the stack.
# Here deck stands for double ended queue.Here we can add the elements in the both the side.
# There are different methods to add the element in both the sides.
# But stack works in the lifo order, last in first out. So we need only one end to add the element and remove the element.
# So using few methods of deck class, we can create the star for the push operation. We can use append method of deque class.
# And for the pop operation, we can use pop method of the deque class Yes, the method names are same as the list methods.
# So let's see the example for this.
# So first we need to import the module collections. Next we can create the stack using collections dot.deque like this.
# Using this class, we can create this stack not.here we can see now if you want to add the element to this tab,
# you can use stack dot append. You can add the element here andAgain, add another element, and you can add another element.
# You can add element like this.
# Now, to pop the element from this, you can use pop method, ok?It will first remove 30 next.20 next, 10.
# If I again use this, it will give the error. You are popping from the empty deck. So here, method names are same.
# And this deck class contains many other methods, also, using that methods, you can add and remove element in the another end also.
# But here we want to create stack using this deck class. That's why we are using append and pop.
# Now, if you want to check whether stack is empty or not, you can use not.stack, or you can chip the length of the stack also,
# not stack. It is true, because now stack is empty. And if you want to check the element present in the top, you can use the 1 index stack of minus 1.
# Same as the list. Ok, so this is about the deque class.
# Next, using the queue You can create the stack in the queue model.
# There is a class called Lifoq. Using this, you can create the stack in the lifoqueue for the push operation you need to use.
# Put method for the pop operation you need to use. Get method. So I'll show you the example for this.
# So here you need to import queue. Next here you can create the stack using queue.
# And if I press the lower arrow button here, we can see empty here. This is the.and use this.Alright.
# So now, if you want to put element to this, you can use stack dot put. AndAnd put the element like this Now,
# if you want to perform pop operation, you can use that dot kit. It will remove 31st.20 next, 10 next.
# Now again, I use tag dot get. It will take the time to finish this function call, because now stack is empty. 
# Now it will take time. So I will close this. It will.block until it finds the element. So to solve that,
# you can use the timeout parameter in the get and put function. There is a parameter called timeout.
# If you set timeout as the positive value, for example, 1 2nd after 1 second, it will print the message.
# That is Q is empty in the get function. And in the put function, sometimes it will print. Q is full like that.
# Well, I will explain you about that. Before that, we can set a limit to this stack.
# That is, how many elements we can enter to this stack. For example,here, if I take three maximum size of the stack is 3 it only takes three elements.
# After that, it will print. Q is full message. For example, here, I took maximum size as 3. Now,
# if I put the value, so now we enter three elements. After this, if I try to enter another element, for example,
# 40. Now, the maximum size is over. Now, if I enter this here,
# what it will do is it will block until Q slot becomes empty If you want to see that message queue is full,
# then you can here set the time out. Timeout I here. I will take 1 2nd. Now,
# if I enter this here, we can see in the one second it will print. Q is full message.

import collections
Stack = collections.deque()
Stack.append(68)
Stack.append(69)
Stack.append(99)#LIFO
Stack.pop()
Stack.append(77)
Stack.append(104)
Stack.append(104)
print(Stack)
print(Stack[0])
print(Stack[-1])
print(not Stack)#stack is not empty