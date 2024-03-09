//optional chaining
const user = {
    firstname:"royal",
    address : {'housenumber':"101"}//check this line it explains everything.

}
console.log(user.firstname);
console.log(user.address);
console.log(user.address?.housenumber);//use ? to prevent error if next value doest exists.