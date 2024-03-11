//function returning function

function fun(){
    
    function hello(){
        console.log("helloworld");
    }
    return hello;
}
const  ans = fun();
console.log(ans)
ans();

//a function can return a function as it happend here
//in the end calling ans calls the hello() function