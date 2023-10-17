var2 = (10, 20, 'Hello', True, (111, 'wow'))
vartemp = list(var2)
vartemp[2] = 'Hi'
var2 = tuple(vartemp)
print(var2)