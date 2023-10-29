var counter = 0

function cc(card){
    switch(card){
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            counter++;
            break;
        case 10:
        case "J":
        case "Q":
        case "K":
        case "A":
            counter--;
            break;
    }

    var holdbet = "Hold"
    if (counter > 0){
        holdbet = "Bet"
    }
    return "The card count is " + counter + "\n You should " + holdbet
}

cc(2); cc("k"); cc(7); cc("K"); cc("A")
console.log(cc(4))