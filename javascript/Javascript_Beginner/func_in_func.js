//functions inside function
function app(){
const hello = ()=>{
    console.log("helloworld");
}

    console.log("insideapp");
    hello();   
}

app();

//functions inside a function can be only called inside the function.