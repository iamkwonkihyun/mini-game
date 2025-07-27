import random

RPS = {
        1: "rock",
        2: "paper",
        3: "scissors"
    }

exit_code = 1

while exit_code:
    user_input = input("user: ").strip().lower()
    
    if user_input not in ["rock", "paper", "scissors", "exit", "e"]:
        print("plz 올바른 input")
    
    random_int = int(random.randint(1, 3))
    
    if user_input in ["exit", "e"]:
        exit_code = 0
    
    random_rps = RPS[random_int]
    
    if user_input == random_rps:
        print("draw")
    
    match user_input, random_rps:
        case "rock", "paper":
            print("you lose")
        case "rock", "scissors":
            print("you win")
        case "paper", "rock":
            print("you win")
        case "paper", "scissors":
            print("you lose")
        case "scissors", "rock":
            print("you lose")
        case "scissors", "paper":
            print("you win")
        case _:
            pass