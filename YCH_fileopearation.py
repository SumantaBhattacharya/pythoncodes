


#File handling.
#creating anew file
#import os
#delete a file
#os.remove("demo.txt")#We cannot write this line between open and close.

f=open("demo.txt","r")# filemode is x to create a file
# filemode is w to writing a file
#f.write("I wanna have You in my Dinner \n")#One time one operation.
#f.write("For YOU I have bring some cheese")

#filemode is a to add a new line
#f.write(" Yum :D")
#reading a file
#filemode is r to access
#lines=f.read()
#print(lines)#To write all the lines you have.written in the note pad.

first_line=f.readline()
second_line=f.readline()
print(first_line)
print(second_line)
f.close()
