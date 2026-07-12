import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
#if user_input in [0, 1, 2]:
if 0 <= user_input <= 2:
    print(rps[user_input])
    computer_choice = random.randint(0,2)
    print(f"Computer chose:\n{rps[computer_choice]}")
    if computer_choice == user_input:
        print("Its a draw!")
    elif computer_choice == 2 and user_input == 0:
        print("You win!")
    elif computer_choice == 0 and user_input == 1:
        print("You win!")
    elif computer_choice == 1 and user_input == 2:
        print("You win!")
    else:
        print("You lose!")
else:
    print("You chose an invalid option! You lose! ")
