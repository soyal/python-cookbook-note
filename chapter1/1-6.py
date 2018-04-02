# 字典中的键映射多个值

from collections import defaultdict

# defaultdict可以给dict每个key指定默认值
arr = defaultdict(list)
arr['a'].append(1)
arr['b'].append(2)

print(arr)