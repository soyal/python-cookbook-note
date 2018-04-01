# 删除序列相同的元素并保持顺序

## hashable去重
def dedupe(items):
  seen = set()
  for item in items:
    if item not in seen:
      yield item
      seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print('after dedupe: ', list(dedupe(a)))