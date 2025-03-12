from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        num1 = "".join(map(str,l1))
        num2 = "".join(map(str,l2))
        value= str(int(num1[::-1]) + int(num2[::-1]))
        for i in value[::-1]:
            result.append(i)
        return result


    

solution = Solution()
result = solution.addTwoNumbers([0],[0])
print(result)