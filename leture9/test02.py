class DTItest03:
    #deta
    infoA = 20
    #contructor จะทำให้ object ไม่เหมือนกัน
    def __init__(self, infoB, infoC):
        self.infoB = infoB
        self.infoC = infoC
        print('wow wow wow')
    def showbababa(self, alx):
        print(self.infoA + self.infoB + self.infoC + alx)
        
sau1 = DTItest03(20, 30)
sau2 = DTItest03(10, 100)
sau3 = DTItest03(50, 40) 
