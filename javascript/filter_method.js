const numbers = [1,2,3,4,4,5];
const isEven = function(number){
    return number%2===0;
}

const even_numbers = numbers.filter(isEven);

console.log(even_numbers);
//it filter the output depending on returned boolean value