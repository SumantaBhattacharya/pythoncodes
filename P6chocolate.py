#write a program to split chocolates fairly among childrens
choclolate=int(input("Enter the number of chocolates:"))
childrens= int(input("Enter the number of childrens:"))

chocolates_even= choclolate // childrens
print("chocolates per children:",chocolates_even)
chocolates_remaain=choclolate % childrens
print(" Remaining chocolates :",chocolates_remaain)
