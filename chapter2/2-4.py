# 字符串匹配和搜索
import re
text = 'a2018/4/3a'
pat = re.compile('(\d+)/(\d+)/(\d+)')

# 注意match与search不同
# match只会匹配字符串开头，只要开头不匹配，整个结果就不会匹配，相当于自带^开头
# 所以对于上面的text, '2018/4/3a'可以匹配，'a2018/4/3'就不能
# 而search可以在任意地方进行匹配

result = pat.search(text)
# group(0)是整个正则匹配到的部分，同js match[0]
print(result.group(0), result.group(1)) # 2018/4/3 2018

# 也可以使用findall
text2 = 'Today is 2012/1/1. PyCon starts 2013/3/13.'
result2 = pat.findall(text2)
print('result2: ', result2) # [('2012', '1', '1'), ('2013', '3', '13')]

# 如果想返回一个迭代器,使用finditer
result3 = pat.finditer(text2)
print('result3: ')
for r in result3:
  print(r.group(0), end=',')