## Date:  2022-01-20
## Title: 7. Reverse Integer
## Description:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
### Example 1:
  Input: x = 123
  Output: 321
### Example 2:
  Input: x = -123
  Output: -321
### Example 3:
  Input: x = 120
  Output: 21
### Constraints:
  -231 <= x <= 231 - 1

## Solution:
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
