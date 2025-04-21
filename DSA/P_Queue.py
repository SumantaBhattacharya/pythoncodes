#We are discussing about data structures.
# And in that previously, we discussed about queue and how to implement queue in python.
# Today, in this tutorial,
# we will discuss about priority queue.
# Q is a linear data structure which works on few four methodology.
# The first is first out method.
# Priority queues are the modified version of the queues in which each element is associated with the priority and is served according to its priority.
# If elements with same priority occurs, they are served according to their order in the queue.
# Q Works on fifo methodologyHere I will enter an element. 10 will come here. Next I will enter 20.
# Next I will enter 30. Next I will enter 100. Next I will enter 70 something like this.
# So in queue, the element which comes first will be served first,
# that is, which will be performed 1st which will be removed 1st from the queue.
# After that, 20 will be removed. After that, 30 will be removed. After that,
# 100 will be removed. It works based on the first in first out method.
# And insertion and deletion is done in the different ends.
# Priority queue is also a queue here.
# Also, the insertion and the removal of element is done in the different end.
# ButThe removing the element is based on the elements priority.
# Each element will be associated with the priority and based on that priority it will be removed from the queue.
# If you went to buy a ticket, then you will stand in the line. The first person in the line will 1st buy the ticket.
# After that, this 2nd person in the line will get dedicated. It will works on the fifo methodology,
# but in the hospital, the critical condition patients are treated for stride. It is based on the priority.
#If the person condition is critical, then he will be treated first.
# # The priority works like thatSo the difference between the queue and priority queues in the queue,
# # the first and first out, the oldest element in the queue is removed first.
# But in the priority queue, it is not on the oldest or new element.
# It is based on its priority. For example, just imagine that 20 priorities more than this 10 then 20 is removed first.
# After that, the element which has highest priority that will be removed second. So the next question is,
# how to set the priority in some.cases, the value of the element itself is considered for the assigning the priority.
# Or you can take the tuple in that you can take the value and its priority. So you can set the priority in 2 ways.
# 1 is, you can take the value of the element itself as the priority of the element.
# Or you can take element and its priority as the tuple value.
# If you are taking the value of the element itself as the priority, then in that also you can take in 2 ways.
# 1 is, you can take the lowest element as the highest priority, lowest the element, highest the priority,
# or you can take the highest the element, highest the priority.For example, if I take the lowest element,
# highest priority, that is nothing but lowest element, will have highest priority. Then in the queue,
# it will check the lowest element here. 10. So that will be removed first. Next, quintu will be removed.
# Next 30 will be removed. Next, 50 will be removed. Next, 70 will be removed. Next 100 will be removed.
# Or if you take highest element, high priority, the highest element will be removed first.
# The 100 will be removed firstNext 70 next 50 next 30 next 20 next 10.
# So here the elements are removed based on its priority and how to set the priority.
# Either they can take the element itself as the priority,
# or you can take the tuple value in that you can take the priority and a value. So the next question is,
# how to implement priorit eq in python? You can use list for that. You can use list preliminary priority,
# or you can use the priority queue class from the queue module. There is another method called heap queue model,
# but I am not discussing about that here. To remove the element based on its priority here. First, we need to sort the list.
# If I want to do this, that is lower the number, higher priority. 1st I need to arrange the number in the ascending order.
# Then I need to remove the element. If you are entering the element from this side,
# and if I am removing the element from this side. So in the list, we will create the queue first,
# then we will add the element using the append method. After appending the value, we need to sort the queue.
# And next.we will use the pop method to remove the element from the queue. So let's see the example. Next..
#The Binary Heap. So the next method in the priority queue class,
# the entries are kept sorted using the heap queue model.
# It will use the binary heap data structure and the lowest value entries retrieved first.
# So next we will implement the priority queue using this class here. Import queue, priority queue.

queue = []
queue.append(68)
queue.append(69)
queue.append(77)
queue.append(99)
queue.append(9)
queue.append(104)
queue.append(404)
queue.append(420)
queue.sort()#priority according to their numbers
print(queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)