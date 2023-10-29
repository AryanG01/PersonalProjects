function CaseInSwitch(val){
    var answer = ""
    switch(val) {
    case 1:
        answer += "Alpha";
        break;
    case 2:
        answer += "Beta";
        break;
    case 3:
        answer += "Gamma";
        break;
    case 4:
        answer += "Delta";
        break;
    default:
        answer += "Incorrect Value";
        break;
    }
    return answer
}

console.log(CaseInSwitch("a"))