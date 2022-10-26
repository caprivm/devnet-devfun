# Data Structures

def legalAges():
    lifeEvent = (
        16, # Driving
        18, # Voting
        21, #Drinking
        65 #Retirement
    )

    # Example with data strcutures
    print("The legal driving age is "
        + str(lifeEvent[0]) + ".")
    print("The legal voting age is "
        + str(lifeEvent[1]) + ".")
    print("The legal drinking age is "
        + str(lifeEvent[2]) + ".")
    print("The legal retirement age is "
        + str(lifeEvent[3]) + ".")

    lifeEvent = {
        "drivingAge": 16,
        "votingAge": 18,
        "drinkingAge": 21,
        "retirementAge": 65
    }

    # Example with data strcutures
    print("The legal driving age is "
        + str(lifeEvent["drivingAge"]) + ".")
    print("The legal voting age is "
        + str(lifeEvent["votingAge"]) + ".")
    print("The legal drinking age is "
        + str(lifeEvent["drinkingAge"]) + ".")
    print("The legal retirement age is "
        + str(lifeEvent["retirementAge"]) + ".")

# List
l = ['a', 1, 18.2]
print(l[2])
l[2] = 20.4
print(l)
l.append("new")
print(l)

# Tuples
t = ('a', 1, 18.2)
print(t[0])

# Dictionaries
d = {"apples": 5, "pears": 2, "oranges": 9}
print(d["pears"])
d["pears"] = 6
d["mangos"] = 10
print(d)

# Example calling a function
legalAges()