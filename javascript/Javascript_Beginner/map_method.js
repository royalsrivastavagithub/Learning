const people = [
{ firstName: 'John', age: 32, gender: 'Male' },
  { firstName: 'Jane', age: 25, gender: 'Female' },
  { firstName: 'Bob', age: 40, gender: 'Male' },
  { firstName: 'Alice', age: 18, gender: 'Female' },
  { firstName: "Eve", age: 35, gender: 'Female' }
];

const users = people.map(
    (user)=>{
        return user.firstName;
    }
)
console.log(users);