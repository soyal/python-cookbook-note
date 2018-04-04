# 最短模式匹配
import re
pat = re.compile(r'"(.*)"')

text = 'Computer says "no." Phone says "yes."'
r1 = pat.search(text)
print('result1: ', r1.group()) # "no." Phone says "yes." 结果为长匹配

# 非贪婪模式
pat2 = re.compile(r'"(.*?)"')

r2 = pat2.search(text)
print('result2: ', r2.group())