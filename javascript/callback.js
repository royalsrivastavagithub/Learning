function myfun(callback) {
  console.log("helloworld");
  callback();
}

function myfun2() {
  console.log("hello again");
}

myfun(myfun2);
