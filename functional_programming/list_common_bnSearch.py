lst1=[2,3,11,5,7,4,1]
lst2=[9,2,11,45,4,2,5]
l=0
h= len(lst2)
c_dict={}
k=0
for i in lst1:
    l = 0
    h = len(lst2)
    while(l<=h):
        mid=(h+l)//2
        if lst2[mid]<i:
            l=mid+1
        elif lst2[mid]>i:
            h=mid-1
        else:
            c_dict[i]=1
            break
        k+=1
print(c_dict)
print(k)