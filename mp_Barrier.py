import multiprocessing
import time
import random

def Worker(s,n):
    t = random.randint(0,9)
    print(f'{n}is waiting in {t}')
    time.sleep(t)
    s.wait()
    print(f'{n} done\n')
    pass

if __name__ == '__main__':
    pb = multiprocessing.Barrier(2)

    pses = []
    for i in range(0,10):
        p = multiprocessing.Process(target=Worker, args=(pb, 'p'+str(i)))
        pses.append(p)

    for i in pses:
        i.start()
    
    for i in pses:
        i.join()
    
    for i in pses:
        i.terminate()