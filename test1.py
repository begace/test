#클래스간의 연결을 테스트해봄
class m1:
    items = [] # 
    __count = 0

    def __init__(self,__val=None):
        if __val is None:
            self.__name = "m" + str(m1.__count)
        else : self.__name = __val

        self.items.append(self)

        self.__num = m1.__count
        if m1.__count != 0 : 
            self.items[self.__count].__next = self
        else:
            self.next = None
        m1.__count += 1

    def defNext(self, __val):
        self.__next = __val

    @classmethod
    def create_instances(cls, __count, __val=None):
        for _ in range(__count):
            cls(__val)

    @classmethod
    def add_instances(cls, __count, __val=None):
        cls.create_instances(__count, __val)

    def getName(self):
        return self.__name
    
    def getNum(self):
        return self.__num

# ma = m1("ma")# ma를 m1의 첫 개체로 지정.

m1.create_instances(10)

# m1의 모든 인스턴스 출력
for instance in m1.items:
   print(instance.getName())
   print(instance.getNum())