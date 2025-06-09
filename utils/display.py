import os
import time
from game.config import GameConfig
from utils.data_manager import DataManager

class DisplayManager:
    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def hide_cursor():
        """Hide the terminal cursor."""
        print(GameConfig.CURSOR_HIDE, end="")
    
    @staticmethod
    def show_cursor():
        """Show the terminal cursor."""
        print(GameConfig.CURSOR_SHOW, end="")
    
    @staticmethod
    def display_leaderboard():
        """Display the game leaderboard."""
        leaderboard = DataManager.get_leaderboard()
        
        if not leaderboard:
            print("📊 Leaderboard is empty!")
            return
        
        print("🏆 === LEADERBOARD === 🏆")
        print()
        
        medals = ["🥇", "🥈", "🥉"]
        for i, (username, score) in enumerate(leaderboard, 1):
            if i <= 3:
                ordinal = ["1st", "2nd", "3rd"][i-1]
                print(f"{medals[i-1]} {ordinal}: {username} - {score} points")
            else:
                print(f"   {i}th: {username} - {score} points")
        print()
    
    @staticmethod
    def display_welcome_message(username):
        """Display welcome message for users."""
        highscore = DataManager.get_user_highscore(username)
        
        if highscore > 0:
            print(f"Welcome back, {username}! Your current highscore is {highscore}")
        else:
            print(f"Welcome, {username}! This is your first time playing.")
        
        print()
        time.sleep(1.5)
