class Employee:

    def __init__(self):
        print("constructor")
    def set_employee(self,name,id,desig):
        self.id=id
        self.name=name
        self.desig=desig
    def disp_info(self):
        print(self.id,self.name,self.desig)

obj=Employee()

obj.set_employee("Abhinav",109,"Manager")
obj.disp_info()