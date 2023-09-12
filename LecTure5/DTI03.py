#Function แบบบที่ 3 - No parameter/Have return
def nice() :
    print(111)
    print(222)
    a, b, c = nice2()
    print(f'สวัสดี {b} อายุ {a} และ {c}')
    return 999

def nice2() :
    print(333)
    return 10 + 20,'สมชาย' ,True

print(nice())
x = nice()
y = nice() + 111 + 222