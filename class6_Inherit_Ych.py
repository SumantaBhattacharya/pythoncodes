#------------------------inheritance python-----------------------------
#inheritance allows us to create a class that inherits the attributes or properties and method of another class
class Animal:#parent class
    def __init__(self,name,likes):
         self.name=name
         self.likes=likes

    def walk(self):
        print("i like to take my dog to a walk"+ self.name+" my baby")

# a=Animal("Tiger")  
# a.walk()     

class Dog(Animal):#child class
    def __init__(self,name,likes):
        super().__init__ (name,likes)

    def sound(self):
        print(self.name+" Barks"+ " at the other dogs")

bruh=Dog("Johny","Bones")
bruh.sound()
bruh.walk()

bro=Dog("alsa","yoh")
bro.sound()
bro.walk()




