#errors are of two types 
#1)syntax errors like missing parenthesis , wrong identation are usually fixed by fixing the syntax
#2)exception errors even if your code is syntactically correct it may sometimes result in a error for example if you devide a number by zero(0) you will get an error these types of errors we encounter during the runtime of the program are called exceptions
#if we try to acces a list out of range we will get the indez error exception
# Exception         | cause of error 
# FileNotFoundError | when a file that doesnt exist is accessed
# IndexError        | when the index of a sequence is out of range
# FloatingPointError| when a floating point operation fails
#Exception handling is the process of responding to exception in a custom way during the execution of a program.

numerator=10
denominator=0
print(numerator/denominator)
