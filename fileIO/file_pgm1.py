fp=open("demo","r")
lst=list()
for line in fp:
    lst.append(line.rstrip("\n").split(" "))
fp.close()
print(lst)