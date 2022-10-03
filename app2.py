#string -> text
# -> geheel getal
#float -> komma getal
#boolean -> true or false
#x="5"
#y=5
#z=5.0

import math



def print_leeftijd(a,b):
    print(a)
    print(b)

k = int(input("leeftijd"))
z = int(input("lengte: "))



def old_enough_to_drive(leeftijd):
    if leeftijd > 18:
        print ("oud genoeg om te rijden")
    else:
        print("mag nog niet rijden")


print_leeftijd(k,z)
old_enough_to_drive(k)


def calc_sqrt(getal):
    x = math.sqrt(getal)
    print(x)

print_leeftijd(k,z)
old_enough_to_drive(k)
calc_sqrt(k)


def getallenTellen(lijst):
    count = 0
    for i in lijst:
        if i < 5:
            count += 1
    print(count)

x = [1,2,3,4,5,6,7,8,9]
getallenTellen(x)
