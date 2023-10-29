# BMI CALCULATOR
def BMI(name):  
    print("Hello " + name + ". Please enter the following details.")
    height = input("Enter your Height: ")
    height = float(height)
    weight = input('Enter you Weight: ')
    weight = float(weight)
    height_squared = pow(height,2)
    BMI = round(weight / height_squared)
    BMI = str(BMI)
    print(name + " your BMI is " + BMI + '.' )

name = input("Enter Your Name: ")
BMI(name)