#We have to define a class before we can create objects
#Think of class as a blueprint of a house.It contains all the details about the floors,doors,windows etc.Based on these descriptions we built the house.House is the object.
#We can create many objects from a single class.
#class cannot be empty.
#When working with objects, variable are called attributes and functions are called methods.
#pass  statement help the class not to be empty
#put attributes inside class so the attributes created from the class have the attributes by default
#Put all methods inside class so that every objects of the class can access them.

class student:
    pass

student1 = student()  # Creating an instance of the class

student1.name = "Harry"  # Adding attributes to the instance
student1.marks = "69"

print(student1.name)  # Accessing the attributes of the instance
print(student1.marks)






