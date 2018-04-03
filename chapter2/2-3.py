# 用Shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
# fnmatch模块是用于匹配filename的

file = 'a.txt'
pat = '*.TXT'
# 使用的是系统的匹配规则，windows大小写不敏感，mac os 大小写敏感
print('fnmatch: ', fnmatch(file, pat))
# 强制大小写敏感
print('fnmatchcase: ', fnmatchcase(file, pat))