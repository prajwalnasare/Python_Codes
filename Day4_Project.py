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
---'    ____)____
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
game_images = [rock,paper,scissors]
user_choice = int(input("What do you choose!! Type 0 for rock, 1 for paper, 2 scissors\n"))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])


# rock beats scissors( 0 beats 2), scissors beats paper(2 beats 1), paper beats rock (1 beats 0)
computer_choice = random.randint(0,1)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("Invalid Input!! You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!!")
elif computer_choice == 2 and user_choice == 0:
    print("You lose!!")
elif computer_choice > user_choice:
    print("You lose!!!")
elif user_choice > computer_choice:
    print("You win!!")
elif computer_choice == user_choice:
    print("its a draw!!")
2

