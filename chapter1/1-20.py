# 合并多个字典或者映射

# 需求：需要在两个字典中进行查找，a中没有就找b
from collections import ChainMap
a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}

# .运算符只能操作attr，即class，不能操作字典这样的数据结构
# a.a会报错
c = ChainMap(a, b)
print(c['a'])
print(c['c'])

# 如果键重复，只有第一次出现的会返回
# 更新，删除操作影响的也只会是第一次出现的key
print('keys: ', list(c.keys()))
print('values: ', list(c.values()))

# ChainMap并没有创建新dict
print('before update: ', c)
a['a'] = 10
print('after update: ', c)