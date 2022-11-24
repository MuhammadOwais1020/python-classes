person = {
    "id" : 23,
    "name" : "Muhammad Owais",
    "age" : 23,
    "skills" : ['python', 'web3', 'django', 'react', 'react native']
}
# print keys
for x in person:
    print(x)

# print values
for x in person:
    print(person[x])

# print values
for x in person.values():
    print(x)

# pritn keys
for x in person.keys():
    print(x)

# pritn keys and values
for key, value in person.items():
    print("Key: " + key)
    print("Value: " + str(value))


