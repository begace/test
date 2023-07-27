from multiprocessing import Queue, Process
import time

"""
프로세스간 객체 공유 : Queue() 클래스 사용
특징 : 데이터가 몇개 남았는지 카운터가 동작함.

"""

def pro1(q):
    for i in range(100):
        q.put(i)
    time.sleep(1)

def pro2(q):
    items = []
    while not q.empty():
        item = q.get()
        items.append(item)
        print(f"p2 : q 객체에서 {item}을 가져왔습니다.")
        print(f"현재 큐에 저장된 값은 {items} 입니다.")
        time.sleep(0.1)

if __name__ == "__main__":
    que = Queue()

    #que.

    p1 = Process(target=pro1, args=(que,))
    p2 = Process(target=pro2, args=(que,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()