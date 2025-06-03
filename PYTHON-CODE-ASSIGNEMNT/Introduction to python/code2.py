a=float(input("Enter your first number: "))
b=float(input("Enter your second number: "))
c=float(input("Enter your third number: "))

if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else: 
    largest=c

print(f"The largest number of three numbers is {largest}.")
     
