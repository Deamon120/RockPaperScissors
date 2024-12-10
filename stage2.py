import random

user_input = input()
rock_paper_scissors = ["rock", "paper", "scissors"]
random_int = random.randint(0,2)
computer_random = rock_paper_scissors[random_int]

# if condition for user input == "rock"
if user_input == "rock" and  computer_random == "rock":
    print(f"There is a draw ({user_input})")
elif user_input == "rock" and computer_random == "scissors":
    print(f"Well done. The computer chose <{computer_random}> and failed")
elif user_input == "rock" and computer_random == "paper":
    print(f"Sorry, but the computer chose <{computer_random}>")

# if condition for user input == "paper"
if user_input == "paper" and  computer_random == "paper":
    print(f"There is a draw ({user_input})")
elif user_input == "paper" and computer_random == "rock":
    print(f"Well done. The computer chose <{computer_random}> and failed")
elif user_input == "paper" and computer_random == "scissors":
    print(f"Sorry, but the computer chose <{computer_random}>")


# if condition for user input == "scissors"
if user_input == "scissors" and  computer_random == "scissors":
    print(f"There is a draw ({user_input})")
elif user_input == "scissors" and computer_random == "paper":
    print(f"Well done. The computer chose <{computer_random}> and failed")
elif user_input == "scissors" and computer_random == "rock":
    print(f"Sorry, but the computer chose <{computer_random}>")