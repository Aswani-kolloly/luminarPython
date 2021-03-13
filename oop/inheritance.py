class Parent:
    def  call(self):
        print("parent meth")
class Child(Parent):
    pass
c=Child()

print(c)
print(type(c))
print(id(c))