# 查找两个字典的相同点
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# keys() 和 items()的返回值可以支持集合操作, values()不行
# 求交集
print(a.keys() & b.keys())
# 求差集
print(a.keys() - b.keys())

## 利用字典推导组成新的字典
c = { key: a[key] for key in a.keys() - b.keys() }
print('c: ', c)