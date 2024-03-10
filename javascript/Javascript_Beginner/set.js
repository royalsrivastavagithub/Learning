//its like an array but all values are unique
//set is iterable.
const number = new Set([1,2,3,4,4,5]);
console.log(number);
//i tried to give two 4's but it give only one 4.
//NO DUPLICATES ALLOWED ! 
//index based access
//not always in order
//sets have own methods
number.add(4);
console.log(number);
//nothing changed
number.add(8);
console.log(number);
//changed 
number.delete(8);
console.log(number);
//8 removed
console.log(number.has(5));
//true
console.log(number.size);