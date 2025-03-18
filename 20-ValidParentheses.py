class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")","[":"]","{":"}"}
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            elif len(stack)==0 or i != brackets[stack.pop()]:
                return False
        return len(stack)

solution = Solution()
result = solution.isValid("]")
print(result)