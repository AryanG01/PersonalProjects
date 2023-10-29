def translator(word):
    translation = ""
    for letter in word:
        if letter.upper() in "AEIOU":
            if letter.islower():
                translation += "g"
            else:
                translation += "G"
        else:
            translation += letter
    return translation

print(translator(input("Enter a word: ")))