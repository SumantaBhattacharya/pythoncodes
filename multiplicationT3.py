n=int(input("enter the number of table you want to get "))
count = 1
for count in range(1,11):# the range() function only work for integers
    product= n*count
    print(n,"*",count,"=",product)


print("range() is a useful function that creates a sequence of numbers. its common to use range() in a for loop to iterate the loop to a certain in number of items ")