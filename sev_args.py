import multiprocessing
import time
#from multiprocessing import freeze_support

print("sev args 모듈 임포트 완료.")

#함수 선언부
def worker_function(name, delay):
    print(f"Worker {name} 시작")
    time.sleep(delay)
    print(f"Worker {name} 종료")

if __name__=="__main__":
    #print("ㅇㅅㅇ")
    #freeze_support()

    process1 = multiprocessing.Process(target=worker_function,args=("노예1",2))
    #프로세스 클래스로 부터 프로세스 객체 생성

    process2 = multiprocessing.Process(target=worker_function,args=("노예2",3))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    process1.terminate()
    process2.terminate()