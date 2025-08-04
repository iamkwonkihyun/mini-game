import random

def get_user_input(comment: str, type: int | str = str):
    user_input = input(f"{comment}").strip().lower()
    return type(user_input)

def random_number(first_num: int, second_num: int, type: int | float = int):
    return type(random.randint(first_num, second_num))