#Function แบบบที่ 2 - Have parameter/No return
def funcA( x , y ) :
    print('AAA')
    z = x + y
    print(f'{x} + {y} = {z}')

def funcB(x , y , z) :
    print('{:.2f} {:.3f} {:.4f}' .format(x,y,z))

funcA(10, 20)
funcA(5, 10)
funcB(1, 5, 10)