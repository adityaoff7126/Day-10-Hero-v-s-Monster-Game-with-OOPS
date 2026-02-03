# 🐉 Text RPG Battle Game (Python OOP Project)

## 📌 Overview
This is a simple **Text-Based RPG Battle Game** built using **Object-Oriented Programming (OOP)** concepts in Python.  
The player fights a monster while an environment adds special battle effects.

The game continues until either the player or monster loses all HP.

---

## 🎮 Features
- Player can **Attack** or **Heal**
- Monster attacks automatically after player turn
- Environment provides **damage bonus**
- Randomized attack and heal values
- Continuous battle loop until win or loss

---

## 🧠 Concepts Used
- Classes & Objects
- Constructors (`__init__`)
- Encapsulation
- Method Interaction Between Classes
- Game Loop Logic
- Random Module
- User Input Handling

---

## 🏗️ Class Structure

### 🌍 Environment Class
Represents the battle location.

#### Attributes
- `name` → Name of environment
- `damage_bonus` → Extra damage added to player attack

#### Methods
- `show()` → Displays environment details

---

### 🧙 Player Class
Represents the player character.

#### Attributes
- `name` → Player name
- `hp` → Player health (starts at 100)

#### Methods
- `attack(env)` → Attacks monster with environment bonus
- `heal()` → Restores player health

---

### 🐲 Monster Class
Represents the enemy.

#### Attributes
- `name` → Monster name
- `hp` → Monster health (starts at 80)

#### Methods
- `attack()` → Deals random damage to player

---

### 🎯 Game Class
Controls overall gameplay.

#### Attributes
- `player`
- `monster`
- `environment`

#### Methods
- `start()` → Runs the game loop

---

## ⚔️ Gameplay Flow
1. Game starts
2. Environment details are shown
3. Player chooses action:
   - Attack
   - Heal
4. Monster attacks after player turn
5. Game ends when:
   - Player HP = 0 → Loss
   - Monster HP = 0 → Win

---

## ▶️ How To Run

### Step 1
Make sure Python is installed.

### Step 2
Save file as:
```
game.py
```

### Step 3
Run in terminal:
```
python game.py
```

---

## 📦 Example Output
```
GAME STARTED
Environment: Volcano | Damage Bonus: 5

--- STATUS ---
Hero HP: 100
Dragon HP: 80

1. Attack
2. Heal
Choose:
```

---

## 🚀 Future Improvements
- Add multiple monsters
- Add player leveling system
- Add inventory and weapons
- Add difficulty levels
- Add graphical interface (Tkinter / Pygame)
- Add save & load game feature
- Add multiplayer mode

---

## 🛠️ Technologies Used
- Python
- Random Module
- OOP Design

---

## 📚 Learning Outcome
By completing this project you will understand:
- Real world OOP implementation
- Game loop design
- Class interaction
- State management
- Randomized gameplay mechanics

---

## 👨‍💻 Author
Python OOP Learning Project
