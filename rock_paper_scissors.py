rock = '''
        _______
       '   _____)
    ---  (______)
         (______)
         (______)
-----.___(______)
'''

paper = '''
      ________________________
                             /
                            /
      _____________________/
    '''


scissors = '''
        ____________
    ___'     _______)___
                _________)_
              _____________)
                  ______)
    -------._________)
             
  '''



import random

player_choice = int(input())
while(player_choice >2):
  print("You can choose either 1 or 2 or 3")
  player_choice = int(input())
computer_choice = random.randint(0,2)
print(computer_choice)

if player_choice==computer_choice:
  print("It's a tie!")
elif player_choice==0 and computer_choice==1:
  print("You lose")
  print(paper)
elif player_choice==0 and computer_choice==2:
  print("You win")
  print(rock)
elif player_choice==1 and computer_choice==2:
  print("You lose")
  print(scissors)
elif player_choice==1 and computer_choice==0:
  print("You win")
  print(rock)
elif player_choice==2 and computer_choice==0:
  print("You lose")
  print(scissors)
elif player_choice==2 and computer_choice==1:
  print("You win")
  print(paper)
