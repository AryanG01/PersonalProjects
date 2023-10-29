print('hello \nAryan')
#\n causes sentence to start from next line

print('hello \'Aryan')
#\ is the escape character as it tells python to ignore what comes next to it and print it out normally




phrase = "Aryan Ganju"
print(phrase) #print

print(phrase.index("an G")) #tells which place does the string start from

print(phrase.replace("Aryan", "Ayush"))

print(len(phrase)) #prints how many characters are in phrase including spaces

print(phrase[-1]) #prints the character in phrase that's at the specified index
                  #numbering starts from 0(A) and reverse numbering starts from -1(u)

print(phrase.lower()) #print lowercase

print(phrase.upper()) #print uppercase

print(phrase.isupper()) #checks if entire string is uppercase or not, and says either True or False

print(phrase.upper().isupper()) #converts phrase to uppercase and then checks if it is uppercase or not