import queue
Stack = queue.LifoQueue(3)#its a limit to the stack
Stack.put(69)#it is just like the append
Stack.put(99)
Stack.put(77)
Stack.put(104,timeout=1)# initially it will stuck into this line because the limit is up so what it will do here is add a time limit to show the error message earlier
Stack.get()
Stack.get()
Stack.get()
Stack.get(timeout=1)
#  Q is a linear data structure where the elements is inserted from one side and removed from the another side.
#  Q will be open at both the ends. That's why insertion and removing elements is done in different ends.
#  The end where elements are added is called as back, tail or rare of the queue.
#  The end where the elements are removed is called as head or front of the queue. And queue follows, prefer or lilo methodology.
#  That is nothing but 1st in, 1st out or last in, last out methodology stack.works on the lifo, right? Last in first out, but queue works on the fifo methodology.
#  First in, first out. Qdata structure works in the same way as the queue in the real world.
#  If you stand in a line to buy a ticket or grocery or something, the first person in the line will be the 1st one to buy a ticket or grocery, right? The last person from the queue will get grocery or ticket at last.
#  Same is the case with the queue data structure. The element.inserted first will leave the queue first.
#  The element which inserted last will leave the queue at last. So I will show you the example here.
#  We'll add the element 10. So here we can see the front and rare position.
#  Both are equal now. I'll add another element. 20 here we can see the rare position.
#  Next I will add 30. Next I will add 40. Next I will add 50 like this. Here we can see right now,
#  if I want to remove the elementthis removing the element is done in the another end. We added the elements in this end,
#  and we are removing the elements in another end. Your first 10 is removed because 10 is added first.
#  10 is inserted first to the queue. So 10 will be removed first. Next 20 will be removed.
#  Next, 30 will be removed. Next, 40 will be removed. Insertion and reviewing of the element is done in the different ends.
#  We can do this insertion and removing the element in another way also. For example, here,
#  I will change the front end rate position. And now.
#  we are adding the element in this end and we are removed the element from other end. You can take Q In this way also.
#  Next, the process of adding the element to the queue is called as N Q.
#  And the process of removing the element from Q is called as DQ. Next, let's see the operation performed by the queue.
#  In this stack, it will perform push pop operation, right? The most important operation of the queue is nq and Dq.
#  In the North queue, it will add the element to the queue. In the day queue, it will remove the element from the queue.
#  And also.you can perform ease full operation with the queue, that is to check whether queue is full or not.
#  You can set the limit to the queue, and you can see whether that limit is reached or not.
#  So you can check whether Q is full or not. If Q is full, you can't add more elements to the queue.
#  In the same way, you can check is empty condition. Also, you can check whether the queue is empty or not.
#  If you try to remove the element from the empty queue, then you will get the mtq message or under flow condition.
#  And also.you can check the element present in the front and rear position.
#  That is the next element which you want to remove from the queue without removing that. You can see which element is that.
#  And also the last element which you enter to the queue without renewing that you can see which element is that. Alright.
#  So this is the operation of the queue next, where we can use queue data structure.
#  Qs are used whenever you want to process things one at a time as they come in. The first in, first out,
#  for example,uploading bunch of photos, images, printing multiple documents. Or in the real life scenario,
#  call center phone systems uses skews. Alright, so this is about the queue and its operation. 
#  Good day in this tutorial, and we'll see how to implement queues in python.
#  So we can implement queues in 2 ways. 1 is using list, and another one is using the classes of different modules.
#  Today, we will discuss about how we can implement queue using list. And in the next tutorial,
#  we'll talk about the second option. So queue works in the 1st in, 1st out order.
#  And the 2 important operation of Q is nq and Dq. Northq is nothing but adding the element to the queue.
#  The queue is nothing but removing the element from the queue. Andone more important thing will be open at both this side.
#  That's why the insertion and removing the element is performed in different ends. 1st entered element will be removed 1st.
#  So this is about the queue summary. So next we will see how to use list as queues. For that, for nq operation,
#  we can use the append operation. So it will add the element at the end of the list or queue. And for dq operation,
#  that is, to remove the element from the queue, we can use pop method for. nq, we can use append method for dequeue.
#  We can use pop method. In the previous tutorial, while implementing this tag using list also, we used the same method,
#  right? Append will add the element at the end, and pop will remove the element from the end. So if I use append and pop,
#  then it will create a stack, right? But here we want Q. In the queue,
#  the operation that is insertion and removing the element is done in the different ends.
#  So for that, in the pork, we need to mention the index of the element. That is nothing but zeroth index.
#  We don't want to remove the element from the end. We want to remove the element from the front. So this side,
#  right? So that is why we need to use pop of zero. So I will show you the example. Then you will understand this.
#  So to create a queue first empty queue, you can create an empty list like this.
#  Next to add the element. Now what you need to do, you need to use append. For example, I will append 10 ok, done.
#  So now, if you want, you can check the queue right next. Next, I will add 20. Next, I add 30. Now, if you want to check Q,
#  here we can see ten, 2030 elements are added like this. Now, if you want to remove the element from the queue, that is,
#  if you want to perform dequeue operation, then you need to use queue dot pop. And you need to mention the index here,
#  0 index, remove from the front. If I did not use any index, it will remove the element from the end, then it will.
# create a stack. We don't want stack here. We want to perform insertion and removing the element in different times.
#  Here we entered the element in this side. Now we need to remove the element from this side. So now, if I enter this here,
#  we can see 1st 10 will be removed. The first entered element is 10. Right here we can see.
#  And the first removed element is also 10. Now again, if I use it, 20 will be removed.
#  If I again use this, 30 will be removed. If I again use that, it will give a error message. Pop from empty list.Ok.
#  So in this way, you can use the append method and pop method to perform lq and dq operation.
#  You can.perform this operation in another way also, as I explained you, you can insert the element in another side,
#  and we can remove the element in another side. That is the limit. You can insert the element from this side,
#  and you can remove the element from this side for the nq operation unit to use insert method. Insert.
#  And here you need to mention the index. At zero index, you want to enter. And here you can enter the element.
#  For example, here next. here I will enter 

