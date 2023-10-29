function ourRandomRange(ourMin, ourMax){
    return Math.floor(Math.random() * (ourMax - ourMin + 1)) +ourMin
}

console.log(ourRandomRange(7,16))