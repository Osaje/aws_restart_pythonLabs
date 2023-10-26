mystring = 'This is a string'
print(mystring)
print(type(mystring))
print(str(mystring) + " is of the data type " + str(type(mystring)))

# string concatenation
firststring = "water"
secondstring = "fall"
thirdstring = firststring + secondstring
print(thirdstring)

name = input("what is your name?: ")
print(name)

color = input("favourite color?: ")
animal = input("favourite animal?: ")
print("{}, you like a {} {}!" .format(name,color,animal))