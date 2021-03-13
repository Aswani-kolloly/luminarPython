str="ABcdEEFaab"
dict={}
for item in str:
    if item not in dict:
        dict[item]=1
    else:
        dict[item]+=1

print("Character count : ",dict)
#for k,v in dict.items():
result=sorted(dict,key=dict.get,reverse=True)
print(result[0])


