# 删除字符串中不需要的字符

s = ' hello world \t\n'
# strip用于删除头部和尾部字符
print('strip: *{}*'.format(s.strip()))
# 删除左侧
print('lstrip: *{}*'.format(s.lstrip()))
# 删除右侧
print('rstrip: *{}*'.format(s.rstrip()))

# 指定删除字符
s2 = '"hello word"'
print('指定删除字符: *{}*'.format(s2.strip('"')))