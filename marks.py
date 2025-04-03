#suppose you are a university student and to pass the examination you need to score 33 or more. if your score is 35 or more then you have passed the examination
marks=int(input("Enter your marks:"))
if (marks>=33 and marks<50):
    print ("3rd DIVISION")

elif (marks>=50 and marks<60):
    print ("2nd DIVISION")

elif (marks>=60 and marks<100):
    print ("1nd DIVISION")
       
elif (marks>=0 and marks<33):
    print ("failed")
else :
    print ("Invalid Input!")