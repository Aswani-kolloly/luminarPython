word="hello hi hi hello Hello "
lst=word.split()
dict={}
print(lst)
for item in lst:
    if item in dict:
        dict[item]+=1
    else:
        dict[item]=1
print("Word count : ",dict)