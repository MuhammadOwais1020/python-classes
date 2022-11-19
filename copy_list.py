x = 5
y = x

x += 1

print(x)
print(y)

lst1 = [2, 3, 4, 6, 4]
lst2 = lst1.copy()

lst2.append('A')

print(lst1)
print(lst2)

# List Join
joinlst = lst1 + lst2
print(joinlst)

for x in range(len(lst2)):
    lst1.append(lst2[x])

print(lst1)

# LIST Methods
# append()
# clear()
# copy()
# extend()
# index()
# insert()
# remove()
# reverse()
# sort()