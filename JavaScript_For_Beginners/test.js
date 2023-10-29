function f(a,b,c){
    var sum = 0;
    sum += a > b && c ? a*a : b > a && c ? b*b : c*c
    return sum
  
  console.log(f(2,3,4))