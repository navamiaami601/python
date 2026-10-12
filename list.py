n1=int(input("enter a number"))
n2=int(input("enter a number"))
if n1<n2:
    min=n1
else:
    min=n2
gcd=1
for i in range(1,min+1):
    if n1%i == 0 and n2%i ==0:
        gcd=i
print(f"the gcd of {n1} and {n2} is {gcd}")

