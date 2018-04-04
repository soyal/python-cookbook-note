# 字符串忽略大小写的搜索和替换
import re

text = 'PYTHON python'
a = re.findall('python', text, re.I)
print(a)


# 让替换的字符串同被替换的字符串保持大小写一致
def matchcase(word):
  def replace(m):
    replaced_text = m.group()
    if replaced_text.isupper():
      return word.upper()
    elif replaced_text.islower():
      return word.lower()
    else:
      return word.capitalize()

  return replace


b = re.sub('python', matchcase('snake'), text, flags=re.I)
print('after sub: ', b)
