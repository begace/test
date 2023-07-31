import multiprocessing
import time
import random

def Worker(s,n):
    t = random.randint(0,9) + 1
    print(f'{n}is waiting in {t} seconds')
    time.sleep(t)
    print(f'{n}is ready')
    s.wait()
    print(f'{n} done\n')
    pass

if __name__ == '__main__':
    pb = multiprocessing.Barrier(10)

    pses = []
    for i in range(0,10):
        p = multiprocessing.Process(target=Worker, args=(pb, 'p' + str(i)))
        pses.append(p)

    j = 0

    for i in pses:
        i.start()

    for i in pses:
        i.join()

    for i in pses:
        i.terminate()