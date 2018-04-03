# 字符串搜索和替换

# 简单的替换
text = 'a b c'
text_ar = text.replace('b', 'eee')
print(text_ar)

# 使用re.sub
import re
# 将2018/1/1 替换为2018-1-1
d = '2018/1/1'
pat = re.compile(r'(\d+)/(\d+)/(\d+)')
# \1 表示前面的group(1)
d_sub = pat.sub(r'\1-\2-\3', d)
print(d_sub)

# 使用fn
def replace_date(m):
  return '{}-{}-{}'.format(m.group(1), m.group(2), m.group(3))
d_sub2 = pat.sub(replace_date, d)
print('after replace fn: ', d_sub2)