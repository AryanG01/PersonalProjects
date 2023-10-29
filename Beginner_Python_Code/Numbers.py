print(1+2) #Addition

print(2-1) #Subtraction

print(1-2) #Subtraction 

print(4/3) #Division

print(4*3) # Multiplication

print(10 % 3) #Modulo Operator gives remainder

my_num = 10 % 3
print(my_num)

my_num = 10
my_num = str(my_num) #converts into a string
print(type(my_num))
my_num = int(my_num) #converts into a number, cant convert letters to number
print(type(my_num))

my_num = -10
print(abs(my_num)) #gives absolute value, i.e. converts to positive

print(pow(9, 2)) #pow(a, b) -> a to the power ofb

print(max(1,2,3,4)) #Max value present

print(min(-1,0,1,2,3,4)) #Min Value present

print(round(3.7)) #rounds odd to nearest whole number

from math import *
print(floor(3.12)) #rounds down
print(ceil(3.12)) #rounds up
print(sqrt(36)) #Square Root