//methods are function inside object

const person={
    firstname:"royal",
    age:20,
    about:function(){
        console.log('name:',this.firstname,"age:",this.age);
    }
}//object with about function

console.log(person.about());

