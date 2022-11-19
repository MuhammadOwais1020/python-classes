fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

fruits_with_contain_a = []

for f in fruits:
    if "a" in f:
        fruits_with_contain_a.append(f)


print("classic method")
print(fruits_with_contain_a)

# List Comprehension
print("List Comprehension")

newlist = [f for f in fruits if "a" in f]

print(newlist)

lst1 = [2, 3, 4, 6, 4]
lst2 = [3, 4, 2, 3, 5]

addlist = [lst1[n] + lst2[n] for n in range(len(lst1))]

print(addlist)