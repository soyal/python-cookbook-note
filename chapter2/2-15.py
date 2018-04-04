# 字符串中插入变量
s = '{name} has {n} message'

print(s.format(name='a', n=10))

# vars
class Person:
  def __init__(self, name, n):
    self.name = name
    self.n = n

p1 = Person('b', 2)
print(s.format_map(vars(p1)))
# __missing__
class safesub(dict):
  def __missing__(self, key):
    return '{' + key + '}'

sub = safesub({'a': 1, 'b': 2})
print(sub['c']) # {c}