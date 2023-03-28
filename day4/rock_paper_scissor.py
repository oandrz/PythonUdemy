import random


def convert_number_rps(selection):
    if selection == 0:
        print(rock)
    elif selection == 1:
        print(paper)
    elif selection == 2:
        print(scissors)


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

# Write your code below this line 👇
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
convert_number_rps(user_selection)

cpu_selection = random.randint(0, 2)
convert_number_rps(cpu_selection)

if user_selection == 2 and cpu_selection == 0:
    print("You lose")
elif user_selection == 0 and cpu_selection == 2:
    print("You win")
elif user_selection > cpu_selection:
    print("You win")
elif user_selection < cpu_selection:
    print("You lose")
else:
    print("Draw")
