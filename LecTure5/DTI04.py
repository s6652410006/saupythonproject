#Function แบบบที่ 4 - Have parameter/Have return
def lmao(a, b) :
    print(f'{a} ยกกำลัง {b} = {a ** b}')
    return a ** b

def lamo2(a, b, x, y) :
    return a + b + x + y + lmao(2, 3) , 'Wow Nice'

x, y = lamo2 (2, 4, 6, 8)
print(f'{x}  ^_^ {y}')