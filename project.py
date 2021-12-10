import random

# print("Tell us you're name: ")
player_name= input("Tell us you're name: ")

computer_score=0
player_score=0

print(f"Welcome {player_name} to Rock, Paper, Scissors")

while True:
    player= input("Choose: Rock, Paper or Scissors:")
    player=player.capitalize()
    
    if player == "End":
         print("Final score:")
         print(f"Computer:{computer_score}")
         print(f"{player_name}:{player_score}")
         break
    
    if player != "Rock" and player != "Paper" and player != "Scissors":
        print("Select a correct answer")
        continue
        
    choices = ["Rock", "Paper", "Scissors"]
    computer=random.choice(choices)
    print(f"You choose:{player}")
    print(f"Computer choose: {computer}")

    
    if player==computer:
        print("Tie!")
        
        
    elif player=="Rock":
        if computer=="Paper":
            print("You Lose!" ,computer, "covers", player)
            computer_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
            
            
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose...", computer, "smashes", player)
            computer_score+=1
        else:
            print("You win!",player,"cut",computer)
            player_score+=1
            
            
    else:
        player=="Paper"
        if computer=="Scissors":
            print("You lose!", computer, "cut", player)
            computer_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+1

