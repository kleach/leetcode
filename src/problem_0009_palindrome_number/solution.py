class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp = x
        res = 0
        
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        return temp == res
