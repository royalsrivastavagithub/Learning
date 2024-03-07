const numbers = [1,2,3,4,5];

const sum = numbers.reduce((index,nextindex)=>{
return index+nextindex;
});

console.log(sum);

/*
what it does : 
1.index 
2.firstindex
3.index++ 
4.repeated until no index left
*/