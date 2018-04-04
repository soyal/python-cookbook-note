# 多行匹配模式
import re

text1 = '*a b c*'
text2 = '''*a b 
c*'''

pat1 = re.compile(r'\*.+\*')
r1 = pat1.search(text1)
print('r1: ', r1)
r2 = pat1.search(text2)
print('r2: ', r2)

# re.DOTALL 表示让.符号可以匹配任意字符，包括换行符
pat2 = re.compile(r'\*.+\*', re.DOTALL)
r2 = pat2.search(text2)
print('dotall r2: ', r2)