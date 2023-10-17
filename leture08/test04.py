class Test04 :
    deta1 = 10

    def __init__(self, deta2, deta3 ):
        print('Hi....')
        self.deta2 = deta2
        self.deta3 = deta3

    def showSumDeta(self):
        print(self.deta1 + self.deta2 + self.deta3)
        self.showow()

    def showow(self):
        print('wow wow wow...')

objA = Test04(20, 30)
objB = Test04(10, 20)
objC = Test04(20, 100)