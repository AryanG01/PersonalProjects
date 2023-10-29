Employee_File = open("Files\Employees.txt", "a") #'a' will add to the bottom of the file
Employee_File.write("\nKelly - Customer Services") 
Employee_File.close()

Employee_File = open("Files\Employees.txt", "w") #While 'w' will erase original file and only write new line
Employee_File.write("Kelly - Customer Services")
Employee_File.close()

Employee_File = open("Files\NewFile.txt", "w") #This will create a new file with only the new line
Employee_File.write("Kelly - Customer Services")
Employee_File.close()

#both scenarios will need .write