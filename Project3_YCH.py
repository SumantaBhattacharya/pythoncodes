#----------------------quiz app python-----------------------
q1='''What is the correct syntax to output "Hello World"  in python?
a)echo("Hello World")
b)p("Hello World")
c)print("Hello World")
d)echo "Hello world"
'''
q2='''Which one is not a legal variable name?
a) my_var
b) my-var
c) _myvar
d) Myvar
'''
q3='''What is the correct file extension for python files
a) .pyth
b) .pt
c) .py
d) .pyt
'''
q4='''Which method can be used to return a string in uppercase letters
a) upper()
b) toUpperCase()
c) uppercase()
d) upperCase()
'''
q5='''Which operator is used to multiply numbers?
a) X
b) *
c) #
d) %
'''

#Dictionary

Questions={q1:"c",q2:"b",q3:"c",q4:"b",q5:"b"}#there is no connection with the string if uou enter c it will say it is the correct answer
name=(input("Enter your name:"))#JESIKA
score=0
print("Sup?",name,"Vanda Mataram")

for i in Questions:
    print(i)

    skip=(input("DO YOU WANT TO SKIP THIS QUESTION, please type yes/no:"))
    if skip == "yes" or skip == "YES":
        continue

    answer=(input("press the correct option(a/b/c/d):"))

    if (answer==Questions[i]):#is is to match the answer with uts question
        print("Correct Answer","You got 1 point")
        score=score+1
        print("current score is",score)
    else:
        print("Wrong Answer","You lost 1 point","the correct answer is",Questions[i])
        score=score-1
        print("current score is",score)
    
    Q=input("if you dont want to continue then you can simple press the exit button(type exit) otherwise simply press the enter key---:")
    if Q=="exit" or Q=="Exit" or  Q=="EXIT":
        break



print("Final Score is",score)
