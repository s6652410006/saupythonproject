#โปรแกรมคำนวนหาพื้นที่วงกลม เส้นรอบวงกลม ปริมาครวงกลมจากรัศมีที่ป้อนโดยผู้ใช้ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ
# 5 ฟังชั่น
import math
def inputradius( ) :
    r = float(input('ป้อนรัศมี : '))
    return r

def calarea( r ) :
    return math.pi * math.pow(r,2)

def calround( r ) :
    return 2* math.pi * r

def calcube( r ) :
    return 4/3 * math.pi * r * r * r
print(f'พื้นที่วงกลม {} เส้นรอบวงกลม {} ปริมาตรทรงกลม')