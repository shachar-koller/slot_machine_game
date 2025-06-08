import os
import time
import random
import json

#add a display leaderboard feature
#make it that it can save multiple user's highscores

class slot_machine_game:
    MAX_LIVES = 3
    GUESS_MINIMUM = 1
    GUESS_MAXIMUM = 2
    DATA_FILE = "user_data.json"

    def __init__(self, user_name):
        self.user_name = user_name
        self.high_score = self.load_highscore()
        self.current_score = 0
        self.lives = self.MAX_LIVES

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def hide_cursor(self):
        print("\033[?25l", end="")  # Hide cursor

    def show_cursor(self):
        print("\033[?25h", end="")  # Show cursor again


    def load_highscore(self):
        try:
            with open(self.DATA_FILE, 'r') as file:
                data = json.load(file)
                if data.get("user_name") == self.user_name:
                    return data.get("highscore", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return 0
    
    def save_highscore(self):
        data = {
            "user_name": self.user_name,
            "highscore": self.current_score
        }
        with open(self.DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)

    def get_user_input(self):
        try:
            guess = int(input(f"Choose a number between {self.GUESS_MINIMUM} and {self.GUESS_MAXIMUM}: "))
            if self.GUESS_MINIMUM <= guess <= self.GUESS_MAXIMUM:
                return guess
            raise ValueError
        except ValueError:
            print("Invalid input.")
            time.sleep(1.5)
            return None
        
    def play_round(self):
        self.clear_terminal()
        guess = self.get_user_input()
        if guess is None:
            return
        
        #Animatino section
        self.hide_cursor()
        for i in range(100):
            self.clear_terminal()
            print("Choosing number...")
            print(random.randint(self.GUESS_MINIMUM, self.GUESS_MAXIMUM))
            print("\nYour guess was:", guess)
            time.sleep(0.01)

        self.clear_terminal()

        result = random.randint(self.GUESS_MINIMUM, self.GUESS_MAXIMUM)
        print("Choosing number...")
        print(result)
        print("\nYour guess was:", guess)
        time.sleep(0.5)

        if guess == result:
            print("✅ Correct!")
            self.current_score += 1
        else:
            print("\n❌ Wrong!")
            self.lives -= 1
            print(f"Subtracting one life. Lives left: {self.lives}")
        time.sleep(3)
        self.show_cursor()

    def game_loop(self):
        while self.lives > 0:
            self.play_round()

        self.clear_terminal()
        print("Game Over!")

        if self.current_score > self.high_score:
            print(f"🎉 New highscore: {self.current_score}")
            self.save_highscore()
        else:
            print(f"Your score: {self.current_score}")
            print(f"Your highscore: {self.high_score}")


def run_dev_menu():
        print("🛠 Dev mode activated. What would you like to do?")
        print("Type A to erase all saved data")
        print("Type B to run a save data test")
        dev_input = input(">> ").strip()

        if dev_input.upper() == "A":
            if os.path.exists("user_data.json"):
                os.remove("user_data.json")
                print("All saved data deleted.")
            else:
                print("No saved data to delete.")
            time.sleep(2)

        elif dev_input.upper() == "B":
            test_user = "test_user"
            test_score = random.randint(5, 15)
            test_game = slot_machine_game(test_user)
            test_game.current_score = test_score
            test_game.save_highscore()

            loaded_game = slot_machine_game(test_user)
            loaded_score = loaded_game.high_score

            if loaded_score == test_score:
                print(f"✅ Save/load test passed. Score {test_score} was saved and loaded correctly.")
            else:
                print(f"❌ Test failed. Saved {test_score}, but loaded {loaded_score}.")

            if os.path.exists("user_data.json"):
                os.remove("user_data.json")
                print()

        else:
            print("Invalid dev menu option.")


              

def main():
    user_name = input("Enter your username: ").strip()

    if user_name == "admin":
        run_dev_menu()
        return
        
    while True:
        game = slot_machine_game(user_name)
        game.game_loop()
        again = input("Play again? (Y/N): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    print("\033[?25h", end="")
    main()
