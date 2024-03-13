function mypromise(){
    return new Promise((resolve,reject)=>{
        resolve("resolved");
    })
}

mypromise().then(value=>{
    console.log(value);
    value += " again";
    return value;
}).then((value)=>{
    console.log(value);
})