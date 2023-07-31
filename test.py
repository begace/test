"""
멀티 프로세싱 - 병렬처리
+ 멀티 쓰레딩도 있음

target = 함수명
args = 인자값
kwargs = 딕셔너리로 받음

"""
"""
from multiprocessing import Process, freeze_support
import sev_args

def Hello(i, **kwargs):
    for j in range(i):
        print("ㅇㅅㅇ")
    
    #여기에 딕셔너리의 키와 데이터를 출력
    for key, value in kwargs.items():
        print(f"key: {key}, Value: {value}")

p1 = Process(target=Hello, args=(20,), kwargs={"하품":"''<"})
p2 = Process(target=sev_args.worker_function,args=("노예1",1))

if __name__=='__main__':
    freeze_support()
    p1.start()
    p1.join()
    p1.terminate()
    freeze_support()
    p2.start()
    p2.join()
    p2.terminate()

"""

import openai
openai.api_key = ""
MAXTOKENS = 4000

prompt = "질문입력" # 여기에 질문 입력
# OpenAI에 질문을 보내고 응답을 받습니다.
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=MAXTOKENS,
    n=1,
    stop=None,
    temperature=0.8,
    api_key=openai.api_key
)

# 응답의 내용을 출력합니다.
print(response.choices[0].message['content'].strip())