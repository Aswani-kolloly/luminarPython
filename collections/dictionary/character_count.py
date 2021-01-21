str="ABcdEEFaab"
dict={}
for item in str:
    if item not in dict:
        dict[item]=1
    else:
        dict[item]+=1

print("Character count : ",dict)
print(min(dict))
