# 过滤序列元素

# 最简单的方式是使用列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 过滤小于等于0的元素
mylist_a1 = [x for x in mylist if x > 0]
print('> 0: ', mylist_a1)

# 过滤大于0的元素
mylist_a2 = [x for x in mylist if x <= 0]
print('<=0: ', mylist_a2)
#ps: 列表推导会输入非常大的结果集，占用大量内存

#为了节省内存，可以使用生成器
mylist_a3 = (x for x in mylist if x > 0)
print('generator: ', end='')
for item in mylist_a3:
  aaa = 1
  print(item, end=' ')
print('')
# 使用filter
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
  try:
    x = int(val)
    return True
  except:
    return False

# filter返回迭代器
filteredValues = list(filter(is_int, values))
print('filter values: ', filteredValues)

# 对不符合条件的元素进行替换
mylist_a4 = [x if x > 0 else 0 for x in mylist]
print('after convert: ', mylist_a4) # [1, 4, 0, 10, 0, 2, 3, 0]

# 使用itertools compress来筛选
from itertools import compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [ x > 5 for x in counts]
counts_a = list(compress(addresses, more5))
print('itertools compress', counts_a) # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']