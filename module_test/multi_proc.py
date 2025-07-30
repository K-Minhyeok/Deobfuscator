import time
from multiprocessing import Pool

def slow_square(x):
    time.sleep(1)
    return x * x

nums = [1,2,3,4]

with Pool(2) as pool:
    print("[ MAP ]")
    # map은 4개 결과가 모두 끝날 때까지 기다림!
    print(list(pool.map(slow_square, nums)))  # → 약 2초 뒤 [1, 4, 9, 16] 출력

    # imap은 앞부분부터 결과를 하나씩 받을 수 있음
    print(" [ IMAP ] ")
    for result in pool.imap(slow_square, nums):
        print(result)  # → 1, 4, 9, 16 순서로 한 개씩 0.5초마다 바로 출력

    print(" [ IMAP_UNORDERED ] ")
    for result in pool.imap_unordered(slow_square,nums):
        print(result)