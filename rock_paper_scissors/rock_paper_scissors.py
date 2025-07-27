import random

RANDOM_RPS = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

KOR_RPS = {
    "바위": "rock",
    "보": "paper",
    "가위": "scissors"
}

while True:
    user_input = input("user: ").strip().lower()
    
    if user_input in ["exit", "e"]:
        break
    
    if user_input not in ["rock", "paper", "scissors", "exit", "e", "가위", "바위", "보"]:
        print("올바른 input plz")
        continue
    
    random_int = int(random.randint(1, 3))
    
    random_rps = RANDOM_RPS[random_int]
    
    if user_input in ["가위", "바위", "보"]:
        user_rps = KOR_RPS[user_input]
    else:
        user_rps = user_input
    
    if user_rps == random_rps:
        print("draw")
        continue
    
    match user_rps, random_rps:
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