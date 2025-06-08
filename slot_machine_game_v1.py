import os
import time
import random

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    clear_terminal()
    try:
        user_input = int(input("Choose a number between 1 and 10: "))
        if not 1 <= user_input <= 10:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 10.")
        return

    for i in range(100):
        clear_terminal()
        print("\033[?25l", end="")
        print("Choosing number...")
        number = random.randint(1, 10)
        print(number)
        time.sleep(0.01) 
    
    result = random.randint(1,10)
    clear_terminal()
    print("Choosing number...")
    print(result)
    time.sleep(0.4)


    print("\033[?25h", end="")
    clear_terminal()


    
    if(result == user_input):
        print("You win! The number was " + str(result) + " and you guessed it correctly!")
    else:
        print("You lost :( The number was " + str(result) + "\nBetter luck next time!")

play_again = True
while play_again == True:
    main()
    again = input("\nDo you want to play again? Press Y for yes, and N for no: ").lower()
    if again != 'y':
        play_again = False