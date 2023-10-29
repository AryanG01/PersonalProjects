var record = {
    "Alpha": "Aryan",
    "Bravo": "Barry",
    "Charlie": "Cheng En",
    "Delta": "Dega",
    "Echo": "Eobard",
    "Foxtrot": "Faramis"
};

function PhoneBook(val){
    return record[val]
}

function CheckObj(CheckProp, Object){
    if (Object.hasOwnProperty(CheckProp)){
        return Object[CheckProp];
    } else{
        return "Not Found"
    }
}

console.log(PhoneBook("Bravo"))

console.log(CheckObj("Alpha", record))
console.log(CheckObj("Golf", record))