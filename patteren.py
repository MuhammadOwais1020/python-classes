# patteren
for i in range(5):
    for j in range(i):
        print(j, end="")

    print("")


# reverse
def reverse(n):
    if len(n) == 0:
        return n
    
    return reverse(n[1:]) + n[0]

n = 12345

num_string = str(n)

print("Reverse string is " + reverse(num_string))