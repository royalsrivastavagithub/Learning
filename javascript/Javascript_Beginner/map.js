//map datastructure
//key can be any type

const map = new Map();
map.set('firstname:','royal');
map.set(1,"sanmita");
console.log(map);
//calling keys 
console.log(map.keys());
console.log(map);
map.set([1,2,3],"array");
console.log(map);

for(let key of map){
    console.log(key);
    console.log(Array.isArray(key));
}

for(let [key,value] of map){
    console.log(value);
}//destructured

