let num1 = 6;
let num2 = num1;
console.log("vaule of num1 is :", num1);
console.log("value of num2 is :", num2);
num1++;
console.log("vaule of num1 is :", num1);
console.log("value of num2 is :", num2);
//this was primitive data type as we can see num1 got changed but num2 didn't.

let array1 = ["item1", "item2"];
let array2 = array1;
console.log("array1:", array1);
console.log("array2:", array2);
array1.push("item3");
console.log("array1:", array1);
console.log("array2:", array2);
//this was reference data type as we can see when array1 got changed the change is also visible on array2.
