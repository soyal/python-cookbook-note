# 在字符串中处理html和xml

# 替换富文本中的< >

import html

text = '<p>111</p>'

print(html.escape(text)) # &lt;p&gt;111&lt;/p&gt;