//getter and setters
class person{
    constructor(fisrtname,lastname,age){
        this.fisrtname= fisrtname;
        this.lastname=lastname;
        this.age=age;
    }
    static classinfo(){
        return console.log("this is a person class");
    }
    get fullname(){
        return console.log(this.fisrtname,this.lastname);
    }
    set fullname(fullname){
        const [fisrtname,lastname] = fullname.split(" ");
        this.fisrtname= fisrtname;
        this.lastname=lastname;
    }

}

const p1 = new person("royal", "srivastava", 20);
console.log(p1);
console.log(p1.fullname);

p1.fullname="sanmita srivastava";
console.log(p1);
const info = p1.classinfo;
console.log(info);