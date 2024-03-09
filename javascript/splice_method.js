//splice method
//to delete or insert in arr
//splice(start,delete,insert)
const arr =  [1,2,3,4,5,6,7,8,9,10];
arr.splice(0,1);

console.log(arr);
//1 deleted

arr.splice(0,0,11)
//11 inserted
console.log(arr);



//first value is starting index then how many items to delte and then items to insert
//it also outputs deleted item just like pop();
//can use insert delete together

let deleted =arr.splice(2,4,"what","the","hell");
console.log(arr);
console.log("deleted:",deleted);