let arr1 = [1, 2, 3];
//clone
let arr2 = [].concat(arr1);
//this way memory will net be referenced for arr2 and separate memory will be used.

//spread
let arr3 = [...arr1];

//slice
let arr4 = arr1.slice(0);

//slice is the fastest
