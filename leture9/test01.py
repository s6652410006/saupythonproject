class DTItest01:
    pass
class DTItest02:

    infoA = ''
    infoB = 20

    def showhi (self):
        print('Hi...')
    #method คือ ฟังชั่นประเภทหนึ่ง
    def showinfoAandB(self):
        print(self.infoA)
        print(self.infoB)

objA = DTItest02()
objB = DTItest02()

objA.infoA = 'xxx'
objB.infoB = 100
print(objA.infoB + objB.infoB)

objA.showinfoAandB()