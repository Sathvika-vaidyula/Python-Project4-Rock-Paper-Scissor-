import random

# ASCII Art for choices (fixed warnings using raw strings)
paper = r''' 
     _ __   __ _ _ __   ___ _ __  
    | '_ \ / _` | '_ \ / _ \ '__| 
    | |_) | (_| | |_) |  __/ |    
    | .__/ \__,_| .__/ \___|_|    
    | |         | |               
    |_|         |_|  
'''

scissor = r''' 
          _                    
         (_)                   
  ___  ___ _ ___ ___  ___  _ __ 
 / __|/ __| / __/ __|/ _ \| '__|
 \__ \ (__| \__ \__ \ (_) | |   
 |___/\___|_|___/___/\___/|_|  
'''

rock = r''' 
      _    
     | |   
 _ __| | __
| '__| |/ /
| |  |   < 
|_|  |_|\_\
'''

# Choices dictionary
choices = {0: rock, 1: paper, 2: scissor}

# User input
user_choice = input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n")

# Validate input
if not user_choice.isdigit() or int(user_choice) not in [0, 1, 2]:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    user_choice = int(user_choice)
    computer_choice = random.randint(0, 2)

    # Display choices
    print(f"\nYou chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[computer_choice]}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a Draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You Win! 🎉")
    else:
        print("You Lose! 😢")
