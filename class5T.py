#create a class named triangle
#create an object from it. the object will have three attributes named a,b and c that represent the sides of the traingle
# the trangle class will have two methods 
#i) the int method to inialize the sides
#ii) a method to calculate the perimeter of the traingle from its sides 
# the Perimeter of the trangle should be printed from outside of the class
class Triagle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def calculate_the_perimeter(self):
        perimeter=self.a+self.b+self.c
        return(perimeter)
    
result = Triagle(3, 6, 9)
perimeter = result.calculate_the_perimeter()
print("result=",perimeter)