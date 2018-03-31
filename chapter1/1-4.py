# 查找最大或者最小的N个元素
import heapq

# 简单数据结构
nums = [2, 5, 3, 1, 4]
print('nsmallest', heapq.nsmallest(3, nums))  # [1,2,3]
print('nlargest', heapq.nlargest(3, nums))  # [5,4,3]

# 复杂数据结构
people = [
    {
        'name': 'a', 'age': 13
    }, {
        'name': 'b', 'age': 15
    }, {
        'name': 'c', 'age': 11
    }, {
        'name': 'd', 'age': 14
    }]
print('the 3 most young people', heapq.nsmallest(
    3, people, lambda item: item['age']))
#the 3 most young people [{'name': 'c', 'age': 11}, {'name': 'a', 'age': 13}, {'name': 'd', 'age': 14}]

## note
# heapq进行的是堆排序
tList = [3,-1,2,0,5,6]
heapq.heapify(tList)
print('after heapify ', tList) # [-1, 0, 2, 3, 5, 6] 最小堆
print('the smallest element: ', heapq.heappop(tList)) # -1 弹出最小元素
print('min: ', min(tList))