# 通过某个字段将记录分组
from itertools import groupby
from operator import itemgetter

rows = [
  {'address': '5412 N CLARK', 'date': '07/01/2012'},
  {'address': '5148 N CLARK', 'date': '07/04/2012'},
  {'address': '5800 E 58TH', 'date': '07/02/2012'},
  {'address': '2122 N CLARK', 'date': '07/03/2012'},
  {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
  {'address': '1060 W ADDISON', 'date': '07/02/2012'},
  {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
  {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
print('before groupby: ', rows)
rows.sort(key=itemgetter('date'))
print('after groupby: ')
# groupby查找的是连续相同的值，如果值不连续相同，会被视为不同组
for date, items in groupby(rows, itemgetter('date')):
  print('date: ', date)
  for item in items:
    print(' ', item)
