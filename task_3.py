def test(num_a: int):
    if num_a % 5 == 0 and num_a % 7 == 0:
        print("11")
    elif num_a % 5 != 0 and num_a % 7 == 0:
        print("01")
    elif num_a % 5 == 0 and num_a % 7 != 0:
        print("10")
    else:
        print("00")


def err():
    print("Not valid input")
    getinput()


def getinput():
    a = input("Enter number a: ")
    try:
        a = int(a)
    except:
        err()
    else:
        test(a)


getinput()
