# Guess-A-Number AI
#
# Colby Brown
# (Date I Finish)


def start_screen():
    print("      ______                           ___         _   __                __                    ___    ____      ")
    print("     / ____/_  _____  __________      /   |       / | / /_  ______ ___  / /_  ___  _____      /   |  /  _/      ")                
    print("    / / __/ / / / _ \/ ___/ ___/_____/ /| |______/  |/ / / / / __ `__ \/ __ \/ _ \/ ___/_____/ /| |  / /        ")                
    print("   / /_/ / /_/ /  __(__  |__  )_____/ ___ /_____/ /|  / /_/ / / / / / / /_/ /  __/ /  /_____/ ___ |_/ /         ")                
    print("   \____/\__,_/\___/____/____/     /_/  |_|    /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/        /_/  |_/___/         ")
    print("                                                                                                                ")
    print("     ____                         _______   __________________     __                __             __          ")
    print("    / __ \________  __________   / ____/ | / /_  __/ ____/ __ \   / /_____     _____/ /_____ ______/ /_         ")
    print("   / /_/ / ___/ _ \/ ___/ ___/  / __/ /  |/ / / / / __/ / /_/ /  / __/ __ \   / ___/ __/ __ `/ ___/ __/         ")             
    print("  / ____/ /  /  __(__  |__  )  / /___/ /|  / / / / /___/ _, _/  / /_/ /_/ /  (__  ) /_/ /_/ / /  / /__          ")
    print(" /_/   /_/   \___/____/____/  /_____/_/ |_/ /_/ /_____/_/ |_|   \__/\____/  /____/\__/\__,_/_/   \__(_)         ")
    print("                                                                                                                ")
    
    input()

def play():
    global name
    low = 1
    high = 100

    print("What is your name?")
    name = input()
    print("")
    
    print(name + ", think of a number from " + str(low) + " to " + str(high) + " and I will try to guess it.")
    input("Press enter once you have thought of a number.")
    print("")
    print("If my guess is too low, say higher.")
    print("If my guess is too high, say lower.")
    print("If my guess is right, then say yes.")
    input("Press enter again.")

    got_it = False

    while got_it == False:

        comp_g = (high + low) // 2
        guess = input(name + ", is your number " + str(comp_g) + "?")

        if guess.lower() == 'higher' or guess.lower() == 'h':
            low = (comp_g + 1)

        elif guess.lower() == 'lower' or guess.lower() == 'l':
            high = (comp_g - 1)

        elif guess.lower() == 'yes' or guess.lower() == 'y':
            print("I won!")
            got_it = True
        
        else:
            print("I don't understand " + str(name) + ". Please enter higher, lower, or yes.")
            input("Press enter to continue.")
        
def play_again():

    while True:
         answer = input("Would you like to play again " + str(name) + "?")

         if answer.lower() == 'no' or answer.lower() == 'n' or answer.lower() == 'nope':
            return False
         elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True

         print("What?!?!?! Just say say or no, please.")


# game begins
start_screen()

again = True

while again == True:
    play()
    again = play_again()

print("Game Over")












