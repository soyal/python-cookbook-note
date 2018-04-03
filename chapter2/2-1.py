# 使用多个界定符分割字符串
import re
s = 'a b    c d                       e'
# 字符串前的r会将字符串中的特殊字符进行转义，将其变成普通字符串
# 输入：r'\s\t'
# 输出：'\\t\\n'
print(re.split(r'\s+', s))

# 如果使用捕获分组，则分组中的匹配文本也会出现在split的结果中
print(re.split(r'(\s+)', s))