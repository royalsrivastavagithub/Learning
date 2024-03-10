//lexical scope 
const n = "v1";
function app()
{
   
    function fun(){
        const n = "value2";
        console.log("inside fun",n);
    }
  const fun2= function(){}
  const fun3 = ()=>{}
  console.log(n);
  fun()
}
app();

//if there are two variables with same name but there are in different scope so when called it will give the value
//of variable from the nearest sope. as we can see n is decleared at 2 places one inside function and one inside a function
//whichi is also insie a function.so the value we get is from the last function