# 🎮 Rock Paper Scissors

A simple command-line Rock Paper Scissors game where you play against the computer.

## 📋 About

This project was built on Day 4 of my 100 Days of Code journey. It's a classic
Rock Paper Scissors game with ASCII art for each choice.

## 🚀 How to Play

1. Run the script
2. Enter your choice:
   - `0` for Rock 🪨
   - `1` for Paper 📄
   - `2` for Scissors ✂️
3. The computer randomly picks its choice
4. The winner is determined and displayed!

## 🛠️ How It Works

- User input is validated to ensure it's between 0 and 2
- The computer's choice is generated randomly using Python's `random` module
- Game logic compares both choices to determine a win, loss, or draw

## 📚 What I Learned

- Working with lists to store and index related data (the ASCII art)
- Using `random.randint()` to generate random choices
- Writing conditional logic (`if`/`elif`/`else`) to handle multiple game outcomes
- Basic input validation

## ⚠️ Known Limitations

- Entering a non-numeric value (e.g. "rock") will currently crash the program,
  since `int()` can't convert text to a number. This will be fixed once I learn
  error handling (`try`/`except`)!

## 🔧 Run It Yourself

\`\`\`bash
python task.py
\`\`\`

---
*Part of my [#100DaysOfCode](https://www.100daysofcode.com/) challenge*
