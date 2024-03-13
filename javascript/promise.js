setTimeout(() => { console.log("[setTimeout]") },0)
setInterval(() => { console.log("[setInterval]") },700)
console.log("[start]")
const bucket = ["coffee", "chips", "vegetables", "salt","rice"];
//promise 
const friedricepromise = new Promise((resolve, reject) => {
  if (
    bucket.includes("vegetables") &&
    bucket.includes("salt") &&
    bucket.includes("rice")
  ) {
    resolve("Fried Rice");
  } else {
    reject();
  }
});

//checking promise 
friedricepromise.then((myfriedrice)=>{
    console.log("lets eat",myfriedrice)
},()=>{
    console.log("no food :(");
})


//a task 
for(let i=0 ; i<=100;i++){
  console.log(Math.random(),i)
}

//end
console.log("[stop]")


//promises have more priority than setTimeout.