//new keyword.js
function createuser(firstname,age){
    this.firstname = firstname;
    this.age = age;
}
createuser.prototype.about = function(){
    console.log(this.firstname,this.age);
}
const user1 = new createuser("royal",6);
console.log(user1);
console.log(user1.__proto__);

for(let key in user1){
    //console.log(key);
    if(user1.hasOwnProperty(key))
    {
        console.log(key);
    }
    
}
