# 转换并同时计算数据
params = [1,2,3,4]

s = sum(x for x in params) # sum的参数其实是一个迭代器, 不用写成sum((x for x in params))
print('sum: ', s)