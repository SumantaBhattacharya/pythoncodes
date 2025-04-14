
import random
my_num= random.randint(1,9)
while(True):
 print(" I have a number in my mind. Can you guess it?. It is in between one to 10?")
 guess=(int(input("Enter Your Number:")))#If we Leave the int part, then it will take string as it data type

 if (guess==my_num):
    print("Yes, you are right.")
    break
 elif(guess>my_num):
    print("My number is greater than the number you have entered \n try again.")
 elif(guess<my_num):
    print("My number is lower than the number you have entered.")
 else:
    print("Invalid")

