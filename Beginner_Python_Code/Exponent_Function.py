base = int(input("Enter a Base Number: "))
power = int(input("Enter a Power Number: "))

def raise_to_power(base, power):
    new_base = 1
    for i in range(power):
        new_base = new_base * base
    return new_base
print(raise_to_power(base,power))
