//class
//in java classes are fake

class CreateUser {
  constructor(firstname, lastname, email, age, address) {
    console.log("constructor called");
    this.firstname = firstname;
    this.lastname = lastname;
    this.email = email;
    this.age = age;
    this.address = address;
  }
  about() {
    return this.firstname, this.age;
  }
  is18() {
    return this.age >= 18;
  }
}

const user1 = new CreateUser(
  "royal",
  "srivastava",
  "royalunofficail@gmail.com",
  18,
  "nift jodpur"
);
console.log(Object.getPrototypeOf(user1));
