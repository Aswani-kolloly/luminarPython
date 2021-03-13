class Parent1{
    print_msg(){
        console.log("parent class");
    }
}
class Child extends Parent{
    print_childMsg(){
        console.log("child class");
    }
}
var child=new Child()
child.print_childMsg()
child.print_msg()
