import time
import random
from game.config import GameConfig
from utils.data_manager import DataManager
from utils.display import DisplayManager

class SlotMachineGame:
    def __init__(self, user_name):
        self.user_name = user_name
        self.high_score = DataManager.get_user_highscore(user_name)
        self.current_score = 0
        self.lives = GameConfig.MAX_LIVES

    def get_user_input(self):
        """Get and validate user input."""
        try:
            guess = int(input(f"Choose a number between {GameConfig.GUESS_MINIMUM} and {GameConfig.GUESS_MAXIMUM}: "))
            if GameConfig.GUESS_MINIMUM <= guess <= GameConfig.GUESS_MAXIMUM:
                return guess
            raise ValueError
        except ValueError:
            print("Invalid input.")
            time.sleep(1.5)
            return None

    def play_round(self):
        """Play a single round of the game."""
        DisplayManager.clear_screen()
        guess = self.get_user_input()
        if guess is None:
            return

        # Animation section
        DisplayManager.hide_cursor()
        for i in range(GameConfig.ANIMATION_FRAMES):
            DisplayManager.clear_screen()
            print("Choosing number...")
            print(random.randint(GameConfig.GUESS_MINIMUM, GameConfig.GUESS_MAXIMUM))
            print("\nYour guess was:", guess)
            time.sleep(GameConfig.ANIMATION_SPEED)

        DisplayManager.clear_screen()

        result = random.randint(GameConfig.GUESS_MINIMUM, GameConfig.GUESS_MAXIMUM)
        print("Choosing number...")
        print(result)
        print("\nYour guess was:", guess)
        time.sleep(0.5)

        if guess == result:
            print(f"{GameConfig.CORRECT_EMOJI} Correct!")
            self.current_score += 1
        else:
            print(f"\n{GameConfig.WRONG_EMOJI} Wrong!")
            self.lives -= 1
            print(f"Subtracting one life. Lives left: {self.lives}")
        
        time.sleep(3)
        DisplayManager.show_cursor()

    def game_loop(self):
        """Main game loop."""
        while self.lives > 0:
            self.play_round()

        DisplayManager.clear_screen()
        print("Game Over!")
        print()

        if self.current_score > self.high_score:
            print(f"{GameConfig.CELEBRATION_EMOJI} New highscore: {self.current_score}")
            DataManager.update_user_highscore(self.user_name, self.current_score)
        else:
            print(f"Your score: {self.current_score}")
            print(f"Your highscore: {self.high_score}")

        print()
        print("Press 'S' to show leaderboard or any other key to continue...")
        choice = input(">> ").strip().lower()
        if choice == 's':
            DisplayManager.clear_screen()
            DisplayManager.display_leaderboard()
            input("\nPress Enter to continue...")
            DisplayManager.clear_screen()
