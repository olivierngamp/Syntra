
def exercise1(array2D):
    pass #write your code here
    c = 0
    for i in array2D:
        for j in i:
            c+=j
    return c

print(exercise1(([1,2,3],[4,5])))


def exercise2():
    pass #write your code here
    array = []
    for i in range(21):
        c = i**2
        array.append(c)
    print(array) 

exercise2()




def exercise3(x, y, z):
    pass #write your code here
    if x == y or y == z or x ==z:
        return 0
    else:
        print(x+y+z)

print(exercise3(3,2,3))



def exercise4(array1, array2):
    pass #write your code here

    array = []
    for i in range(len(array1)):
        array.append(array1[i] + array2[i])
    print(array)


exercise4([1,2,3,4],[5,6,7,8])




def exercise5(array):
    pass #write your code here
    newArray = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]%3 == 0:
                tuple = (i,j)
                newArray.append(tuple)
    print(newArray)
    
exercise5([[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]])