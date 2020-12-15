

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
# var ranking system for game  
scissors > rock  
rock > paper 
paper > scissors 
# message to player
print(f" welcome to my game{rock}rock {paper}paper {scissors}scissors  \n \nPRESS:\n1 for rock\n2 for paper\n3 for scissors")
# player input choice
choice = input("What do you chose:")
# make random gen for out come
game_1 = (scissors, rock, paper)
 = random.gitrandbit(game_1)


if choice == True:


  print("you win")