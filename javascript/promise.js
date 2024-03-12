const bucket = ["coffee", "chips", "vegetables", "salt","rice"];

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

friedricepromise.then((myfriedrice)=>{
    console.log("lets eat",myfriedrice)
},()=>{
    console.log("no food :(");
})
