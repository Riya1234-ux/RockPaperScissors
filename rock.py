import random
user_choice= int(input("Type 0 for Rock,1 for paper,2 for Scissors "))
if user_choice>=3 or user_choice<0:
    print("You have entered invalid choice,you lose.")
else:
    computer_choice = random.randint(0, 2)
    print("Computer Choice: ", computer_choice)
    if user_choice==computer_choice:
        print("It's a draw.")
    elif computer_choice==0 and user_choice==2:
        print("You lose.")
    elif user_choice==0 and computer_choice==2:
        print("You win.")
    elif computer_choice>user_choice:
        print("You lose.")
    elif user_choice>computer_choice:
        print("You win.")