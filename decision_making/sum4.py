a = input("Enter number")
#print(str(a))
res=0
for i in range(1, int(a)+1):
    st = str(a) * i
    res = res + int(st)
print(res)
