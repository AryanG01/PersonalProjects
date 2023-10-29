/*
function CheckEqual(a,b){
    if (a === b){
        return true
    }else{
        return false
    }
}
*/

// condition ? statement-if-true : statement_if_false;

function CheckEqual(a,b){
    return a === b ? true:false
}

//console.log(CheckEqual(2,"2"))

function CheckSign(num){
    return num > 0 ? "Positive": num < 0 ? "Negative" : "Zero"
}
console.log(CheckSign(0))