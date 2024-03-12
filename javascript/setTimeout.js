console.log("start");
function delay() {
  for (let i = 0; i < 3; i++) {
    console.log("inside for loop [", i, "]");
  }
  
}
setTimeout (delay, 0);
console.log("stop");

//start prints first end prints second then loop starts.