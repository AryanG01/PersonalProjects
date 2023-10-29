const s = [5,7,2]
// s = [2,5,7] - an error coz can't mutate a const
//to mutate a const
s[0] = 2
s[1] = 5
s[2] = 7

console.log(s)

Object.freeze(s)

try {
    s = [1,2,3]
} catch (ex){
    console.log(ex)
}