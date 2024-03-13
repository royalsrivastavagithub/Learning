//promise.resolve
//promise chaining 
const mypromise = Promise.resolve(5);
mypromise.then(value=>{
    console.log(value)
})

//then() method always return promise.

