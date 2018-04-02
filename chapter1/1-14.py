# 排序不支持原生比较的对象
from operator import attrgetter

class User:
  def __init__(self, id):
    self.id = id
  def __repr__(self):
    return 'User({})'.format(self.id)

demo = [User(11), User(111), User(12)]
print('before, demo: ', demo)
demoAfter = sorted(demo, key=attrgetter('id'))
print('after, demo: ', demoAfter)