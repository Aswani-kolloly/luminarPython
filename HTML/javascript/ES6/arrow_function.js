/*var a=(num1)=>(num1**3)
console.log(a(2));*/
var arr=[10,20,30,40,1,13,2,7,0]
//arr.map(n1=>n1**2).forEach(no=>console.log(no))
arr.sort((n1,n2)=>n1<n2?-1:1).forEach(n=>console.log(n))