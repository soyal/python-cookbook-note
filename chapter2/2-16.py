# 以指定列宽格式化字符串

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
# 限制打印出来的宽度
print(textwrap.fill(s, 40, initial_indent='    '))