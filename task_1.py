def err():
    print("try printing actual number :|")


def ask():
    a = input("Input a number:\n")
    try:
        b = int(a) % 2
    except:
        err()
    else:
        if b == 0:
            print("This is an even number")
        else:
            print("This is an odd number")


ask()
