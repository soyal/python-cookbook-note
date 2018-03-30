# 解构不确定变量数量的对象

# demo1
name, address, *phone = ('eric', 'Canlifornia', '180-0-000', '106-0-000')
print('name: ', name)
print('address: ', address)
print('phone: ', phone) # type: list

# demo2
records = [('a', 1, 2), ('b', 'haha'), ('c', 4, 5)]

for name, *num in records:
  if name != 'b':
    print('position: [{}, {}]'.format(num[0], num[1]))

# demo3
def sum(items):
  head, *tail = items
  return head + sum(tail) if tail else head

sum([1,2,3])