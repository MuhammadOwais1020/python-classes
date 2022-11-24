person = {
    "id" : 23,
    "name" : "Muhammad Owais",
    "age" : 23,
    "skills" : ['python', 'web3', 'django', 'react', 'react native']
}
# nested dictionary
persons = {
    "01" : {
        "id" : 1,
        "name" : "Muhammad Owais",
        "age" : 23,
        "skills" : ['python', 'web3', 'django', 'react', 'react native']
    },
    "02" : {
        "id" : 2,
        "name" : "Muhammad Arslan",
        "age" : 24,
        "skills" : ['python', 'web3', 'django', 'react', 'CSS', 'HTML']
    },
    "03" : {
        "id" : 3,
        "name" : "Abdul Samad",
        "age" : 22,
        "skills" : ['video editing', 'affter effects', 'graphics designing']
    }
}

print(persons['03']["skills"][1])

print(persons['03']['age'])

persons['03'] = 23

print(persons["03"])

print(persons)
# update value
persons.update({'03':24})

# add item i dictionary
persons["04"] = 56
print(persons)

# remove element
persons.pop('04')
print(persons)

# popitem() remove last inserted item 
persons.popitem()
print(persons)

# delete dict:
del persons["02"]
print(persons)

# delete complete dict
del persons

# clear dict
person.clear()
print(person)


