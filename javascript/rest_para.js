//rest parameters
//variable n will take all the values passed and create an array for the function.

function addall(...n) {
  let ans = 0;
  for (let i = 0; i < n.length; i++) {
    ans = ans + n[i];
  }
  return ans;
}

console.log(addall(1,2,5,8));
