import string


type(3.14159)

# Single quote to put into ' a " double quote.
stringExample = 'Hamilton: "I am not throwing away my shot." Washington: "Dying is easy, young man. Living is harder."'
print(stringExample)

# Operations with strings
print("One" + "Two")
print("Abc"*3)

# The .<method> with Strings
print("My name is {}.".format("Alexander Hamilton"))
print("My name is {name}, and there's a {howmany} things I haven't done.".format(name="Alexander Hamilton", howmany="million"))
print("a b c".split(" "))
print(",".join(['a', 'b', 'c']))

# Use atributes and methods of any object in Python
a = 57
print(a.bit_length())

# Lower string and look inside an object
stringExample = "WhAt iS THIS CRaZY TEXt?"
print(stringExample.lower())
# print(dir(stringExample))

# Work with variables
firstName = "Elphaba"
lastName = "Thropp"
fullName = firstName
fullName += " "
fullName += lastName
currentLocation = "Emerald City"

print("My first name is {}".format(firstName))
print("My last name is {}".format(lastName))
print("My full name is " + firstName + " " + lastName)
print("There are " + str(len(firstName)) + " characters in my first name")
print("There are " + str(len(lastName)) + " characters in my last name")
print("I currently live in " + currentLocation)