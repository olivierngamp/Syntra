


# Exercise 1
# Create a tuple called data with two values, (1, 2) and (3, 4)

tuple = ((1,2),(3,4))
# Exercise 2
# Loop over data and print the sum of each nested tuple


for i in tuple:
    s = 0
    for j in i:
        s+=j
    print(s)

# Exercise 3
# Create the list [4, 3, 2, 1] and assign it to variable numbers
numbers = [4,3,2,1]


# Exercise 4
# Create a copy of the number list using [:]
newList = numbers[:]
print(newList)

# Exercise 5
# Sort the numbers list in numerical order
newList.sort()
x = sorted(newList)
print(newList)