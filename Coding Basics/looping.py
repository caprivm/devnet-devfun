testNum = int(input("Enter an integer to test for prime: "))
if testNum > 1:
    for i in range(2, testNum):
        if (testNum % i) == 0:
            print(testNum, "is not a prime number")
            print(i,"times",testNum//i,"is",testNum)    # El // devuelve el entero de la división.
            break
    else:
        print(testNum, "is a prime numer")
else:
    print("You must enter an integer.")