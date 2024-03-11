//getter and setters
class person{
    constructor(fisrtname,lastname,age){
        this.fisrtname= fisrtname;
        this.lastname=lastname;
        this.age=age;
    }
    get fullname(){
        return console.log(this.fisrtname," ",this.lastname);
    }
    set fullname(fullname){
        const [fisrtname,lastname] = fullname.split(" ");
        this.fisrtname= fisrtname;
        this.lastname=lastname;
    }

}

const p1 = new person("royal", "srivastava", 20);
console.log(p1);
console.log(p1.fullname);//fullname is a function but now using get we can use it as a property
//changing p1 values using setname()
p1.fullname="sanmita srivastava";
console.log(p1);
