rows = int(input("Enter the number of rows: "))

for i in range( 0,rows+1,1 ):
    for j in range(i):
        print("*", end="")
   
    print()

rows = int(input("Enter the number of rows: "))

for i in range( rows,0,-1 ):
    for j in range(i):
        print("*", end="")
   
    print()