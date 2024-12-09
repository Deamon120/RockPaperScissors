

def computer_always_won(user_input):
    if user_input == "paper":
        print("Sorry, but the computer chose scissors")
    elif user_input == "scissors":
        print("Sorry, but the computer chose rock")
    elif user_input == "rock":
        print("Sorry, but the computer chose paper")

user_input = input()
computer_always_won(user_input)
