# encoding=UTF-8
# 统计序列中出现次数最多的元素

# 统计最高词频
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
wordCounts = Counter(words)
mostCommon = wordCounts.most_common(3)
print(mostCommon) # [('eyes', 8), ('the', 5), ('look', 4)]
wordCounts.update(['this', 'is', 'eyes'])
mostCommon = wordCounts.most_common(3)
print(mostCommon) # [('eyes', 9), ('the', 5), ('look', 4)]

## Counter可以很方便地进行进行数学运算
a = Counter(['a', 'b', 'a', 'c'])
b = Counter(['a', 'c', 'e', 'c'])
c = a + b
print('most 3 c common: ', c.most_common((3)))
