# Exercise 1
# Create a tuple "cardinal_numbers" with "first", "second" and "third"
cardinal_numbers = ("first","second","third")

# Exercise 2
# Display the second object in the tuple

print(cardinal_numbers[1])

# Exercise 3
# unpack the tuple into three string and display them
for i in cardinal_numbers:
    print(i)

# Exercise 4
# Create a tuple containing the letters of your name from a string

my_name = tuple("Olivier")
print(my_name)



# Exercide 5
# Check whether or not x is in my_name
print("x" in my_name)

# Exercise 6
# Create tuple containing all but the first letter in my_name
my_name = tuple("Olivier")
print(my_name[1:])