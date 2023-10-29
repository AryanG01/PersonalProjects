#Must state the relative location, copy it after right clicking the text file
#remember to always close file in the end
Employee_File = open("Files\Employees.txt", "r") #r - read file only

#print(Employee_File.readline())
#print(Employee_File.readline())

print(Employee_File.readlines()[1])

#print(Employee_File.read())

#print(Employee_File.readable())
Employee_File.close()

#Employee_File = open("Files\Employees.txt", "r+") #r+ - read and write
#Employee_File.close()

#Employee_File = Employee_File =open("Files\Employees.txt", "w") #w - write/change in the file
#Employee_File.close()

#Employee_File = open("Files\Employees.txt", "a") #a - append information to the end of the list
#Employee_File.close()

Employee_File = open("Files\Employees.txt", "r") #r - read file only
for employee in Employee_File.readlines():
    print(employee)
Employee_File.close()