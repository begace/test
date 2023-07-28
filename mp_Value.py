import multiprocessing
import time

def pro1(v,pn):
    # print(f"벨류객체의 초기값 {v.value}")
    temp_list = v[0]
    temp_list.append(5)
    temp_list.append(6)
    v[0]=temp_list 
    time.sleep(0.1)
    pass

def pro2(v,pn):
    # v.value = 10
    # print(f"벨류 객체에 입력된 값 {v.value}")
    print(f"매니저 리스트의 값 {v}")
    pass

if __name__ == "__main__":
    value = multiprocessing.Value('i',0)
    manager = multiprocessing.Manager()

    manager_list = manager.list() # 빈 리스트 생성

    manager_list.append([1,2])
    manager_list.append([3,4])
    
    #manager_list[0].append(5) #안됨

    #print(f"매니저 리스트의 값 {manager_list[1][0]}")

    # p1 = multiprocessing.Process(target=pro1,args=(value,"p1"))
    # p2 = multiprocessing.Process(target=pro2,args=(value,"p2"))
    
    p1 = multiprocessing.Process(target=pro1,args=(manager_list,"p1"))
    p2 = multiprocessing.Process(target=pro2,args=(manager_list,"p2"))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    p1.terminate()
    p2.terminate()