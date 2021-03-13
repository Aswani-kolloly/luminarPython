var numbers=[1,"abhi",13.2]
function pattern(){
   
    for(let num of numbers)
    console.log(num);
}
pattern()
numbers.push(100)
console.log(numbers);
numbers.pop()
console.log(numbers);