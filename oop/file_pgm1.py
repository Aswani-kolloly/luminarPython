class Employee:
    def __init__(self,id,name,desig,exp,sal):
        self.id=id
        self.name =name
        self.desig = desig
        self.exp = exp
        self.sal = sal
    def print_info(self):
        print(self.id,self.name,self.desig,self.exp,self.sal)
emplist=[]
dict_sal={}
f=open("employee","r")
for line in f:
    id,na,desig,exp,sal=line.rstrip("\n").split(",")
    emplist.append(Employee(id,na,desig,exp,sal))
for employee in emplist:
    dict_sal[employee]=employee.sal
    max_key=max(dict_sal,key=dict_sal.get)
print(max_key.name)
print(max_key.desig)
print(max_key.exp)
#print(min(sal_list))
