# a complex number has real and imaginary parts, when we add two comples numbers we need to add the real and imaginary part separately.
# for example 3+2i here 3 is a real number and 2i is a imaginary number
class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def add(self,other):#def add(numb1,numb2):  #other: Any
     real =numb1.real + numb2.real
     imag=numb1.imag + numb2.imag
     result=ComplexNumber(real,imag)

     return(result)
    

numb1=ComplexNumber(69,96)
numb2=ComplexNumber(6,9)


result= numb1.add(numb2)
print("real=",result.real)
print("imaginary=",result.imag)




