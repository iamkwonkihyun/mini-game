import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_board(j):
    print("\ | 0 | 1 | 2\n--------------")
    for i in range(5):
        if i % 2 == 0:
            print("{} | {} | {} | {}".format(j, board[j][0], board[j][1], board[j][2]))
            j += 1
        else:
            print("--------------")

board = [[" " for _ in range(3)] for _ in range(3)]
round_cnt = 0
j = 0

while True:
    clear_console()
    
    show_board(j)
    
    match round_cnt % 2:
        case 0:
            # 입력 받기
            user1_input_row, user1_input_col = map(int, input("\nuser1: ").split())
            
            # 중복 확인
            if board[user1_input_row][user1_input_col] != " ":
                print("중복된 값")
                time.sleep(1)
                continue
            
            # 입력받은 값의 칸을 표시
            board[user1_input_row][user1_input_col] = "O"
            
            # 라운드 값 증가
            round_cnt += 1
        case 1:
            # 입력 받기
            user2_input_row, user2_input_col = map(int, input("user2: ").split())
            
            # 중복 확인
            if board[user2_input_row][user2_input_col] != " ":
                print("중복된 값")
                time.sleep(1)
                continue
            
            # 입력받은 값의 칸을 표시
            board[user2_input_row][user2_input_col] = "X"
            
            # 라운드 값 증가
            round_cnt += 1
    
    if board[0][0] == board[0][1] == board[0][2] != " ": # 1 -
        clear_console()
        show_board(j)
        print("1 user1 win" if board[0][0] == "O" else "1 user2 win")
        time.sleep(10)
        break
    elif board[1][0] == board[1][1] == board[1][2] != " ": # 2 -
        clear_console()
        show_board(j)
        print("2 user1 win" if board[0][0] == "O" else "2 user2 win")
        time.sleep(10)
        break
    elif board[2][0] == board[2][1] == board[2][2] != " ": # 3 -
        clear_console()
        show_board(j)
        print("3 user1 win" if board[0][0] == "O" else "3 user2 win")
        time.sleep(10)
        break
    elif board[0][0] == board[1][0] == board[2][0] != " ": # 1 |
        clear_console()
        show_board(j)
        print("4 user1 win" if board[0][0] == "O" else "4 user2 win")
        time.sleep(10)
        break
    elif board[0][1] == board[1][1] == board[2][1] != " ": # 2 |
        clear_console()
        show_board(j)
        print("5 user1 win" if board[0][0] == "O" else "5 user2 win")
        time.sleep(10)
        break
    elif board[0][2] == board[1][2] == board[2][2] != " ": # 3 |
        clear_console()
        show_board(j)
        print("6 user1 win" if board[0][0] == "O" else "6 user2 win")
        time.sleep(10)
        break
    elif board[0][2] == board[1][1] == board[2][0] != " ": # /
        clear_console()
        show_board(j)
        print("7 user1 win" if board[0][0] == "O" else "7 user2 win")
        time.sleep(10)
        break
    elif board[0][0] == board[1][1] == board[2][2] != " ": # \
        clear_console()
        show_board(j)
        print("8 user1 win" if board[0][0] == "O" else "8 user2 win")
        time.sleep(10)
        break