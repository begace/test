import multiprocessing
import time

# def pro1(s):
#     s.acquire()
#     for i in range(10):
#         print(f"{i}번째 pro1")
#         time.sleep(0.1)
#     s.release()
#     pass

# def pro2(s):
#     s.acquire()
#     for i in range(10):
#         print(f"{i}번째 pro2")
#         time.sleep(0.1)
#     s.release()
#     pass

# if __name__ == '__main__':
#     sema = multiprocessing.Semaphore(1)
#     p1 = multiprocessing.Process(target=pro1, args=(sema,))
#     p2 = multiprocessing.Process(target=pro2, args=(sema,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     p1.terminate()
#     p2.terminate()
#     pass

def Worker_process(s, index):
    s.acquire()
    print(f'Worker process {index} started\n')
    time.sleep(1)

    print(f'Woeker process {index} completed\n')

    s.release()

    print(f'프로세스{index}: semaphore를 release 했습니다.\n')


if __name__ == '__main__':
    sema = multiprocessing.Semaphore(2)
    
    processes = []
    for i in range(20):
        process = multiprocessing.Process(target=Worker_process,
                                           args=(sema, i))
        processes.append(process)
        process.start()
    
    for i in processes:
        i.join()

    
    print('all processes completed')
    pass