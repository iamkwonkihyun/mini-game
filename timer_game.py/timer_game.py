import time
import msvcrt  # Windows에서 키 입력 감지용

start = time.perf_counter()

MODE = {
    1: 3,
    2: 5,
    3: 10
}

while True:
    choice_mode = int(input("1. fast(3sec)\n2. medium(5sec)\n3. slow(10sec)\n( 1 / 2 / 3 ) => "))
    if choice_mode not in [1, 2, 3]:
        print("올바른 input plz")
        continue
    else:
        mode = MODE[choice_mode]
        break

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

if seconds == MODE[choice_mode] and milliseconds == 000:
    print("\nwow, Unbelievable!!")
else:
    print("\nfailed")