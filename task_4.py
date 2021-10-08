def count(a, b, c):
    D = b**2 - (4 * a * c)
    print(D)
    if D > 0:
        print("X1: " + str((- b + (D)**0.5)/ (2 * a)) + ", X2: "+ str((- b - (D)**0.5)/ (2 * a)))
    elif D == 0:
        print("X1,2: " + str((- b + (D) ** 0.5) / (2 * a)))
    else:
        print("X1,2: N/A")


def err():
    print("Please input valid input")
    getinput()


def getinput():
    print("Following [a]X^2 + [b]x + [c]")
    a = input("Enter [a] coefficient:\n")
    b = input("Enter [b] coefficient:\n")
    c = input("Enter [c] coefficient:\n")
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        err()
    else:
        count(a, b, c)


getinput()
