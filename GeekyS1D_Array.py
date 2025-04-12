'''
entitle array is an object that provide a mechanism for storing several data items with only 1 identifier thereby simplifying the task of data management 
array is beneficial if you need to store group of elements of samearray stores the elements of steam data type 
in python array can 'Increase and decrease their size dynamically 
'''

# Create Array Example 1
import array as arr
stu_roll=arr.array('f',[420,96,69,143,6.9])# 'i'= integer |  'float' object cannot be interpreted as an integer |'int' object can be interpreted as an float this is called implicit type casting because of the size of datatype
print(stu_roll[0])#Access one dimensional array elements
print(stu_roll[:])#when we perform slicing the end input is not included
print(stu_roll[1:4])
print(stu_roll[:0])

print(type(stu_roll))
print(id(stu_roll))#In python every object has an indentity. the id of an object is always unique and constant for this object during its lifetime  

print(dir(stu_roll))#we can list out all the attributes and methods of a given object using the dir () function 




for i in stu_roll:#without index
     print(i,end=" ")

n=len(stu_roll)#with index it uses range function
print("\nlength:-",n)
for i in range(n):
     print("index:",i)
     print(stu_roll[i])

stu_roll.remove(420)
print(stu_roll)
stu_roll.append(420)
print(stu_roll)
stu_roll.pop()#romoves the last item
print(stu_roll)
stu_roll.insert(1,6.8)#insert expected 2 arguments we can incert one item as desired location by using incert method
print (stu_roll)

print(stu_roll.index(69))#based on the latest or updated list it gives the output





    
