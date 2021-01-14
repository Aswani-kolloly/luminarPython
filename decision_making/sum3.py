num=int(input("enter power"))
l=int(input("enter lower"))
u=int(input("enter upper"))
for i in range(u+1):
    if (i**num) in range(l,u):
        print(i**num)
    else:
        pass
