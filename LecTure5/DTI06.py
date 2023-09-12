def examplel() :
    print(111)
    print(222)
    print(333)
    return
    print(3333)
    print(9999)
    return
examplel()

#Default Paramiter
def dtitest(x, y, z = 20, a = 10) :
    print(f'{x} + {y} + {z} + {a} = {x+y+z+a}')

dtitest (5, 100)
dtitest(9, 8, 10)