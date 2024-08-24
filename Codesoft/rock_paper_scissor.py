import random 

print("\tWELCOME TO THE GAME ROCK, PAPER, SCISSOR")
game=["rock", "paper", "scissors"]
#players names
player_name=input("Enter your name: ")
#displaying players names
print("Player1: ",player_name)
print("Player2: computer")

#players choosing their option
print("Rock, Paper or scissor")

player_option=input("Enter your option : ")

computer_option=random.choice(game)
print("Player1 choosed:",player_option)

print("Computer choosed:",computer_option)
if( player_option in game):
#calculating results                                                                                                                                  
    if (player_option==computer_option):
         print("It is a tie") 
    elif player_option=="rock" and computer_option=="paper":

         print("Computer wins")


    elif player_option=="rock" and computer_option=="scissors":
         print(player_name, "wins")


    elif player_option=="paper" and computer_option=="rock":


        print(player_name, "wins")


    elif player_option=="paper" and computer_option=="scissors":

        print("Computer wins")

    elif player_option=="scissors" and computer_option=="paper":

         print(player_name, "wins") 
    elif player_option== "scissors" and computer_option=="rock":

         print("Computer wins")

    else:

        print("Selected option doesn't exist")

else:
    print("Closing the game")
