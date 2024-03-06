function array_search(aar,n)
{
for(let i=0;i<arr.length;i++)
{
    if(arr[i]===n)
    {
        return i;
    }
}
return -1;
}
const arr = [1,2,3,4,5];
const n = 1;
console.log(array_search(arr,n));