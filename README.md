```markdown
# 🎮 Snake-Water-Gun Game 

A fun and simple command-line game where you play **Snake-Water-Gun** against the computer. It's a twist on the classic **Rock-Paper-Scissors**, written entirely in Python.

---

## 🧠 Game Rules

- 🐍 **Snake** drinks 💧 **Water**
- 💧 **Water** damages 🔫 **Gun**
- 🔫 **Gun** kills 🐍 **Snake**

| Player's Choice  | Computer's Choice | Result            |
|------------------|-------------------|------------------ |
| Snake            | Water             | ✅ You Win        |
| Water            | Gun               | ✅ You Win        |
| Gun              | Snake             | ✅ You Win        |
| Snake            | Gun               | ❌ You Lose       |
| Water            | Snake             | ❌ You Lose       |
| Gun              | Water             | ❌ You Lose       |
| Same             | Same              | ⚖️ It's a Draw    |

---

## ✅ Features

- Terminal-based interactive game
- Input validation (case-insensitive)
- Real-time score tracking
- Final match winner announcement
- Emoji-enhanced UI for better experience 🎉

---

## ▶️ How to Play

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/snake-water-gun.git
   cd snake-water-gun
   ```

2. Run the game:

   ```bash
   python snake_water_gun.py
   ```

3. Enter your move: `Snake`, `Water`, or `Gun`.

4. To quit anytime, type `exit`.

---

## 🖥️ Sample Output

```
🎮 Welcome to Snake-Water-Gun Game 🎮

Enter your choice (Snake, Water, Gun) or 'exit' to quit: snake
You chose Snake 🆚 Computer chose Gun
❌ You Lost this Round.

Score → You: 1 | Computer: 2
```

---

## 💡 Future Enhancements

- [ ] Add a GUI using Tkinter
- [ ] Add sound effects 🎵
- [ ] Best-of-N rounds or tournament mode
- [ ] Multiplayer (hot-seat)

---

## 📁 Project Structure

```
snake-water-gun/
├── snake_water_gun.py   # Main game file
├── README.md            # You're here!
```

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy playing! 😄 Feel free to ⭐ star the repo if you liked it!
```

---

Let me know if you'd also like:
- A matching `LICENSE` file
- GitHub repo badges (language, license, stars, etc.)
- GUI version added to the same repo

Happy coding, champ! 💻🔥
