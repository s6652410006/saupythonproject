wide = float(input('ความฐาน  : '))
high = float(input('ความสูง   : '))
long = float(input('ความยาว  : '))
lol = float(input('1 แกลลอนทาได้ : '))
area = wide*high*long
print('________________________________________')
print('พื้นที่ทั้ง 6 ด้านของสี่เหลี่ยม {} ตร.ซม จะต้องใช้สี {} แกลลอน' .format (wide*high*long,round(area/lol)))