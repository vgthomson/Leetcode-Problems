class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        reverse = value[::-1]
        if value == reverse:
            return True
        else:
            return False
        
solution = Solution()
result = solution.isPalindrome(-121)
print(result)



