function fun(){
let count = 0;
return function onemorefun(){
    if(count === 0 )
    {
        console.log("first time called");
        
    }
    else
    {
        console.log("you already called [",count,"] times.");
        
    }
    count++;
}
}


const myfun= fun();
myfun();
myfun();
myfun();
myfun();
const myfun2 = fun();
myfun2(); 