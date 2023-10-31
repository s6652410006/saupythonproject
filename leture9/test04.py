#คุณสมบัติเด่น Encpsulation (ห่อหุ้ม data / attribute fleld / property)
class DTItest05:
    infoA = 10
    __infoB = 20

    def __init__(self, infoC, infoD):
        self.infoC= infoC
        self.__infoD = infoD
        
    def setinfoB(self, infoB):
        self.__infoB = infoB

    def getinfoB(self):
        return self.__infoB
    
    def setinfoD(self, infoD):
        self.__infoD = infoD

    def getinfoB(self):
        return self.__infoD
    
    def showinfo(self):
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print('__________________')
 
ob1 = DTItest05(30, 40)
ob2 = DTItest05(30, 100)
ob1.showinfo()
ob1.infoA = 555
ob1.setinfoB(999)
ob1.showinfo()
print(ob1.getinfoB() + ob1.getinfoB())
