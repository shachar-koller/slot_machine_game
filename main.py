from game.slot_machine import SlotMachineGame
from utils.display import DisplayManager
from utils.dev_tools import DevTools

def main():
    DisplayManager.clear_screen()
    user_name = input("Enter your username\n> ").strip()

    if user_name == "admin":
        DevTools.run_dev_menu()
        return

    DisplayManager.display_welcome_message(user_name)

    while True:
        game = SlotMachineGame(user_name)
        game.game_loop()
        again = input("Play again? (Y/N)\n> ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    print("\033[?25h", end="")  # Ensure cursor is visible on exit
    main()
    print("\033[?25h", end="")  # Ensure cursor is visible on exit
