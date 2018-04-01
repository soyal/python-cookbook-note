# 字典排序
# 注意：3.6之后，dict也是插入有序的，3.7之后将成为语言规范
from collections import OrderedDict

normalDict = OrderedDict() # OrderedDict会按照元素的插入顺序排序
normalDict['d'] = 4
normalDict['a'] = 2
normalDict['b'] = 3
normalDict['cc'] = 5
normalDict['bb'] = 6
normalDict['dd'] = 7

for key in normalDict:
  print('key: {}, value: {}'.format(key, normalDict[key]))

import json 
print('json: ', json.dumps(normalDict)) # json:  {"d": 4, "a": 2, "b": 3, "cc": 5, "bb": 6, "dd": 7}