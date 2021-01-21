lst=[10,11,12,13,14,15,16,17]
eve_list=[]
odd_list=[]
for i in lst:
    if i%2==0:
        eve_list.append(i)
    else:
        odd_list.append(i)
print("Even list : ",eve_list,end=" ")
print("\nSum : ",sum(eve_list))
print("Odd list : ",odd_list,end=" ")
print("\nSum : ",sum(odd_list))