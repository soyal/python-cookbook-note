record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:37])

# 替换为切片命名
SHARES = slice(20, 23)
print('SHARES: ', record[SHARES])
PRICE = slice(31, 37)
print('PRICE: ', record[PRICE])
cost = int(record[SHARES]) * float(record[PRICE])
print('cost: {}'.format(cost))

# 使用indices将slice映射到一个确定大小的序列上
a = slice(2, 10, 3)
print('before indecies: ', a)
s = '12345'
b = a.indices(len(s)) 
print('after indecies: ', b) # (2, 5, 3) 返回一个三元组