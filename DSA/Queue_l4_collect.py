#Double ended Q Class from the collections module.
# This deck or DQ, or double ended queue, is a class which contains many methods.
# And in this you can enter the values from the both ends. That is, it provides the methods which allows us to enter the data from both ends.
# Here, here you can enter the data as well as you can remove the data from this side.
# Also, you can enter the data, and you can remove the data. This is the left side, and this is the right side And if you want to enter the data from this side,
# then you need to use the append method here. And if you want to remove the element from this side,
# you need to use the method name pop. When we implement a stack using this class, we use these two methods, right? Now,
# if you want to enter the element from this side, then you can use append left method, because this is the left side.
# You are appending from the left side. And now, if you want to remove the element from this side,
# you need to use pop left.To implement queue. Q Works on the fifo technology, right? First in first out.
# The insertion and removing the element is done in the different ends. So to implement the queue,
# you can use append left to insert the value. And you can use path to remove the value.
# Or you can use append method to insert the value. And you can use popleft to remove the value.
# So lets see the example for thisFirst, i'll use append left hand pop

# appendleft--->[]<---pop
#    popleft--->[]<---append

import collections
Queue = collections.deque()#It will create an empty queue
Queue.appendleft(68)
Queue.appendleft(69)
Queue.appendleft(77)
print(Queue)
Queue.pop()
print(Queue)

Q = collections.deque()
Q.append(99)
Q.append(104)
Q.append(420)
Q.popleft()
print(Q)
print(not Q)
print(Q[-1])
print(Q[0])