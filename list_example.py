lst1 = [2, 3, 4, 6, 4]
lst2 = [3, 4, 2, 3, 5]

#output [5, 7, 6, 9, 9]

output = [] #empty list

# first method
# output.append(lst1[0] + lst2[0])
# output.append(lst1[1] + lst2[1])
# output.append(lst1[2] + lst2[2])
# output.append(lst1[3] + lst2[3])
# output.append(lst1[4] + lst2[4])

# print(output)

# second method
for n in range(len(lst1)):
    output.append(lst1[n] + lst2[n])

print(output)