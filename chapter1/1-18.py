# 映射名称到序列元素
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['name', 'age'])

a = Subscriber('eric', 13)
b = Subscriber('tony', 14)
c = Subscriber('frank', 11)

name, age = a
print('name: {}, age: {}'.format(name, age))

# 模拟从数据库中取出比较大的元组列表
def computed_cost(records):
  Stock = namedtuple('Stock', ['name', 'share', 'price'])
  total = 0
  for rec in records:
    s = Stock(*rec)
    total += s.share + s.price
  return total

print(computed_cost([('a', 1, 2), ('b', 3, 4), ('c', 6, 7)]))
# 注意：命名元组不可更改
# s = Stock('a', 1, 2)
# s.name = 'b'
# 上述代码会报错