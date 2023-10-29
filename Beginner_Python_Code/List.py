from typing import List


friends = ["Karen", "Sherlock", "Clark", "John", "Samantha", "Jennifer", "Aryan"]

print(friends[1]) #gives the value in list at that particular index

friends[1] = "Watson"
print(friends[1])

print(friends[1:]) #gives the values from the index mentioned until and including last index

print(friends[0:3]) #gives the values from the index mentioned until and excluding last index

print(friends[0::3]) #gives the values from the index mentioned until and including last index 
                     #while skipping a designated set of numbers

print(len(friends)) #number of elements in list 


List_1 = ["Karen", "Sherlock", "Clark", "John"]
List_2 = ["Samantha", "Jennifer", "Aryan"]

List_1.extend(List_2) #Adds one list to another
print(List_1)
#if you extend a singal parameter and not a list it will break down the parameter into individual components
#extend("LIST") -> 'L', "I", "S", "T" being added to the list

List_2.append('Jacob') #Adds a singal parameter to the list only
print(List_2)
#if you append a list and not a singal parameter it will add to the original list as a singal item
#append(List_2) -> [..., ["Samantha", "Jennifer", "Aryan"]]

List_1 = ["Karen", "Sherlock", "Clark", "John"]

List_1.insert(1, "Jeffery") #inserts at that particular index
print(List_1)

List_1.remove('Karen') #removes this value from list
print(List_1)

List_1.clear() #empties the list
print(List_1)

List_1.pop() #removes last item from list
print(List_1)

print(List_1.index("Clark")) #At which index is parameter

print(List_1.count("Clark")) #how may times has Clark appeared in List 1

List_1.sort() #Arranges items in List in ascending order
print(List_1)

List_1.reverse() #Order of items in List are reversed
print(List_1)

List_4 = List_1.copy() #makes a copy of the list
print(List_4)

