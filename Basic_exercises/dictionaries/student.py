
# Exercise 1
# Create an empty dictionary
dictionnary = {}

# Exercise 2
# Add some key-value pairs to the dictionary

dictionnary["Voornaam"] = "Olivier"
dictionnary["Achternaam"] = "Ngamp"
dictionnary["Hobby"] = "progammeren"

# Exercise 3
# Check if "Enterprise" and "Discovery" exist; if not, add them

if "Enterprise" not in dictionnary:
    dictionnary["Enterprise"] = "Eligio"
if "Discovery" not in dictionnary:
    dictionnary["Discovery"] = "Unknown"
    

# Bonus points: you could instead loop over a list of names to check


# Exercise 4
# Display the contents of the dictionary, one pair at a time

for k,v in dictionnary.items():
    print(k, ' : ', v)

# Exercise 5
# Remove "Discovery"
del dictionnary["Discovery"]
print(dictionnary)

# Exercise 6 (Bonus)
# Create dictionary by passing a list to dict()
