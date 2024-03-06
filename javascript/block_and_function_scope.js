//block scope and function scope 
//let and const are block scope 
//block ->
{
let n = "royal";
console.log(n);
}
//n is not defined cuz n is in a block and called outside of block 

{
    let n = "sanmita";
    console.log(n)    
}

let n= "sandeep";
console.log(n)
//var can be access outside of scope 

{
    var n2= "tadah ! ";
}
console.log(n2);