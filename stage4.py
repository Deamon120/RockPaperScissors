import random

name = input("Enter your name: ")
print(f"Hello, {name}")
rating = 0
file = open('rating.txt', 'r')
for line in file:
    line_split = line.split()
    name_line = line_split[0]
    rating_line = int(line_split[1])
    if name == name_line:
        name = name_line
        rating = rating_line

rock_paper_scissors = ["rock", "paper", "scissors"]
user_input = ""
while user_input != "!exit":
    user_input = input()
    if (user_input != "rock" and user_input != "scissors" and
            user_input != "paper" and user_input != "!exit" and user_input != "!rating"):
        print("Invalid input")
        continue
    elif user_input == "!rating":
        print(f"Your rating: {rating}")
    random_int = random.randint(0,2)
    computer_random = rock_paper_scissors[random_int]

    # if statement for user input == "rock"
    if user_input == "rock" and  computer_random == "rock":
        print(f"There is a draw ({user_input})")
        rating += 50
    elif user_input == "rock" and computer_random == "scissors":
        print(f"Well done. The computer chose <{computer_random}> and failed")
        rating += 100
    elif user_input == "rock" and computer_random == "paper":
        print(f"Sorry, but the computer chose <{computer_random}>")

    # if statement for user input == "paper"
    if user_input == "paper" and  computer_random == "paper":
        print(f"There is a draw ({user_input})")
        rating += 50
    elif user_input == "paper" and computer_random == "rock":
        print(f"Well done. The computer chose <{computer_random}> and failed")
        rating += 100
    elif user_input == "paper" and computer_random == "scissors":
        print(f"Sorry, but the computer chose <{computer_random}>")


# if statement for user input == "scissors"
    if user_input == "scissors" and  computer_random == "scissors":
        print(f"There is a draw ({user_input})")
        rating += 50
    elif user_input == "scissors" and computer_random == "paper":
        print(f"Well done. The computer chose <{computer_random}> and failed")
        rating += 100
    elif user_input == "scissors" and computer_random == "rock":
        print(f"Sorry, but the computer chose <{computer_random}>")


file.close()
print("Bye!")