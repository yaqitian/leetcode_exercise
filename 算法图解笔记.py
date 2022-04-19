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

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))  # => 1
    print(binary_search(my_list, -1))  # => None

# 练习
# 1.1 假设有一个包含128个名字的有序列表，你要使用二分查找在其中查找一个名字，请问最多需要几步才能找到？
#     log 128 = 7
# 1.2 上面列表的长度翻倍后，最多需要几步？
#     log 256 = 8
