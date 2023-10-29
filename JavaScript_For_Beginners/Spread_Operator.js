const arr1 = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN"];
let arr2;
(function(){
    // arr2 = arr1 makes them to equal to same stored data instead of copying the data
    arr2 = [...arr1] // copies the items in arr1 and spreads it into arr2
    arr1[0] = "potatoes"
})(); //important to put () at the end of namelless function
console.log(arr2,arr1)