# เปิดไฟล์
# a, w, x จาก-----------------I-----------ตรงนี้มีคุณสมบัติต่างกัน
f_dti = open('myfile01.txt', 'w', encoding='utf-8')

f_dti.write('Hello')
f_dti.write('Hi...')
f_dti.write('สวัสดี.')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว...')