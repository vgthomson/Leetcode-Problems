class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        for i in s:
            if i == "(" or i =="{" or i =="[":
                stacks.append(i)
                print(i)
            elif i==")":
                if len(stacks)== 0:
                    stacks.append(i)
                elif stacks[-1] == "(":
                    stacks.remove("(")
            elif i=="}":
                if len(stacks)== 0:
                    stacks.append(i)
                elif stacks[-1] == "{":
                    stacks.remove("{")
            elif i=="]":
                print(i)
                if len(stacks)== 0:
                    stacks.append(i)
                elif stacks[-1] == "[":
                    stacks.remove("[")
                    
        if len(stacks) == 0:
            return True
        else:
            return False


solution = Solution()
result = solution.isValid("(])")
print(result)