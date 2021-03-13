class Demo{
    add(){
        console.log("zero argument method");
    }
    add(n1,n2){
        console.log("two argument method");
    }

    add(n1,n2,n3){
        console.log("3 argument method");
    }

}

var ob=new Demo()
ob.add()
ob.add(2,5)
ob.add(1,2,3)
//only latest defined method is invoked.