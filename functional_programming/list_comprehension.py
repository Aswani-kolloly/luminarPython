lst=[[10,20],[30,40],[50,60],[11,101],[7,71]]
ls=[num for st in lst for num in st]
print(ls)
print("even numbers")
lst_eve=[num for num in ls if num%2==0]
print(lst_eve)
#sq=[n**2 for n in lst]
#print(sq)
#find even num from given list using list comprehension