lst1=[2,3,11,5,7,4,1,99]
lst2=[9,2,11,45,4,2,5,8,99]
lst1.sort()
lst2.sort()
c_dict={}
k=0
for i in lst1:
    for j in lst2:
        if i==j:
            c_dict[i]=1
            break
        elif(i<j):
            break
        else:
            continue
    k+=1
print(c_dict)
print(k)