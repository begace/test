"""
멀티 프로세스를 시작하는 두가지 방법
"""

import multiprocessing

def start_process():
    return 1

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=start_process)

    p1.start()
    print(multiprocessing.get_start_method())
    p1.join()
    p1.terminate()