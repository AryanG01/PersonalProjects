function IsItEqual(num){
    if (num == 10){
        return "They are equal";
    }
    return "They are not equal";
}

console.log(IsItEqual(10));
console.log(IsItEqual("10"));
console.log(IsItEqual(11));

function StrictEqual(num){
    if (num === 10){
        return "They are strictly equal";
    }
    return "They are not equal";
}

console.log(StrictEqual("10"));
console.log(StrictEqual(10));