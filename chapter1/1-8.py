# 字典的运算

## 求字典中value最大的key
demo1 = {
  'a': 123,
  'b': 12,
  'c': 443,
  'd': 32
}
# zip可以将两个可遍历对象合并成一个可迭代对象
minItemR = min(zip(demo1.values(), demo1.keys()))
print('min key: ', minItemR[1])
maxItemR = max(zip(demo1.values(), demo1.keys()))
print('max key: ', maxItemR[1])

## 也可以用sorted
sortedDemo1 = sorted(demo1, key=lambda x:demo1[x])
print('sorted demo1: ', sortedDemo1) # ['b', 'd', 'a', 'c'] 返回的是key