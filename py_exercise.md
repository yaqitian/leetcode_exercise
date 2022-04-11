## 7. Reverse Integer
Date:  2022-01-20
### Description:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#### Example 1:
Input: x = 123
Output: 321
#### Example 2:
Input: x = -123
Output: -321
#### Example 3:
Input: x = 120
Output: 21
#### Constraints:
-2^31 <= x <= 2^31 - 1
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
### Description:
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
#### Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
#### Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#### Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#### Constraints:
-2^31 <= x <= 2^31 - 1
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
