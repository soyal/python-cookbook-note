# 实现一个优先队列
import heapq

class Item:
  def __init__(self, name):
    self.name = name

  # __repr__与__str__区别在于__repr可以同时支持print与直接输出，__str__只支持print, __str__的输出会覆盖__repr__
  def __repr__(self):
    return 'Item name:{}'.format(self.name)

class PriorityQueue:
  def __init__(self):
    self._queue = []
    self._len = 0
  def push(self, item, priority):
    heapq.heappush(self._queue, (-priority, self._len, item))
    self._len += 1
  def pop(self):
    return heapq.heappop(self._queue)[-1]

a = Item('a')
b = Item('b')
c = Item('c')

pQ = PriorityQueue()
pQ.push(a, 3)
pQ.push(b, 4)
pQ.push(c, 1)

pQ.pop()
# print('最高优先级item: ', pQ.pop()) # Item name b