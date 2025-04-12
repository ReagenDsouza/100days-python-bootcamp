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
import random
print("WELCOME TO THE ROCK,PAPER,SCISSORS GAME!!")
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))
game_images=[rock,paper,scissors]

random_num=random.randint(0,2)
random_name=game_images[random_num]

if choice >= 0 and choice <= 2:
    print(game_images[choice])
    print(f"Computer chose: {random_name}")
    if random_name == game_images[choice]:
        print("Its a draw!!")
    elif random_name == rock and game_images[choice] == paper:
        print("You win")
    elif random_name == rock and game_images[choice] == scissors:
        print("You lost")
    elif random_name == paper and game_images[choice] == rock:
        print("You loose")
    elif random_name == paper and game_images[choice] == scissors:
        print("You win")
    elif random_name == scissors and game_images[choice] == paper:
        print("You lost")
    elif random_name == scissors and game_images[choice] == rock:
        print("You win")
else:
    print("Invalid choice")








