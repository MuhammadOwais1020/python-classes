# agelst = [21, 22, 20, 23, 34, 26]
# print(agelst[2:5])

lst = ["apple", "mango", 23, 34.5, "apple"]

print(lst)

# lst[1] = "banana" #changing value mango to banana
# print(lst)

# for l in lst:
#     print(l)

# print("Length of the string: " + str(len(lst)))

# print(type(lst))

# add new member in list
lst.append("banana")

print(lst)

lst.insert(1, "Oranges") #add new member on 1st index

print(lst)

# fruits
fruits = ["apple", "banana", "mango"]
# animals
animals = ['cat', 'dog', 'goat']

# extend lists 
fruits.extend(animals)

print(fruits)
print(animals)

# remove member from list
fruits.remove('apple')

print(fruits)

del fruits[3]
print(fruits)


# Loop
for l in fruits:
    print(l)

for i in range(len(fruits)):
    print(fruits[i])

# clear list
fruits.clear()

print(fruits)

print(range(4))
# Python Collections (Arrays)
# There are four collection data types in the python programming language:
# 1. LIST: is a collection which is ordered and changeable. Allows duplicate members.
# 2. TUPLE: is a collection which is ordered and unchangeable. Allows duplicate members.
# 3. SET: is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# 4. DICTIONARY: is a collection which is ordered and changeable No duplicate members

# dictionary
data = {
    "key": "value",
    "age": 23,
    "name": "Muhammad Owais"
}
data['age'] = 24
print(data['age'])