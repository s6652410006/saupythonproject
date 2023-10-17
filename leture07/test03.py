#append (เพิ่มทีละ 1 ข้อมูล)
var1 = [10, 20, 'Hello', True, [111, 'wow']]
var1.append(555)
var1.append(['Hi', 'Hey', 999])
print(var1)
#extend (เพิ่มทีละหลายๆข้อมูล)
var1.extend([10, 20, 30])
print(var1)
#remove
var1.remove('Hello')
var1.remove(10)
print(var1)
print('--------------------------------')
var2 = [10, 20, 'Hello']
#Insert
var2.insert(0, 'Hi')
#Pop
var2.pop()
print(var2)
var2.pop(1)
print(var2)
#index
print(var2.index('Hi'))
#count (นับจำนวนซ้ำ)
var3 = [10, 10, 10, 10, 'Hi', 'Hi']
print(var3. count(10))

var5=  [99, 34, 55, 78, 56, 555]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)

