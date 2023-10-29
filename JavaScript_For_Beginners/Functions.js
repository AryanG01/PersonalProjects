var myGlobal = 10;

function fun1(){
    //var oopsGlobal = 5
    oopsGlobal = 5
}

function fun2(){
    var output = "";
    if (typeof myGlobal != "undefined"){
        output += "myGlobal: " + myGlobal;
    }
    if (typeof oopsGlobal != "undefined"){
        output += "\noopsGlobal: " + oopsGlobal;
    }
    return output
}

fun1();
console.log(fun2());