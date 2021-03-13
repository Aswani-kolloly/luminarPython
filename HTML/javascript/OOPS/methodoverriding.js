class Parent{
    print_msg(){
        console.log("parent class");
    }
}
class Child extends Parent{
    print_msg(){
        console.log("child class overrides parent method");
    }
}
var child=new Child()

child.print_msg()
