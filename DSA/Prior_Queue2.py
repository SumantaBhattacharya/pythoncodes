#  In a PriorityQueue in Python, elements are retrieved in decending order based on their priority.
#  The higher the value, the higher the priority. 

#The append method only accepts one argument, so you need to create tuples explicitly.
#The sort method does not return a value, so when you print q.sort(reverse=True), it prints None.
q = []
q.append((69, "Alexa"))#tuple
q.append((68, "Moon"))
q.append((77, "Angila"))
q.append((6.9, "Emily"))
q.append((99, "Sunny"))
print(q)

q.sort()
print(q)

q.sort(reverse=True)
print(q)

D=q.pop(0)
print("Deleted:",D)
print(q)#to dlete from the last element

#q.pop()#to delete from the first element element
#print(q)