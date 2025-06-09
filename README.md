# 🎰 Slot Machine Game

A terminal-based guessing game with user persistence and leaderboards.

## 🎮 Quick Demo
> Click the box below to watch a video demonstration:
>
>[![Video Demonstration](https://img.youtube.com/vi/KKmS28tzaKY/0.jpg)](https://www.youtube.com/watch?v=KKmS28tzaKY)

## ✨ Features
- Multi-user system with JSON data persistence
- Global leaderboard system
- Developer admin panel for data management
- Clean modular architecture (split into 6+ files)
- Terminal animations and visual feedback

## ⚙️ Technical Highlights
- **Separation of Concerns**: Game logic, data management, and UI split into different files
- **Error Handling**: Robust file I/O with graceful fallbacks
- **Configuration Management**: Centralized settings system
- **Developer Tools**: Built-in admin interface for testing

## 🚀 Quick Start
In your terminal, type the following, one by one:
```bash
git clone [repo-url]
cd slot_machine_game
python3 main.py
```

## 📁 Project Structure
```
slot_machine_game/
├── main.py              # Entry point
├── game/
│   ├── slot_machine.py  # Core game logic
│   └── config.py        # Game configuration
└── utils/
    ├── data_manager.py  # File I/O operations
    ├── display.py       # UI management
    └── dev_tools.py     # Developer tools
```