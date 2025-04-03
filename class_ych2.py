#class with attributes
class class_ych2:#the __init__ allow us provide values for the attributes of the class
    def __init__(self,roll,name,age):#self parameter allow us to access the the attributes and method of the class
        self.roll=roll
        self.name=name
        self.age=age
#creating a object 
#creating a instance of the class
stu1=class_ych2(180,"Sumanta",18)#instance-simply the object created from the class -instance are always unique
stu2=class_ych2(181,"arya",19)


s2=stu1.name
s3=stu1.age
print("name=",s2)
print(s3)

print("\nstudent2:",stu2.name)
