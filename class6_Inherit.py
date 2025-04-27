'''
>Inheritance
.Inheritance allows us to inherit attributes and methods from apparent class to child classes.
.Perimeter is the sum of all sides of the polygon.
.If the same method is defined in both base and derived class
,Then the method of the derived class overrides the method of the base class.
.The Super()Function returns a temporary objects of the super class from a subclass. super is a object we can use this to access the method and attributes of a parent class from inside a child class. 
'''

class polygon:
    def __init__(self,sides):
        self.sides=sides

    def display_info(self):
        print("A polygon is a two dimentional shape with straight lines ")
     
    def get_perimeter(self):
         perimeter=sum(self.sides)
         return(perimeter)
        
class Triangle(polygon):#put the parent class name inside parentheses after the child class name
    def display_info(self):
        print("A triangle is a polygon with 3 sides ")

t1 = Triangle((3, 6, 9))
t1.display_info()
perimeter = t1.get_perimeter()

print("The perimeter is", perimeter)





 

    
    
    



