import random

KOR_TO_ENG_ODD_OR_EVEN = {
    "홀": "odd",
    "짝": "even"
}

user_score = 0

while True:
    user_input = input("user: ").strip().lower()

    if user_input not in ["홀", "짝", "odd", "even"]:
        print("올바른 input plz")
        continue

    if user_input == "홀":
        user_input = KOR_TO_ENG_ODD_OR_EVEN[user_input]
    elif user_input == "짝":
        user_input = KOR_TO_ENG_ODD_OR_EVEN[user_input]
    
    random_num = int(random.randint(1, 10))
    
    match user_input:
        case "odd":
            if random_num % 2 == 1:
                print(f"you win")
                user_score += 1
                continue
            else:
                print(f"you lose, random number is {random_num}\nyour score: {user_score}")
                break
        case "even":
            if random_num % 2 == 0:
                print(f"you win")
                user_score += 1
                continue
            else:
                print(f"you lose, random number is {random_num}\nyour score: {user_score}")
                break