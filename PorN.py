#create a program to check whether a number is positive or nagative or 0.
 #for this create a variable named number and assign it to a float value based on the user input. 
#then using a if statement, check if the number variable is positive or nagative or 0
#.if number is positive, print "the number is posiive"
#. if number is nagative, print " the number is nagative "
#(and). if number is 0 ,print " the number is zero" 
number = int(input("enter a value"))
if (number>0):
    print("the number is posiive")
elif (number<0):
    print("the number is nagative")
else:
    print("the number is zero",number)

