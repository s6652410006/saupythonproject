try:
    num1 = int(input('Inputnumber 1: '))
    num2 = int(input('Inputnumber 2: '))

    result1 = num1 * num2
    result2 = num1 / num2

    print(f'{num1} x {num2} = {result1}')
    print(f'{num1} / {num2} = {result2}')
except ValueError:
    print('กรุณากรอกจำนวนเต็ม')
except ZeroDivisionError:
    print('0 ไม่สามารถคำนวณ / ได้')
except Exception:
    print('เกินข้อผิดพลาด กรุณาติดต่อ 02-555555 หรือ แผนก IT')
finally:
    print('_________________')
    print('Create by DTI SAU')