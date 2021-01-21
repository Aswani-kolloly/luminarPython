list=[1,2,13,27]
s=0

for item in list:
    s=s+item
    if item%2==0:
        print(item)
print("Sum : ",s)