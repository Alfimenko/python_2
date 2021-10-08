def celtofah(cel: float):
    print(str(cel) + " in celsius will be " + str(cel * 9 / 5 + 32) + " in fahrenheit")


def fahtocel(fah: float):
    print(str(fah) + " in fahrenheit will be " + str((fah - 32) * 5 / 9) + " in celsius")


def err():
    print("not a valid answer. Try again")
    getinputs()


def getinputs():
    a = input("Would you like to know celsius from fahrenheit or other way round?\nC/F?")
    if a == "C" or a == "c":
        b = input("Input degrees - ")
        try:
            b = float(b)
        except:
            err()
        else:
            celtofah(b)
    elif a == "F" or a == "f":
        b = input("Input degrees - ")
        try:
            b = float(b)
        except:
            err()
        else:
            fahtocel(b)
    else:
        err()


getinputs()
