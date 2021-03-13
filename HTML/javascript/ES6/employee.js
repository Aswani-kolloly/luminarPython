class Employee{
    constructor(eid,name,sal,desig){
        this.eid=eid
        this.name=name
        this.sal=sal
        this.desig=desig
    }
printDetails=()=>{
    console.log(this.eid+this.name+this.sal+this.desig)
}
}
var emp1=new Employee(13,"Abhi",30000,"developer")
var emp2=new Employee(14,"Arun",25000,"designer")
var emp3=new Employee(15,"Aswin",20000,"analyst")
var emp4=new Employee(16,"Ajay",27000,"developer")
var emp_arr=[]
emp_arr.push(emp1)
emp_arr.push(emp2)
emp_arr.push(emp3)
emp_arr.push(emp4)
//print desig of all employees
//emp_arr.forEach(emp=>console.log(emp.desig))
//add sal by 2k
//emp_arr.map(emp=>emp.sal+=2000).forEach(sal=>console.log(sal))
//name caps
//emp_arr.map(emp=>emp.name.toUpperCase()).forEach(na=>console.log(na))
//filter:-
//emp_arr.filter(emp=>emp.desig=="developer").forEach(emp=>console.log(emp))
//sort:-
