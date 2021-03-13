names=["india","pak","aus","eng","sa","srilanka","aukland","indonesia"]
uplist=list(map(lambda str:str.upper(),names))
print(uplist)
lst=list(filter(lambda str:str[0]=='a',names))
print(lst)
from functools import reduce
ls=[10,11,12,13]
ls1=[10,21,14,12]
lst2=[10,14,21,12]
lst3=[14,21]
sum=reduce(lambda num,num2:num+num2,ls)
print(sum)
#highest
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,ls)
print(high)

#common elements in 2 list
diff=list(filter(lambda no1:no1 in ls1 and lst2,ls))
print(diff)