try:
    f_dit = open('myfile01.txt', 'r', encoding='utf-8')
    data = f_dit.read()

    print(data)
except Exception:
    print('ติดต่อ 02-55555')
finally:
    f_dit.close()