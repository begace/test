from multiprocessing import Process, JoinableQueue
import time

def pro1(q):
    for i in range(10):
        q.put(i)
        q.join()
        print(f"Joinable Queue의 값 {i}를 입력했습니다.")
        time.sleep(0.5)
    q.put(None)
    pass

def pro2(q):
    items = []
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        items.append(item)
        print(f"joinable Queue로 부터 {item} 데이터를 가져옴.")
        q.task_done()

    print("모든 Joinable Queue객체의 내용을 가져왔습니다.\n내용 : ",end="")

    print(items)
    pass

if __name__ == "__main__":

    que = JoinableQueue()

    p1 = Process(target=pro1, args=(que,))
    p2 = Process(target=pro2, args=(que,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()