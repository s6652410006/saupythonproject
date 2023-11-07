f_dti = open('myfile01.txt', 'a', encoding='utf-8')

f_dti.write('AAA')
f_dti.write('CCC')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว...')