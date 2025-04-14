#write a program to get a multiplication table from 10 to 1 instead of 1 to 10
n=int(input("enter the number of table you want to get "))
count = 10
while count <=10 and count >=1:
    product= n*count
    print(n,"*",count,"=",product)
    count = count - 1