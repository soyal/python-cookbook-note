# 字符串开头或者结尾匹配

a = 'ababc'
print('start with: ', a.startswith('ab'))
print('end with: ', a.endswith('abc'))

# 也可以传递元组
print('start with(tuple): ', a.startswith(('b', 'a')))