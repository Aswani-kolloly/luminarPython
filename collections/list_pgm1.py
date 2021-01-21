lst=list()
new_list=list()

r=int(input("enter range of list"))
print("Enter elements")
for i in range(0,r):
    lst.append(int(input()))
print("\nList\n",lst)
print("\n new list")
for i in range(0,r):
    s=0
    for j in range(0,r):

        if lst[j]!=lst[i]:
            s=s+lst[j]
    new_list.append(s)
print(new_list)