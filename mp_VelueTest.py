import multiprocessing
import time

def pro1(val,pn):
    print(f"벨류 객체의 초기값 \t{''.join(val)}")
    pass

def pro2(val,pn):
    #new_string = "하이룽" 길이가 긴 문자열은 넣을 수 없다.
    new_string = "하잉"
    for i in range(len(new_string)):
        val[i] = new_string[i]
    print(f"벨류 객체에 입력된 값 \t{''.join(val)}")
    pass

if __name__ == "__main__":
    value = multiprocessing.Array('u',"안뇽")

    p1 = multiprocessing.Process(target=pro1, args=(value,"p1"))
    p2 = multiprocessing.Process(target=pro2, args=(value,"p2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()