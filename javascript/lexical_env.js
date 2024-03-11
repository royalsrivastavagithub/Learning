const lastname = "srivastava";

const printname = function(){
    const firstname = "royal";
    
    function fun(){
        console.log(firstname);
        console.log(lastname);    
    };
   
    fun()

}
printname();

//when javascript is unable to find variable in current scope.
//it starts checking in the above scope and it keeps checking
//until it reaches global windows as we can see we are calling
//last name in a function which is also in a function but still
//we get output

