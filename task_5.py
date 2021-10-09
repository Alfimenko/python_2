import random as rand
import time




def main():
    print("║  ╠═╬═╣ -=-   -= GUESS THE NUMBER! =-  -=- ╠═╬═╣  ║\n")
    time.sleep(0.5)
    print("Welcome to the [GUESS THE NUMBER!]\n")
    time.sleep(0.5)
    print("Rules are simple!\n * Enter number corresponding ceiling of random number\n * Enter "
          "number of tries to guess\n * First reaching 3 points wins!")
    time.sleep(0.5)
    max_number = get_max_number()
    tries = get_max_tries(max_number)
    game(max_number, tries)


def get_max_number():
    a = input("Enter maximum number from range:\n  ->  ")
    try:
        a = int(a)
    except:
        print("Invalid input. Ya aint fooling anybody. Try again.")
        get_max_number()
    else:
        if a <= 10:
            print(
                "Dont you think this is a little to easy for you?\n"
                "Be a good human and come up with number bigger than 10"
            )
            case_bad_number = True
            while case_bad_number:
                a = input("Enter new VALID number:"
                          "  ->  "
                          )
                try:
                    a = int(a)
                except:
                    print("NO. STOP.")
                else:
                    if a <= 10:
                        print("NO. STOP.")
                    elif a >= 1000:
                        print("O.o")
                        time.sleep(1)
                        print("Okay... As you wish")
                        case_bad_number = False
                    else:
                        print("Ok. Now this input is valid")
                        case_bad_number = False
        elif a >= 1000:
            print("O.o")
            time.sleep(1)
            print("Okay... As you wish")
        return a


def get_max_tries(max_num):
    a = "0"
    a = input("Enter number of tries you want to have to guess the number:\n  ->  ")
    b = tries_check(a, max_num)
    if b > 0:
        return b
    else:
        get_max_tries(max_num)


def tries_check(input_tries_begin, n):
    try:
        input_tries = int(input_tries_begin)
    except:
        print("Invalid input. Ya aint fooling anybody. Try again.")
        get_max_tries(n)
    else:
        if input_tries > (n // 8) + 2:
            b = input("Isn't it a bit too much tries? Like "
                      + str(input_tries) + " for " + str(n)
                      + " total numbers? I recomend you choosing better number.\n(Y/N?): -> "
                      )
            if b == "Y" or b == "y":
                print("Thats a good choice :)")
                return 0
            if b == "N" or b == "n":
                print("I guess someone wants to play \"Baby mode\". It is your choice :P")
                return input_tries
        elif (n // 8) - 2 > input_tries > 0:
            print("Oooh. Chalanging yourself? I like it. Lets continue!")
            return input_tries
        elif input_tries == 0:
            print("I apreciate that you willing to give me a free win but i think we would be better off with more "
                  "tries ;)")
            return 0
        else:
            print("Number of tries accepted")
            return input_tries


def get_rand_number(n):
    a = rand.randint(0, n)
    return a


def game(num, tries):
    score_human = 0
    score_pc = 0
    game_round = 0
    while True:
        if score_human < 3 or score_pc < 3:
            game_round += 1
            print("\n----------------------------------\nRound " + str(game_round) + "! Current score: \nHuman: " + str(score_human) + "\nPC: " + str(score_pc))
            time.sleep(0.5)
            print("Computer thinks of a number from 1 to " + str(num) + "...")
            time.sleep(0.5)
            rand_num = rand.randint(1, num + 1)
            current_tries = tries
            while current_tries > 0:
                a = input("Computer has made its choice! Take a guess:\n  ->  ")
                try:
                    a = int(a)
                except:
                    print("Not valid number was entered. Try again!")
                    pass
                else:
                    if a == rand_num:
                        score_human += 1
                        print("Correct!")
                        break
                    else:
                        current_tries -= 1
                        print("Wrong! " + str(current_tries) + " left!")
                        if current_tries == 0:
                            score_pc += 1
        if score_human == 3:
            print("\n ╠═╬═╣ -=- Human wins! Congratulations! -=- ╠═╬═╣ ")
            time.sleep(3)
            break
        elif score_pc == 3:
            print("\n ╠═╬═╣ -=- Computer wins! Too bad :P -=- ╠═╬═╣ ")
            time.sleep(3)
            break


main()
