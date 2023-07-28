import multiprocessing
import time

#프로세스간의 공유데이터를 한번에 한 프로세스만 접근하도록 잠금

def pro1(v,lck):
    lck.acquire()
    while 10>v.value:
        print(f"pro1 현재의 값은 {v.value}")
        time.sleep(0.01)
        v.value+=1
    lck.release()
    pass

def pro2(v,lck):
    lck.acquire()
    while -10<v.value:
        print(f"pro2 현재의 값은 {v.value}")
        time.sleep(0.01)
        v.value-=1
    lck.release()
    pass

if __name__ == "__main__":
    value = multiprocessing.Value('i',0)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=pro1,args=(value,lock))
    p2 = multiprocessing.Process(target=pro2,args=(value,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()

    pass