import time
import msvcrt  # Windows에서 키 입력 감지용

exit_code = 0

MODE = {
    1: 3,
    2: 5,
    3: 10
}

def timer_game():
    start = time.perf_counter()
    while True:
        now = time.perf_counter() - start
        
        minutes = int(now // 60)
        seconds = int(now % 60)
        milliseconds = int((now - int(now)) * 1000)
        
        print(f"\r{minutes:02d}:{seconds:02d}.{milliseconds:03d}", end="")
        
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in [b'\r', b' ']:
                break
        
        time.sleep(0.001)
    
    return seconds, milliseconds

while True:
    choice_mode = int(input("1. fast(3sec)\n2. medium(5sec)\n3. slow(10sec)\n(1/2/3) => "))
    
    if choice_mode not in [1, 2, 3]:
        print("올바른 input plz")
        continue
    else:
        mode = MODE[choice_mode]
        
        seconds, milliseconds = timer_game()

        if seconds == MODE[choice_mode] and milliseconds == 000:
            print("\nwow, Unbelievable!!")
            break
        else:
            user_input = input("\nfailed\nretry? (Y/n) => ").strip().lower()
        
        if user_input == "":
            user_input = "y"
        
        if user_input not in ["y", "n"]:
            print("올바른 input plz")
            continue
        
        if user_input == "n":
            break