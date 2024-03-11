//call()

const u1 = {
    Name:"royal",
    age: 20,
    about:function(hobby,favmus){
        console.log(this.Name,this.age,hobby,favmus);
    }
}
const u2 = {
    Name:"sanmita",
    age: 14,
    }
    u1.about;
//call the function in about of u1 for u2 

u1.about.call(u2,"guitar","skrillex");

//so the function was in u1 object but still i can use it to call it for other object 

//apply
u1.about.apply(u2,["guitar","skrillex"]);
//bind 
const func = u1.about.bind(u1,"guitar", "matin");
func();

//ARROW FUNCTION THIS DONT WORK.