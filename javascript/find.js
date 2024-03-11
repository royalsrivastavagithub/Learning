//find method 

const arr = ["hello","cat","royal","monkey","snake","dog"];

function islngth3(string){
    return string.length ===3;
}

console.log(arr.find(islngth3));