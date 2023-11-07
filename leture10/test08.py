# ลบไฟล์
import os
from os import remove

if os.path.exists('myfil01.txt'):
    remove('myfil01.txt')
    print('ลบไฟล์')
else:
    print('ไฟล์ที่จะลบไม่มี')