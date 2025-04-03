
rows, cols = (4, 5)
arr = [[0]*cols]*(rows)
#arr = [[0 for i in range(cols)] for j in range(rows)]

print("before",arr)

arr[0][3] = 1 # update only one element
print("after", arr)

for i in arr:
    print(arr)

arr[0][2] = 4 #this is a update line
for row in arr: #printing after updating # i == row
  print("<>",row)

arr[0][2] = 4 #update
print(">",row)

print("->",arr)

for row in arr:
  print("<->",arr)

print(cols)
print(rows)

print(arr[0])
print(arr[2])
print(arr[0] is arr[2])# prints True because there is only one list object being created.


arr = [[0 for i in range(cols)] for j in range(rows)] #creating an another array
print(arr[0] is arr[2])


