import os
import time
import random
import json

# Multi-user slot machine game with leaderboard functionality
# Features: Multiple user highscore tracking, leaderboard display, user login system

class slot_machine_game:
    MAX_LIVES = 3
    GUESS_MINIMUM = 1
    GUESS_MAXIMUM = 3
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
                # Check if user exists in the data
                if self.user_name in data:
                    return int(data[self.user_name])  # Ensure it's an integer
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            pass
        return 0
    
    def save_highscore(self):
        # Load existing data
        try:
            with open(self.DATA_FILE, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        
        # Update user's highscore only if current score is higher
        if self.user_name not in data or self.current_score > data[self.user_name]:
            data[self.user_name] = self.current_score
            
            with open(self.DATA_FILE, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        return False
    
    def display_leaderboard(self):
        try:
            with open(self.DATA_FILE, 'r') as file:
                data = json.load(file)
                
            if not data:
                print("📊 Leaderboard is empty!")
                return
                
            # Sort users by highscore (highest first), ensure scores are integers
            sorted_users = sorted(data.items(), key=lambda x: int(x[1]), reverse=True)
            
            print("🏆 === LEADERBOARD === 🏆")
            print()
            for i, (username, score) in enumerate(sorted_users[:10], 1):  # Show top 10
                if i == 1:
                    print(f"🥇 1st: {username} - {score} points")
                elif i == 2:
                    print(f"🥈 2nd: {username} - {score} points")
                elif i == 3:
                    print(f"🥉 3rd: {username} - {score} points")
                else:
                    print(f"   {i}th: {username} - {score} points")
            print()
            
        except (FileNotFoundError, json.JSONDecodeError):
            print("📊 Leaderboard is empty!")

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
        print()

        if self.current_score > self.high_score:
            print(f"🎉 New highscore: {self.current_score}")
            self.save_highscore()
        else:
            print(f"Your score: {self.current_score}")
            print(f"Your highscore: {self.high_score}")
        
        print()
        print("Press 'S' to show leaderboard or any other key to continue...")
        choice = input(">> ").strip().lower()
        if choice == 's':
            self.clear_terminal()
            self.display_leaderboard()
            input("\nPress Enter to continue...")
            self.clear_terminal()


def run_dev_menu():
    while True:
        print("🛠 Dev mode activated. What would you like to do?")
        print("Type A to erase all saved data")
        print("Type B to run a save data test")
        print("Type C to manually enter user data")
        print("Type D to view all stored data")
        print("Type F to delete a specific user")
        print("Type E to exit dev mode")
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

            # Clean up test data
            try:
                with open("user_data.json", 'r') as file:
                    data = json.load(file)
                if "test_user" in data:
                    del data["test_user"]
                    with open("user_data.json", 'w') as file:
                        json.dump(data, file, indent=4)
                    print("Test data cleaned up.")
            except (FileNotFoundError, json.JSONDecodeError):
                pass
            
            time.sleep(2)

        elif dev_input.upper() == "C":
            # Manually enter user data
            username = input("Enter username: ").strip()
            if not username:
                print("Invalid username.")
                time.sleep(2)
                continue
            
            try:
                score = int(input("Enter score: ").strip())
                if score < 0:
                    print("Score must be non-negative.")
                    time.sleep(2)
                    continue
            except ValueError:
                print("Invalid score. Must be a number.")
                time.sleep(2)
                continue
            
            # Load existing data
            try:
                with open("user_data.json", 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            
            # Add or update user data
            data[username] = score
            
            with open("user_data.json", 'w') as file:
                json.dump(data, file, indent=4)
            
            print(f"✅ User '{username}' with score {score} has been added/updated.")
            time.sleep(2)

        elif dev_input.upper() == "D":
            # View all stored data
            try:
                with open("user_data.json", 'r') as file:
                    data = json.load(file)
                
                if not data:
                    print("📊 No stored data found.")
                else:
                    print("📊 All stored user data:")
                    print(json.dumps(data, indent=4))
                
            except (FileNotFoundError, json.JSONDecodeError):
                print("📊 No stored data found or file is corrupted.")
            
            input("\nPress Enter to continue...")

        elif dev_input.upper() == "F":
            # Delete a specific user
            try:
                with open("user_data.json", 'r') as file:
                    data = json.load(file)
                
                if not data:
                    print("📊 No user data found to delete.")
                    time.sleep(2)
                    continue
                
                print("📊 Current users:")
                for username in data.keys():
                    print(f"  - {username}")
                print()
                
                username_to_delete = input("Enter username to delete: ").strip()
                if not username_to_delete:
                    print("Invalid username.")
                    time.sleep(2)
                    continue
                
                if username_to_delete in data:
                    del data[username_to_delete]
                    
                    with open("user_data.json", 'w') as file:
                        json.dump(data, file, indent=4)
                    
                    print(f"✅ User '{username_to_delete}' has been deleted.")
                else:
                    print(f"❌ User '{username_to_delete}' not found.")
                    
            except (FileNotFoundError, json.JSONDecodeError):
                print("📊 No user data found or file is corrupted.")
            
            time.sleep(2)

        elif dev_input.upper() == "E":
            break

        else:
            print("Invalid dev menu option.")
            time.sleep(2)


              

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_name = input("Enter your username: ").strip()

    if user_name == "admin":
        run_dev_menu()
        return
    
    # Welcome message for returning users
    try:
        with open("user_data.json", 'r') as file:
            data = json.load(file)
            if user_name in data:
                print(f"Welcome back, {user_name}! Your current highscore is {data[user_name]}")
            else:
                print(f"Welcome, {user_name}! This is your first time playing.")
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Welcome, {user_name}! This is your first time playing.")
    
    print()
    time.sleep(1.5)
        
    while True:
        game = slot_machine_game(user_name)
        game.game_loop()
        again = input("Play again? (Y/N): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    print("\033[?25h", end="")
    main()
