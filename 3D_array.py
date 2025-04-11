# Python program to print 3D list
# importing pretty printed
import pprint
def three(a,b,c):
    list=[[[[[1] for col in range(a)] for col in range (b)] for row in range (c)]]
    return list
# Driver Code    
col1 = 5
col2 = 3
row = 2
pprint.pprint(three(col1,col2,row))