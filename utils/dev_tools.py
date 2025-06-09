import time
import json
import random
from utils.data_manager import DataManager

class DevTools:
    @staticmethod
    def run_dev_menu():
        """Run the developer menu."""
        while True:
            print("🛠 Dev mode activated. What would you like to do?")
            print("Type A to erase all saved data")
            print("Type B to run a save data test")
            print("Type C to manually enter user data")
            print("Type D to view all stored data")
            print("Type F to delete a specific user")
            print("Type E to exit dev mode")
            
            dev_input = input(">> ").strip().upper()
            
            if dev_input == "A":
                DevTools._delete_all_data()
            elif dev_input == "B":
                DevTools._run_save_test()
            elif dev_input == "C":
                DevTools._manual_data_entry()
            elif dev_input == "D":
                DevTools._view_all_data()
            elif dev_input == "F":
                DevTools._delete_specific_user()
            elif dev_input == "E":
                break
            else:
                print("Invalid dev menu option.")
                time.sleep(2)
    
    @staticmethod
    def _delete_all_data():
        """Delete all saved data."""
        if DataManager.delete_all_data():
            print("All saved data deleted.")
        else:
            print("No saved data to delete.")
        time.sleep(2)
    
    @staticmethod
    def _run_save_test():
        """Run a save/load test."""
        test_user = "test_user"
        test_score = random.randint(5, 15)
        
        # Save test data
        DataManager.update_user_highscore(test_user, test_score)
        
        # Load and verify
        loaded_score = DataManager.get_user_highscore(test_user)
        
        if loaded_score == test_score:
            print(f"✅ Save/load test passed. Score {test_score} was saved and loaded correctly.")
        else:
            print(f"❌ Test failed. Saved {test_score}, but loaded {loaded_score}.")
        
        # Clean up
        DataManager.delete_user(test_user)
        print("Test data cleaned up.")
        time.sleep(2)
    
    @staticmethod
    def _manual_data_entry():
        """Manually enter user data."""
        username = input("Enter username: ").strip()
        if not username:
            print("Invalid username.")
            time.sleep(2)
            return
        
        try:
            score = int(input("Enter score: ").strip())
            if score < 0:
                print("Score must be non-negative.")
                time.sleep(2)
                return
        except ValueError:
            print("Invalid score. Must be a number.")
            time.sleep(2)
            return
        
        data = DataManager.load_user_data()
        data[username] = score
        DataManager.save_user_data(data)
        
        print(f"✅ User '{username}' with score {score} has been added/updated.")
        time.sleep(2)
    
    @staticmethod
    def _view_all_data():
        """View all stored data."""
        data = DataManager.load_user_data()
        
        if not data:
            print("📊 No stored data found.")
        else:
            print("📊 All stored user data:")
            print(json.dumps(data, indent=4))
        
        input("\nPress Enter to continue...")
    
    @staticmethod
    def _delete_specific_user():
        """Delete a specific user."""
        data = DataManager.load_user_data()
        
        if not data:
            print("📊 No user data found to delete.")
            time.sleep(2)
            return
        
        print("📊 Current users:")
        for username in data.keys():
            print(f"  - {username}")
        print()
        
        username_to_delete = input("Enter username to delete: ").strip()
        if not username_to_delete:
            print("Invalid username.")
            time.sleep(2)
            return
        
        if DataManager.delete_user(username_to_delete):
            print(f"✅ User '{username_to_delete}' has been deleted.")
        else:
            print(f"❌ User '{username_to_delete}' not found.")
        
        time.sleep(2)
