# 解构不确定变量数量的对象

name, address, *phone = ('eric', 'Canlifornia', '180-0-000', '106-0-000')
print('name: ', name)
print('address: ', address)
print('phone: ', phone) # type: list