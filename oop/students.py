
class Student:
    def __init__(self,na,cs):
        self.name=na
        self.course=cs
    def __str__(self):
            print("object")
obj1=Student("aswani","mca")
obj2=Student("abhi","mca")
obj3=Student("Hari","ba")
lst=[]
lst.append(obj1)
lst.append(obj2)
lst.append(obj3)
c=0
for i in lst:
    if i.course=="mca":
        c+=1
        print(i.name)
print(c)