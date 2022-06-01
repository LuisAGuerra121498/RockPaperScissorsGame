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

#Write your code below this line 👇

player1 = input("Pick 1:rock,2:paper,3:scissors to play: ")
computer = random.randint(1, 3)

if player1 == 1 and computer == 1:
  print(f'You played rock {rock} \t\t\t\t Computer played rock {rock}')
  print("It was a draw try again")
elif player1 == 1 and computer == 2:
  print(f'You played rock {rock} \t\t\t\t Computer played rock {paper}')
  print("You lose")
elif player1 == 1 and computer == 3:
  print(f'You played rock {rock} \t\t\t\t Computer played rock {scissors}')
  print("You win!!!")
elif player1 == 2 and computer == 1:
  print(f'You played rock {paper} \t\t\t\t Computer played rock {rock}')
  print("You win!!!")
elif player1 == 2 and computer == 2:
  print(f'You played rock {paper} \t\t\t\t Computer played rock {paper}')
  print("It was a draw try again")
elif player1 == 2 and computer == 3:
  print(f'You played rock {paper} \t\t\t\t Computer played rock {scissors}')
  print("You lose")
elif player1 == 3 and computer == 1:
  print(f'You played rock {scissors} \t\t\t\t Computer played rock {rock}')
  print("You lose")
elif player1 == 3 and computer == 2:
  print(f'You played rock {scissors} \t\t\t\t Computer played rock {paper}')
  print("You win!!!")
elif player1 == 3 and computer == 3:
  print(f'You played rock {scissors} \t\t\t\t Computer played rock {scissors}')
  print("It was a draw try again")
else:
  print("Please choose what is being provided. Please try again")