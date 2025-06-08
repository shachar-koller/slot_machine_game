import os
import time
import random
import json

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    user_name = input("Please input your username: ")
    high_score = 0

    lives = 3
    while lives >= 0:
        clear_terminal()
        try:
            user_input = int(input("Choose a number between 1 and 10: "))
            if not 1 <= user_input <= 10:
                raise ValueError
        except ValueError:
            time.sleep(1.5)
            continue

        for i in range(100):
            clear_terminal()
            print("\033[?25l", end="")
            print("Choosing number...")
            number = random.randint(1, 10)
            print(number)
            print("\nYour guess was:", user_input)
            time.sleep(0.01) 
        
        result = random.randint(1,10)
        clear_terminal()
        print("Choosing number...")
        print(result)
        print("\nYour guess was:", user_input)
        time.sleep(1)


        print("\033[?25h", end="")
        clear_terminal()


        
        if(result == user_input):
            print("You win! The number was " + str(result) + " and you guessed it correctly!")
            print("1 point has been added to your score.")
            high_score += 1
        else:
            print("\033[?25l", end="")
            print("You lost :( The number was " + str(result) + "\nBetter luck next time!")
            print(f"Subtracting 1 life. Lives remaining: {lives}")
            lives -= 1
            time.sleep(3.5)
            print("\033[?25h", end="")

    user_data_object = {
        "user_name": user_name,
        "highscore": high_score
    }
    json_object = json.dumps(user_data_object, indent=4)

    with open("user_data.json", "w") as outfile:
        outfile.write(json_object)

    print("Out of lives.")

play_again = True
while play_again == True:
    main()
    again = input("\nDo you want to play again? Press Y for yes, and N for no: ").lower()
    if again != 'y':
        play_again = False