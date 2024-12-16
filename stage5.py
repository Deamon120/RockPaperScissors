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

choose_option = input().split(",")
if len(choose_option) == 1:
    choose_option = ["rock", "paper", "scissors"]
print("Okay, let's start")
user_input = ""
while user_input != "!exit":
    user_input = input()
    if (user_input not in choose_option and user_input != "!exit"
            and user_input != "!rating"):
        print("Invalid input")
        continue
    elif user_input == "!rating":
        print(f"Your rating: {rating}")
        continue
    elif user_input == "!exit":
        break

    user_index = choose_option.index(user_input)
    after_index_list = choose_option[user_index+1:]
    before_index_list = choose_option[:user_index]
    sum_list = after_index_list + before_index_list
    if len(sum_list) % 2 == 0:
        lose_option = len(sum_list) // 2
        win_option = len(sum_list) // 2
    else:
        lose_option = len(sum_list) // 2 + 1
        win_option = len(sum_list) // 2

    random_int = random.randint(0, len(choose_option) - 1)
    computer_random = choose_option[random_int]

    # if statement for user input == "rock"
    if computer_random == user_input:
        print(f"There is a draw ({user_input})")
        rating += 50
    elif computer_random in sum_list[win_option:]:
        print(f"Well done. The computer chose <{computer_random}> and failed")
        rating += 100
    elif computer_random in sum_list[:lose_option]:
        print(f"Sorry, but the computer chose <{computer_random}>")

file.close()
print("Bye!")
