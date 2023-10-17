#List
     #   0   1     2       3        4
var1 = [10, 20, 'Hello', True, (111, 'wow')]

print(var1[0] + var1[1])
print(var1[-5] + var1[-4])
print(var1[0] + var1[4][0])
print(var1[-5] + var1[-1][-2])

#Tuple
    #    0   1    2       3        4
var2 = (10, 20, 'Hello', True, (111, 'wow'))

print(var2[0] + var2[1])
print(var2[-5] + var2[-4])
print(var2[0] + var2[4][0])
print(var2[-5] + var2[-1][-2])
print(f'{var2[2]} ...{var2[4][1]}')