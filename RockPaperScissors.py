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
playagain = ''

while playagain == 'Yes' or "yes":

  player1 = input("Pick 1:rock,2:paper,3:scissors to play: ")
  computer = random.randint(1, 3)

  if player1 == 1 and computer == 1:
    print(f'You played rock {rock} \t\t\t\t Computer played rock {rock}')
    print("It was a draw try again")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 1 and computer == 2:
    print(f'You played rock {rock} \t\t\t\t Computer played paper {paper}')
    print("You lose")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 1 and computer == 3:
    print(f'You played rock {rock} \t\t\t\t Computer played scissors {scissors}')
    print("You win!!!")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 2 and computer == 1:
    print(f'You played paper {paper} \t\t\t\t Computer played rock {rock}')
    print("You win!!!")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 2 and computer == 2:
    print(f'You played paper {paper} \t\t\t\t Computer played paper {paper}')
    print("It was a draw try again")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 2 and computer == 3:
    print(f'You played paper {paper} \t\t\t\t Computer played scissors {scissors}')
    print("You lose")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 3 and computer == 1:
    print(f'You played scissors {scissors} \t\t\t\t Computer played rock {rock}')
    print("You lose")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 3 and computer == 2:
    print(f'You played scissors {scissors} \t\t\t\t Computer played paper {paper}')
    print("You win!!!")
    playagain = input("Want to play again?(types yes if you do):")
  elif player1 == 3 and computer == 3:
    print(f'You played scissors {scissors} \t\t\t\t Computer played scissors {scissors}')
    print("It was a draw try again")
    playagain = input("Want to play again?(types yes if you do):")
  else:
    print("Please choose what is being provided. Please try again")
    playagain = input("Want to play again?(types yes if you do):")

print("The games as ended the game will close")
time.sleep(10)
exit()