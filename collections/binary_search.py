lst=list()
r=int(input("enter range of list"))
print("Enter elements")
for i in range(0,r):
    lst.append(int(input()))
print("\nList\n",lst)
lst.sort()
print("\nafter sorting List\n",lst)
num=int(input("Enter number to be found"))
start=0
end=r-1
while(start<end):
    #mid=(start+end)//2
    if ((lst[start]+lst[end])==num):
        print("(",lst[start],",",lst[end],")")
        end-=1

    elif ((lst[start]+lst[end])>num):
        start=start+1
    else:
        end=end-1


