# 合并拼接字符串

demo = ['a', 'b', 'c']
# 1.join
print(','.join(demo))

# 2.直接放在一起
b = 'hello' 'world'
print(b)

# 连接大量字符串
data = ['aaa', 'bbb', 'ccc']
c = ','.join(x for x in data)
print(c)

# ps:不要随意用+做字符串合并，尽量使用join