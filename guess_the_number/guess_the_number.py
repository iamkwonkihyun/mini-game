import random

is_right = False
try_cnt = 0
hint_cnt = 0

MODES = {
    1: {"digits": 1, "hint": 0, "updown": False, "limit": 0},
    2: {"digits": 5, "hint": 3, "updown": True, "limit": 0},
    3: {"digits": 10, "hint": 1, "updown": True, "limit": 0},
    4: {"digits": 20, "hint": 0, "updown": True, "limit": 40},
    5: {"digits": 100, "hint": 0, "updown": True, "limit": 20},
    6: {"digits": 1000, "hint": 0, "updown": False, "limit": 0}
}

choice_mode = int(input("""
choice mode
1. super easy
2. easy
3. medium
4. hard
5. EXTREME
6. !!k1HyUn!!
=> """))

# 모드        ||  자릿수  || 기타
# super easy ==  1      == 힌트 0번, up&down X
# easy       ==  5      == 힌트 3번, updown O
# midium     ==  10     == 힌트 1번, updown O
# hard       ==  20     == 힌트 0번, updown O
# extreme    ==  100    == 힌트 0번, updown 20
# kihyun     ==  1000   == 힌트 0번, updown X

def print_result(try_cnt, hint_cnt):
    if try_cnt == 1:
        print("bot: you are LEGEND!!")
    else:
        print("bot: you are Right!!")
    print(f"[@] answer is {random_num} you tried {try_cnt} time{'s' if try_cnt > 1 else ''} and used hint {hint_cnt} times")

def is_right_function(user_input, updown):
    if user_input == random_num:
        return True
    elif user_input > random_num and updown:
        print("bot: DOWN ↓")
        return False
    elif user_input < random_num and updown:
        print("bot: UP ↑")
        return False

mode = MODES[choice_mode]["digits"]
allowed_hint = MODES[choice_mode]["hint"]
updown = MODES[choice_mode]["updown"]
limit = MODES[choice_mode]["limit"]

random_num = random.randint(10**(mode-1), 10**mode - 1)

while not is_right:
    user_input = input("user: ").strip().lower()
    
    if user_input in ["hint", "h"]:
        if mode == 5:
            hint_cnt += 1
            match hint_cnt:
                case 1:
                    print(f"bot: first number is {str(random_num)[0]}")
                case 2:
                    print(f"bot: second number is {str(random_num)[:2]}")
                case 3:
                    print(f"bot: third number is {str(random_num)[:3]}")
                case _:
                    print("bot: no more hints!")
            continue
        else:
            if allowed_hint > hint_cnt:
                hint_cnt += 1
                print(f"bot: first {hint_cnt} digit(s) is {str(random_num)[:hint_cnt]}")
            else:
                print("bot: no more hints!")
            continue
    elif user_input in ["surrender", "quit", "exit", "q", "s", "e"]:
        print(f"bot: answer is {random_num}, you tried {try_cnt} times")
        break
    
    # 숫자 맞추기 로직
    try:
        user_input = int(user_input)
        try_cnt += 1
        
        # 모드 설정
        match mode:
            case 1:
                if is_right_function(user_input=user_input, updown=updown):
                    print_result(try_cnt=try_cnt, hint_cnt=hint_cnt)
                    is_right = True
                else:
                    print("bot: Nope")
            
            case 5:
                if is_right_function(user_input=user_input, updown=updown):
                    print_result(try_cnt=try_cnt, hint_cnt=hint_cnt)
                    is_right = True
                
            
            case 10:
                if is_right_function(user_input=user_input, updown=updown):
                    print_result(try_cnt=try_cnt, hint_cnt=hint_cnt)
                    is_right = True
            
            case 20:
                if is_right_function(user_input=user_input, updown=updown):
                    print_result(try_cnt=try_cnt, hint_cnt=hint_cnt)
                    is_right = True
            
            case 100:
                if is_right_function(user_input=user_input, updown=updown):
                    print_result(try_cnt=try_cnt, hint_cnt=hint_cnt)
                    is_right = True
                else:
                    print("bot: Nope")
            
            case 1000:
                if is_right_function(user_input=user_input, updown=updown):
                    print_result(try_cnt=try_cnt, hint_cnt=hint_cnt)
                    is_right = True
                else:
                    print("bot: Nope")
            
    except ValueError:
        print("bot: please enter a valid number or command.")