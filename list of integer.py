n=int(input("total number of integer"))
list=[]
for i in range(n):
    a=int(input("enter an integer"))
    if a<100:
        list.append(a)
    else:
        list.append("obver")
    print(list)
