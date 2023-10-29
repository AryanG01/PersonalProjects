var contacts = [
    {
        "firstName" : "Akira",
        "lastName" : "Laine",
        "number" : "053236543",
        "likes" : ["Pizza", "Coding", "Brownie Points"]
    },    
    {
        "firstName" : "Harry",
        "lastName" : "Potter",
        "number" : "0994372684",
        "likes" : ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName" : "Sherlock",
        "lastName" : "Holmes",
        "number" : "0487345643",
        "likes" : ["Intriguing Cases", "Violin"]
    },
    {
        "firstName" : "Kristian",
        "lastName" : "Vos",
        "number" : "Unknown",
        "likes" : ["JavaScript", "Gaming", "Foxes"]
    }
];

function ProfileLookup(name, prop){
    for (var i = 0; i < contacts.length; i++){
        if (contacts[i]["firstName"] === name){
            return contacts[i][prop] || "No such property";
        }
    }
    return "Name not found";
}

console.log(ProfileLookup("Harry", "likes"));