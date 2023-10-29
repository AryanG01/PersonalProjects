try:
    #value = 10/0
    num = int(input('Enter a Number: '))
    print(num)
    value = 10/0
except ZeroDivisionError:
    print("Division By Zero")
except ValueError:
    print("Invalid Input")

try:
    value = 10/0
    num = int(input('Enter a Number: '))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as val:
    print(val)    