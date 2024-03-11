function hello(){}

console.log(hello.prototype);

hello.prototype.name="royal";
hello.prototype.age="age";
hello.prototype.fun=function(){
    return this.name,this.age;
}

console.log(hello.prototype);


function createuser(firstname,lastname,email,age,address){
    user.firstname = firstname;
    user.lastname = lastname;
    user.email = email;
    user.age = age;
    user.address = address;
    return user;
}

createuser.prototype.about = function(){
    return this.firstname,this.age;
}

console.log(createuser);
console.log(createuser.prototype);