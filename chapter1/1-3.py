# 保留最后N个元素
from collections import deque

q = deque(maxlen = 3)
q.append('a')
q.append('b')
q.append('c')
print('q: ', q) #a, b, c

q.append('d')
print('q: ',q) # b, c, d

# 如果不设置maxlen，可以得到无限大小的队列
qInfinite = deque()
qInfinite.append('a')
qInfinite.append('b')
qInfinite.pop()
print('qInfinite: ', qInfinite)
# ps:相比于list，deque在左侧插入元素的效率为o(1)，而list为o(N)