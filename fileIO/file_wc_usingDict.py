f=open("demo","r")
dict={}
for line in f:
    line1=line.rstrip("\n").split(" ")
    for word in line1:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)