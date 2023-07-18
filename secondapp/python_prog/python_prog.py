# class Hello :
#     def __init__(self, a, b) :
#         self.a = a
#         self.b = b
    
#     def getPlus(self):
#         return self.a + self.b

from module.util import Hello

def viewPrint() :
    h = Hello(20, 30)
    print(h.getPlus())

### 프로그램 최초 시작 위치....
# - 클래스 또는 함수 형태로 프로그램 구성을 하는 경우 
#   --> 프로그램 시작점이 필요함
# - __main__은 프로그램의 시작을 의미함
if __name__ == '__main__' :
    viewPrint()