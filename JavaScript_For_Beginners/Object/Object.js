var myDog = {
    "name" : "Ayush",
    "legs" : 2,
    "tails" : 0,
    "friends" : ["everything"]
}

myDog.name = "Rajeev"
console.log(myDog["name"])

myDog["height"] = 175
console.log(myDog.height)
console.log(myDog)

delete myDog.height
console.log(myDog)