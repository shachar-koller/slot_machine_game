class GameConfig:
    MAX_LIVES = 3
    GUESS_MINIMUM = 1
    GUESS_MAXIMUM = 3
    DATA_FILE = "user_data.json"
    ANIMATION_FRAMES = 100
    ANIMATION_SPEED = 0.01
    
    # Display settings
    CURSOR_HIDE = "\033[?25l"
    CURSOR_SHOW = "\033[?25h"
    
    # Emojis
    CORRECT_EMOJI = "✅"
    WRONG_EMOJI = "❌"
    TROPHY_EMOJI = "🏆"
    CELEBRATION_EMOJI = "🎉"
