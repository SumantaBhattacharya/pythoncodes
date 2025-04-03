#the __init__() method is a special method that automatically gets called everytime when objects are created
#the __init__() method closely resembles construction  in java , c++

class student:
 

 def __init__(self, gender, marks):
        self.gender = gender
        self.marks = marks

 def class_pass_fail(self):
        if self.marks >= 35:
            return True
        else :
            return False
        
student1= student("male",69)

result=student1.class_pass_fail()
print(result)

print( student1.marks )

