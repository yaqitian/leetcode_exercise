# 第一章 二分查找

# 基础二分查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# 练习
# 1.1 假设有一个包含128个名字的有序列表，你要使用二分查找在其中查找一个名字，请问最多需要几步才能找到？
#     log 128 = 7
# 1.2 上面列表的长度翻倍后，最多需要几步？
#     log 256 = 8

# 练习
# 使用大O表示法给出下述各种情形的运行时间。
# 1.3 在电话簿中根据名字查找电话号码。
#     O(log n)，二分查找
# 1.4 在电话簿中根据电话号码找人。（提示：你必须查找整个电话簿。）
#     O(n)
# 1.5 阅读电话簿中每个人的电话号码。
#     O(n)
# 1.6 阅读电话簿中姓名以A打头的人的电话号码。这个问题比较棘手，它涉及第4章的概念。答案可能让你感到惊讶！
#     O(n)，大O表示法不考虑乘以、除以、加上或减去的数字



# 第二章 选择排序

# 选择排序复杂度O(n x n)

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = [] 
    for i in range(len(arr)): 
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) 
    return newArr



# 第四章 分治算法

# 递归求和
def sum(list):
    if len(list) == 1:
        return list[0]
    return list[0] + sum(list[1:])
