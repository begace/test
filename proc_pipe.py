import multiprocessing

def pro1(ps):

    ps.send('1234')
    print("pro1 에서 데이터 보냄")
    pass

def pro2(pr):
    item = pr.recv()
    print(f"pro2 데이터 받음 \n받은 데이터 : {item}")
    pass


if __name__ == '__main__':
    ps, pr = multiprocessing.Pipe()
    
    p1 = multiprocessing.Process(target=pro1, args=(ps,))
    p2 = multiprocessing.Process(target=pro2, args=(pr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()

"""
매니저 - 매니저.리스트, 딕트, 셋 등 복잡한 데이터를 공유하기 위해 씀
큐 - 간단한 데이터를 비동기적으로 공유해 처리하는데 유용함
파이프 - 문자열 같은 직렬화된 데이터를 공유하는데 씀. 샌드 리시브 써서 공유"""