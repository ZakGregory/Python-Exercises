math_mark=int(input("Enter Maths mark: "))
chem_mark=int(input("Enter Chemistry mark: "))
phys_mark=int(input("Enter physics mark: "))

average=(math_mark+phys_mark+chem_mark)/3

print("Your average percentage is: "+str(average))

grade=""

if average>70:
    grade="A"
elif average>60:
    grade="B"
elif average>50:
    grade="C"
elif average>40:
    grade="D"
else:
    grade="F"

print("your grade is : "+grade)