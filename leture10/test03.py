f_dti = open('myfile02.txt', 'x', encoding='utf-8')

f_dti.write('Hello')
f_dti.write('Hi...')
f_dti.write('สวัสดี.')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว...')