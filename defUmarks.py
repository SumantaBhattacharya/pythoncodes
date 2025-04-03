#suppose You just attended a university examination.The marks you obtain in various subjects are stored in a list like this
#marks=[55,64,75,80,65]
# you want to find the average marks you obtainedIn the examination and based on the average marks you want to find your grade
#The grading rule is like this
#1)You will get grade A if the average marks is equal to or above 80
#2)You will get great B if the averageMarx is equal to or above 60 and less than 80
#3)You will get great C if the average Marx is equal to or above 50 and less than 40
#4)And if the average marks is less than 50 you will get grade F

marks=[55,64,75,80,65]

def average(marks):
    total = sum(marks)
    print("Total:",total)
    subject=len(marks)
    print("SUBJECTS",subject)

    avg=total/subject
    return(avg)


def grade(avg):
    if avg>=80:
        print("grade A")
    elif (avg>50 or avg<60):
         print("grade B")
    else:
        print("grade C")

avgs=average(marks)
print(avgs)
grades= grade(avgs)
print(grades)





    









