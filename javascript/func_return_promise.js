//funcction returning promise

function ricePromise() {
    const bucket = ["coffee", "chips", "vegetables", "salt","rice"];
  return new Promise((resolve, reject) => {
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
}

ricePromise().then((myfriedrice)=>{
    console.log("lets eat",myfriedrice)
},()=>{
    console.log("no food :(");
})