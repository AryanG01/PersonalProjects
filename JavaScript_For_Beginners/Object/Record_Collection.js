var collection = {
    "2458":{
        "Album": "Slippery when wet",
        "Artist": "Bon Jovi",
        "Tracks": [
            "Let It Rock",
            "You give me a bad name"
        ]
    },
    "2468":{
        "Album": "1999",
        "Artist": "Prince",
        "Tracks": [
            "1999",
            "Little Red Corvette"
        ]
    },
    "1245":{
        "Artist": "Robert Palmer",
        "Tracks": []
    },
    "5439":{
        "Album": "ABBA Gold"
    }
}


var collectionCopy = JSON.parse(JSON.stringify(collection))


function updateRecords(id, prop, val){
    if (val === "" || val === undefined){
        delete collection[id][prop]
        return collection
    } else if (prop === "Tracks"){
        collection[id][prop] = collection[id][prop] || []
        collection[id][prop].push(val)
    } else {
        collection[id][prop] = val
    }

    return collection
}

console.log(updateRecords("5439", "Track", "We will rock you"))














