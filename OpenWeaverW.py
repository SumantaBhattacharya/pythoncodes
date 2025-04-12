weight= (float(input("enter your weight:")))
unit=(str(input("enter unit in LBS(L) or kg(K):".upper() )))
if (unit)=="L":
    convert=weight*0.45
    print(f"you are{convert}kilos")
else:
     convert=weight*0.46
     print(F"you are {convert} pounds")
