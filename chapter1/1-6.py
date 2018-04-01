# 字典中的键映射多个值

from collections import defaultdict

arr = defaultdict(list)
arr['a'].append(1)
arr['b'].append(2)

print(arr)