# The for loop in python is used to iterate over a sequence and in each iteration we can access individual items of that sequence
text = "Sumanta Bhatacharya"
for character in text:
 print (character)
 # we see each character in a new line beacause the print function adds a new line at the end of each line by default
 # syntax
 # for item in sequence:
 # statement
 
n=len(text)#with index it uses range function
print("\nlength:-",n)
for i in range(n):
     print("index:",i)
     print(text[i])

my_friend= ["ROHIT","MOHIT","SAYAN"]
print(my_friend)
for i in my_friend:
   print(i)
 
 
#range()-When programming sometimes you will need to basically repeatively execute a block of codes but you don't have something to look over ~indranil chakraborty
for x in range(10):
   print(x)
   print("HEllo world")










