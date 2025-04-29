import queue

q = queue.PriorityQueue()
q.put(69)
q.put(68)
q.put(9)
q.put(99)
q.put(77)

elements = list(q.queue)
print(elements)  # [9, 68, 69, 99, 77]
#  In a PriorityQueue in Python, elements are retrieved in ascending order based on their priority.
#  The lower the value, the higher the priority. 
print(q.get())   # Retrieves and prints the smallest element (9)
print(q.get())   # Retrieves and prints the next smallest element (68)
print(q.get())   # Retrieves and prints the next smallest element (69)

# q.get() - This line doesn't print anything, it just removes the next smallest element (77).

print(q)         # This won't show the elements, it's an internal representation of PriorityQueue

elements = list(q.queue)
print(elements)  # [99] - After the last q.get(), only 99 is left in the priority queue
