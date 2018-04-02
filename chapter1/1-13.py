# 通过某个关键字排序一个字典列表
from operator import itemgetter

rows = [
  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
  {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
  {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# itemgetter(name)返回一个函数，该函数接受一个indexable(r)对象，然后回传r[name]
# After f = itemgetter(2), the call f(r) returns r[2].
# After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
sorted_fname = sorted(rows, key=itemgetter('fname'))
print('sorted_fname: ', sorted_fname)
sorted_uid = sorted(rows, key=itemgetter('uid'))
print('sorted_uid: ', sorted_uid)
