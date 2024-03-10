class Car {
    constructor(model,speed){
        this.model = model;
        this.speed = speed;
    }
    about(){
        return this.model,this.speed;
    }
}
const car1 = new Car("ford", 200);
console.log(car1);
console.log(car1.about);

class extra extends Car{
    constructor(model,speed,color){
        super(model,speed);
        {
            this.color= color;
        }
    }
    about(){
        return "modified about";//now it wont go to super consturcture cuz it found about here.
    }
}
const extra1 = new extra("farrari",300,"red");
console.log(extra1);
