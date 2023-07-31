import multiprocessing
from multiprocessing import Pool
import time
import random

def f(x):
    print(f"x = {x}\n")
    return x**(x)

if __name__ == '__main__':
    pool = Pool()

    result = 0

    temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

    for i in temp:
        result = pool.apply(f,args=(i,))
        print(result)

    print("-----------------------------")

    # 비동기 결과 저장을 위한 빈 리스트
    results = []

    results = [pool.apply_async(f, (num,)) for num in temp]

    # 더 이상 작업 추가를 허용하지 않음
    pool.close()
    
    # 모든 작업이 끝날 때까지 대기
    pool.join()

    # 결과 출력
    for result in results:
        print(result.get())