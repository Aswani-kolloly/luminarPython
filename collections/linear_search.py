lst=list()
f=0
r=int(input("enter range of list"))
print("Enter elements")
for i in range(0,r):
    lst.append(int(input()))
print("\nList\n",lst)
num=int(input("Enter number to be found"))
for i in range(0,r):
    if lst[i]==num:
        pos=i
        f=1
        break
if f==1:
    print("\nElemnt found at position : ",(pos+1))
else:
    print("Not found")