import random

print("Let's Play Rock, Paper, Scissors!")
print("---------------------------------")

yesNo = "Y";

while yesNo == "Y" or "y":
  
  # Initialization
  yourChoice = input("Type (rock, paper or scissors): ")
  possibleOutcomes = ["rock", "paper", "scissors"]
  
  # Set computer choice to be random
  # This ensures a fair game
  computerChoice = random.choice(possibleOutcomes)
  
  # Print both outcomes, display the winner!
  print(f"\nYou chose {yourChoice}, computer chose {computerChoice}.")
  
  # Logic behind Rock, Paper, Scissors
  if yourChoice == computerChoice:
      print(f"Both played {computerChoice}. What a tie!")
  elif yourChoice == "rock":
      if computerChoice == "scissors":
          print("Rock smashes Scissors! What a win!")
      else:
          print("Paper covers Rock! You lose, try again!")
  elif yourChoice == "paper":
      if computerChoice == "rock":
          print("Paper covers Rock! You nailed it!")
      else:
          print("Scissors cuts paper! You lose, try again!")
  elif yourChoice == "scissors":
      if computerChoice == "paper":
          print("Scissors cuts Paper! Easy win!")
      else:
          print("Rock smashes scissors, try again!")
  
  yesNo = input("\nDo you wish to continue? Y/N: ")
  print("\n")
  
  if yesNo == "N" or yesNo == "n":
    break
