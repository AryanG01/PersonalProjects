function wordBlank(myNoun, myAdjective, myVerb, myAdverb){
    var result = ""
    result += "The " + myAdjective + " " + myNoun + " " + myVerb + " " + myAdverb
    return result
}

console.log(wordBlank("dog", "big", "ran", "quickly"))