import random
computer_choice = random.randint(0,2)
print(" 0 = Rock\n","1 = Paper\n","2 = Scissors\n")
user_choice = int(input("Enter your choice:- "))
print("Computer has chosen:-",computer_choice)
if computer_choice == user_choice:
    print("Draw")
elif computer_choice == 0 and user_choice == 2:
    print("Computer wins!!")
elif computer_choice == 2 and user_choice == 0:
    print("You win!!")
elif user_choice < computer_choice:
    print("Computer wins!!")
elif user_choice > computer_choice:
    print("You win!!")

