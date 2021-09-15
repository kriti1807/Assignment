print("\t\t\t\t\t\t\tCALCULATOR")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
p=int(input("Choose an option:"))
x=int(input("Enter Number 1="))
y=int(input("Enter Number 2="))

if p==1:
    print("The summation of the above the two numbers is", x+y)
elif p==2:
    print("The difference of the above two numbers is", x-y)
elif p==3:
    print("The product of the above the two numbers is", x*y)
else:
    print("The division of the above the two numbers is", x/y)
