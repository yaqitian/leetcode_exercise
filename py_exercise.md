## 7. Reverse Integer
Date:  2022-01-20
https://leetcode.com/problems/reverse-integer/
### Solution:
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(abs(x))
        str_y = str_x[::-1]
        y = int(str_y)
        
        if x < 0:
            y = -y
        
        if y < -pow(2, 31) or y > pow(2, 31) - 1:
            return 0
        return y
```

## 9. Palindrome Number
Date:  2022-01-21
https://leetcode.com/problems/palindrome-number/
### Solution:
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        str_y = str_x[::-1]
        if str_y == str_x:
            return True
        return False
```
