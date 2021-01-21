lst=list()
r=int(input("enter range of list"))
print("Enter elements")
for i in range(0,r):
    lst.append(int(input()))
print("\nList\n",lst)
num=int(input("Enter number"))
print("\n 'pairs")
for i in range(0,r):
    for j in range(i+1,r):
        if (lst[i]+lst[j]==num):
            print("\n(",lst[i],",",lst[j],")")
