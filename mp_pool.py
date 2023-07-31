import multiprocessing
from multiprocessing import Pool
import time

# def f(x):
#     return x * x

# if __name__ == '__main__':
#     p = Pool()
#     results = p.map(f,[1,2,3,4,5,6,7,8,9])

#     for i in multiprocessing.active_children():
#         print(i)
        
#     p.close()
#     p.join()
#     p.terminate()
#     print(results)
#     pass

def square_number(x):
    return x ** 2

if __name__ == '__main__':

    numbers = [1,2,3,4,5]

    with multiprocessing.Pool() as pool:
        result = pool.map(square_number,numbers)

        for i in result:
            print(i)
