#Dstructor
class DTItest04:
    deta1 = 10
    def __init__(self, deta2):
        self.deta2 = deta2
        print('Hi')

    def dotack1(self):
        print('>:/')
    
    def dotack2(self, value):
        print(value)  

    def __del__(self):
         print('bye bye')

sauA = DTItest04(10)
sauB = DTItest04(20)
sauC = DTItest04(30)

sauC.dotack2('T_T')
sauC.dotack1()
print(sauA.deta1 + sauB.deta1)