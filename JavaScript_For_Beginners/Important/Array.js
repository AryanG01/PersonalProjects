var pdArray = [["Aryan", 21], ['Ayush', 17]]

/*
var temp = pdArray[0]
pdArray[0] = pdArray[1]
pdArray[1] = temp
*/

// PUSH to append data to end of an array
pdArray.push(["Anamika", 54])
console.log(pdArray)

// POP to remove last item of an array
pdArray.pop()
console.log(pdArray)

// SHIFT removes first item of an array
pdArray.shift()
console.log(pdArray)

// UNSHIFT adds an item to the beginning of an array
pdArray.unshift(["Rajeev", 53])
console.log(pdArray)