import json
import os
from game.config import GameConfig

class DataManager:
    @staticmethod
    def load_user_data():
        """Load all user data from JSON file."""
        try:
            with open(GameConfig.DATA_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    @staticmethod
    def save_user_data(data):
        """Save user data to JSON file."""
        with open(GameConfig.DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    
    @staticmethod
    def get_user_highscore(username):
        """Get a specific user's highscore."""
        data = DataManager.load_user_data()
        return int(data.get(username, 0))
    
    @staticmethod
    def update_user_highscore(username, score):
        """Update user's highscore if the new score is higher."""
        data = DataManager.load_user_data()
        
        if username not in data or score > data[username]:
            data[username] = score
            DataManager.save_user_data(data)
            return True
        return False
    
    @staticmethod
    def delete_user(username):
        """Delete a user from the data."""
        data = DataManager.load_user_data()
        if username in data:
            del data[username]
            DataManager.save_user_data(data)
            return True
        return False
    
    @staticmethod
    def delete_all_data():
        """Delete the entire data file."""
        if os.path.exists(GameConfig.DATA_FILE):
            os.remove(GameConfig.DATA_FILE)
            return True
        return False
    
    @staticmethod
    def get_leaderboard(limit=10):
        """Get sorted leaderboard data."""
        data = DataManager.load_user_data()
        return sorted(data.items(), key=lambda x: int(x[1]), reverse=True)[:limit]
