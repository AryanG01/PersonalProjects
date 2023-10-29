def say_hi():
    name = input("Enter your name: ")
    print("Hello " + name + "!")

say_hi()

def hello(name):
    print("Hello " + name + '!')

hello("Aryan")
hello("Rajeev")

def intro(name, age, gender):
    print("Hello " + name + ", you are a " + str(age) + " year old " + gender)

intro("Aryan", 20, "Male")

def power(num_1, num_2):
    return pow(num_1, num_2)
print(power(0,0))
result = power(9,9)
print(result)

def odd_even(num):
    if num %2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

odd_even(8)
odd_even(19)