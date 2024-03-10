function hello(){}

console.log(hello.prototype);

hello.prototype.name="royal";
hello.prototype.age="age";
hello.prototype.fun=function(){
    return this.name,this.age;
}

console.log(hello.prototype);

//prototype is a free space default created when a function is created.