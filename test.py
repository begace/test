"""
멀티 프로세싱 - 병렬처리
+ 멀티 쓰레딩도 있음

target = 함수명
args = 인자값
kwargs = 딕셔너리로 받음

"""
"""
from multiprocessing import Process, freeze_support
import sev_args

def Hello(i, **kwargs):
    for j in range(i):
        print("ㅇㅅㅇ")
    
    #여기에 딕셔너리의 키와 데이터를 출력
    for key, value in kwargs.items():
        print(f"key: {key}, Value: {value}")

p1 = Process(target=Hello, args=(20,), kwargs={"하품":"''<"})
p2 = Process(target=sev_args.worker_function,args=("노예1",1))

if __name__=='__main__':
    freeze_support()
    p1.start()
    p1.join()
    p1.terminate()
    freeze_support()
    p2.start()
    p2.join()
    p2.terminate()

"""

a = "100"

try:
    print(len(a))
except TypeError:
    print("a는 시퀀스 타입이 아닙니다. 에러 처리가 필요합니다.")
except ValueError:
    print("Val")
finally: 
    print("fin")