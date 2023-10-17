#List
my_list =  [10, 20, 10, 'Hi', True, [20, 'Hello']]
print(my_list)

#Tuple
my_tuple = (10, 20, 10, 'Hi', True, (20, 'Hello'))
print(my_tuple)

#Set   ไม่มีลำดับ
my_set =   {10, 20, 10, 'Hi', True}
print(my_set)

#Dictionary
my_dict = {'name':'สมชาย', 'ago':20, 444:999, 'fiag':True}
print(my_dict['name'])
print(my_dict['ago']+ my_dict[444])
my_dict['name'] = 'สมหญิง'
print(my_dict)
my_dict.pop('name')
my_dict.pop(444)
print(my_dict)

for data in my_dict:
    print(data, end= ' ')
print()
for data in my_dict.keys():
    print(data, end= ' ')
print()
for data in my_dict.values():
    print(data, end= ' ')
print()

my_dict1 = {'a':10, 'b':20, 'c':30}
my_dict2 = my_dict1
my_dict3 = my_dict2.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict2['a'] = 999
my_dict3['a'] = 555
print('-----------------')
print(my_dict1)
print(my_dict2)
print(my_dict3)