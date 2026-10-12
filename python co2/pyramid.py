def disp_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i * j ,end="")
        print()
n=int(input("enter th enumber of steps"))
if n<1:
    print("please enter a postitive number")
else:
    disp_pyramid(n)
