from random import randint
computer = randint(0,2)

if computer == 0:
	computer = "rock"
if computer == 1:
	computer = "scissor"
if computer == 2:
	computer = "paper"

def main():
  run = True
  while run:
    player = input("rock, paper, or scissor? ").lower()
    if player == "rock" or player == "paper" or player == "scissor": 
      print("You choose " + str(player))
      print("Computer chooses " + str(computer))
    else:
      print("Invalid input")
      break

    if player == computer:
      print("Draw")
    if player == "rock":
      if computer == "scissor":
        print("You win!")
      if computer == "paper":
        print("You lose!")
    if player == "scissor":
      if computer == "paper":
        print("You win!")
      if computer == "rock":
        print("You lose!")
    if player == "paper":
      if computer == "rock":
        print("You win!")
      if computer == "scissor":
        print("You lose!")
    
    replay = input("Player again? Yes/No: ").lower()
    if replay != "yes":
      run = False

if __name__ == "__main__":
  main()
