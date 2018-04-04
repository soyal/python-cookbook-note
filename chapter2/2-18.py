# 字符串令牌解析
text = 'foo = 23 + 42 * 10'
import re

# ?P<TOKENNAME>用于给一个模式命名，供后面使用
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# while _s:
#   print(_s.group(), end='')
#   _s = scan.match()

from collections import namedtuple

def generate_tokens(pat, text):
  Token = namedtuple('Token', ['type', 'value'])
  scanner = pat.scanner(text)
  # iter(object[, sentinel])
  # 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object
  for m in iter(scanner.match, None):
    yield Token(m.lastgroup, m.group())

for v in generate_tokens(master_pat, 'foo = 3'):
  print(v.type, v.value)
