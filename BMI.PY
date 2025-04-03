weight=(int(input("Enter yor weight:-")))
height=(float(input("Enter yor height:-")))

BMI= weight/height**2
print(BMI)


if BMI<18.5:
    print("Underweight")
elif(BMI<25):
    print("Healthyweight")
else:
    print("Overweight")


