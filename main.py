import random
print('welcome to Rock, Paper and Scissors game. Can you win me?')

while True:
  choices = ["rock", "paper", "scissors"]
  CPU = random.choice(choices)
  player = None
  while player not in choices:
    print("please enter a valid option")
    player = input ("rock, paper, or scisssors?:").lower()
    

  if player == CPU:
      print("CPU:", CPU)
      print("player:", player)
      print("repeat game")
      player = input ("rock, paper, or scissors?:").lower()
  elif player == "rock": 
    if CPU == "paper":
        print("CPU:", CPU)
        print("player:", player)
        print("you lose!")
    if CPU == "scissors":
        print("CPU:", CPU)
        print("player:", player)
        print("you Win!")
  elif player == "scissors": 
    if CPU == "rock":
        print("CPU:", CPU)
        print("player:", player)
        print("you lose!")
    if CPU == "paper":
        print("CPU:", CPU)
        print("player:", player)
        print("you Win!") 
  elif player == "paper": 
    if CPU == "scissors":
        print("CPU:", CPU)
        print("player:", player)
        print("you lose!")
    if CPU == "rock":
        print("CPU:", CPU)
        print("player:", player)
        print("you Win!")

  play_again = input("play again? (yes/no): ")

  if play_again != "yes":
    break

print("Thank you for playing with me")
