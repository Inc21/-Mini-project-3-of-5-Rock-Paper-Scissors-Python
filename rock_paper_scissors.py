import random

user_wins = 0
computer_wins = 0
draw_game = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    # print(user_input)
    
    if user_input not in options:
        continue
    
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1 
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        
    elif user_input == "rock" and computer_pick == "rock":
        print("It's a draw!")
        draw_game += 1  
        
    elif user_input == "paper" and computer_pick == "paper":
        print("It's a draw") 
        draw_game += 1  
        
    elif user_input == "scissors" and computer_pick == "scissors":
        print("It's a draw")   
        draw_game += 1   
             
    else:
        print("You lost!")
        computer_wins += 1    
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.") 
print("Draw", draw_game, "times.")   
print("Goodbye!")