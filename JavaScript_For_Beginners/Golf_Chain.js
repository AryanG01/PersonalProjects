var names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home"]

function GolfChain(par, stroke){
    if (stroke == 1){
        return names[0];
    } else if (stroke <= par - 2){
        return names[1];
    } else if (stroke == par - 1){
        return names[2];
    } else if (stroke == par){
        return names[3];
    } else if (stroke == par + 1){
        return names[4];
    } else if (stroke == par + 2){
        return names[5];
    } else {
        return names[6];
    }
}

console.log(GolfChain(5,7))