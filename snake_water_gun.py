import random

'''
1 for Snake 
-1 for Water 
0 for Gun
'''

your_dict = {"Snake": 1, "Water": -1, "Gun": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

your_score = 0
computer_score = 0

print("🎮 Welcome to Snake-Water-Gun Game 🎮")

while True:
    computer = random.choice([-1, 0, 1])
    your_input = input("\nEnter your choice (Snake, Water, Gun) or 'exit' to quit: ").strip().capitalize()

    if your_input == 'Exit':
        print("\n🏁 Game Over!")
        print(f"Your Score: {your_score} | Computer Score: {computer_score}")
        if your_score > computer_score:
            print("🎉 Final Result: You Win the Match!")
        elif your_score < computer_score:
            print("😞 Final Result: You Lost the Match.")
        else:
            print("🤝 Final Result: It's a Draw.")
        break

    if your_input not in your_dict:
        print("❌ Invalid input! Please enter Snake, Water, or Gun.")
        continue

    you = your_dict[your_input]

    print(f"You chose {reverse_dict[you]} 🆚 Computer chose {reverse_dict[computer]}")

    if you == computer:
        print("⚖️ It's a Draw!")
    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print("✅ You Won this Round!")
        your_score += 1
    else:
        print("❌ You Lost this Round.")
        computer_score += 1
