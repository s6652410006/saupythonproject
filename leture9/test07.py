import test06
import math
from test08 import calcireclearea, calsqurarea, caltrianglearea

print(f'ผลรวมของ 10 + 20 = {test06.sumNumber(10, 20)}')

test06.showHi()
print(f'ราคาสินค้า 2000 ภาษีเป็น {2000*test06.VAT}')

print(f'7 ยกกำลัง 15 ได้ {math.pow(7, 15)}')

print(f'พื้นที่วงกลม รัศมี 3 มีค่า {math.pi + math.pow(3, 2)}')

print(f'พื้นที่วงกลม รัศมี 8 มีค่า {calcireclearea}')

print(f'พื้นที่สี่เหลี่ยม กว้าง 10 ยาว 5 {calsqurarea}')