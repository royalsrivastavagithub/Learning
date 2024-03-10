//spread operator
const arr1 = [1, 2, 3];
const arr2 = [5, 6, 7];

const arr3 = [...arr1, ...arr2];
console.log(arr3);

const arr4 = [..."abc"];
console.log(arr4);

const arr5 = [..."12352352364263345345345"];
console.log(arr5);
//numbers cannot spread ...
//notice the arr5 have a characters saved not numbers

const obj1 = {
  k1: "v1",
  k2: "v2",
};
const obj2 = {
  k1: "v23423",
  k3: "v2",
};
const obj3 = { ...obj1, ...obj2 };

console.log(obj3);
