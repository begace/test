import multiprocessing
import time

"""
def callNrecv(temp):
    print(f'this is {temp}')

def pro1(pc):
    pc.acquire()
    pc.wait()
    callNrecv('pro1')
    pc.release()
    pass

def pro2(pc):
    pc.acquire()
    pc.notify_all()
    callNrecv('pro2')
    pc.release()
    pass

if __name__ == '__main__':
    pc = multiprocessing.Condition()
    p1 = multiprocessing.Process(target=pro1, args=(pc,))
    p2 = multiprocessing.Process(target=pro1, args=(pc,))
    p3 = multiprocessing.Process(target=pro2, args=(pc,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    p1.terminate()
    p2.terminate()
    p3.terminate()
    """

def worker_process(condition, pn):
    with condition:
        condition.wait()

        print(f'{pn} Worker process started')
        print('Worker process completed')

if __name__ == '__main__':
    condition = multiprocessing.Condition()

    process1 = multiprocessing.Process(target=worker_process, args=(condition, 'pro1'))
    process2 = multiprocessing.Process(target=worker_process, args=(condition, 'pro2'))

    process1.start()
    process2.start()

    time.sleep(2)

    #condition.acquire()

    with condition:
        condition.notify_all()

    process1.join()
    process2.join()

    print('All process is done')