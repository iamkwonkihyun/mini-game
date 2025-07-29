import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_board():
    j = 0
    print("\ | 0 | 1 | 2\n--------------")
    for i in range(5):
        if i % 2 == 0:
            print("{} | {} | {} | {}".format(j, board[j][0], board[j][1], board[j][2]))
            j += 1
        else:
            print("--------------")

winning_lines = [
    [(0, 0), (0, 1), (0, 2)],  # 가로 1
    [(1, 0), (1, 1), (1, 2)],  # 가로 2
    [(2, 0), (2, 1), (2, 2)],  # 가로 3
    [(0, 0), (1, 0), (2, 0)],  # 세로 1
    [(0, 1), (1, 1), (2, 1)],  # 세로 2
    [(0, 2), (1, 2), (2, 2)],  # 세로 3
    [(0, 0), (1, 1), (2, 2)],  # 대각선 \
    [(0, 2), (1, 1), (2, 0)],  # 대각선 /
]

board = [[" " for _ in range(3)] for _ in range(3)]
round_cnt = 0

while True:
    clear_console()
    
    show_board()
    
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
            user2_input_row, user2_input_col = map(int, input("\nuser2: ").split())
            
            # 중복 확인
            if board[user2_input_row][user2_input_col] != " ":
                print("중복된 값")
                time.sleep(1)
                continue
            
            # 입력받은 값의 칸을 표시
            board[user2_input_row][user2_input_col] = "X"
            
            # 라운드 값 증가
            round_cnt += 1
    
    for idx, line in enumerate(winning_lines, 1):
        a, b, c = line
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != " ":
            clear_console()
            show_board()
            winner = "user1" if board[a[0]][a[1]] == "O" else "user2"
            print(f"\n{idx} {winner} win")
            time.sleep(10)
            break