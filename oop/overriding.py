class Parent:#parent class of parent is Object class
    name="parent"
    def __str__(self):#method overriding ,str defined in object class,str can return only string val
        return  self.name
ob=Parent()
print(ob)