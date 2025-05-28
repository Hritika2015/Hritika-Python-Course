import random
while True:
    user_action = input("Lets Play rock,scissors paper, shoot! Will you pick rock scissors or paper?:")
    possible_actions = ["Rock!","Paper!","Scissors!"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose{user_action}, Your AI Oppment Chose {computer_action}")
    #1
    if user_action == computer_action:
        print(f"Both players has selected {user_action}. You think same as AI... WELL! its a tiebreaker!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper Covers Rock! You WIN!")#2
    elif user_action == "paper":
        if computer_action == "Scissors":
            if computer_action ==