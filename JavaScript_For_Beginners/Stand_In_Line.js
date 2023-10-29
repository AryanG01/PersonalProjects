function NextInLine(array, num){
    array.push(num);
    return array.shift();
}

var testArray = [1,2,3,4,5];

console.log("Before: " + JSON.stringify(testArray));
console.log(NextInLine(testArray, 6));
console.log("After: " + JSON.stringify(testArray));