var array = [];
var total = 0;

for (var i = 1; i <= 5; i++){
    array.push(i);
}
console.log(array)

for (var i = 0; i < array.length ; i++){
    total += array[i]
}
console.log(total)