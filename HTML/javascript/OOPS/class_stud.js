class Stud{
    constructor(name,course){
        this.name=name
        this.course=course
    }
    disp(){
        console.log(`name ${this.name} and course ${this.course}`);
    }
}
var obj=new Stud("Abhi","MBA")
obj.disp()