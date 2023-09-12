#คำนวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนคนแล้วคำนวนเงินที่จะแชร์กัน
#โดยใช้ 2 ฟังชั่น
def inputmoney() :
    money = float(input('ป้อนจำนวนเงิน : '))
    person = int(input('ป้อนจำนวนคน : '))
    return money, person
def human(money, person) :
    print(f'จำนวนเงิน {(money):.2f} บาท คน {person} คน แบ่งกันคนละ {round(money/person)} บาท')
    print('จำนวนเงิน {:.2f} บาท คน {} คน แบ่งกันคนละ {} บาท' .format(money, person, round(money/person)))
    print('จำนวนเงิน' ,'{:.2f}'.format(money), 'บาท คน' ,person, 'คน แบ่งกันคนละ' ,round(money/person), 'บาท')
    print('จำนวนเงิน '+'{:.2f}'.format(money)+' บาท คน '+str(person)+' คน แบ่งกันคนละ '+str(round(money/person))+' บาท')
    print('จำนวนเงิน %.2f บาท คน %d คน แบ่งกันคนละ %d บาท' %(money, person, round(money/person)))
    
money, person = inputmoney()

human(money, person)