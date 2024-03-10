//callback functions
//this is wierd u can pass a function into a function and it will be stored in the 
//parameter variable (the whole function).and the which you call that variable with "()"
//it will work just like the orignal function which was passed in a function.


function fun1(){
    console.log("This is wierd : /");
}
function myfunc(callback){
    
    callback();
}
//called a function in a function.
myfunc(fun1);
