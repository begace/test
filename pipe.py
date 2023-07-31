import multiprocessing

def pro1(sender):
    sender.send('1234')
    print('p1 데이터 보냄')

def pro2(receiver):
    item = receiver.recv()
    print(f'p2 데이터 받음 item {item}')

if __name__ == "__main__":
    ps, pr = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=pro1, args=(ps,))
    p2 = multiprocessing.Process(target=pro2, args=(pr,))

    p1.start()
    p2.start()

    print(f'current prosecc name = {multiprocessing.current_process().name}')
    print(f'current prosecc ID = {multiprocessing.current_process().pid}')

    active_processes = multiprocessing.active_children()
    
    for i in active_processes:
        print(i.name)
        print(i.pid)

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()