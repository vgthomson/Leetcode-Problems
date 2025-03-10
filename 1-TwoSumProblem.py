from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                print(i,j,nums[i],nums[j])
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)        

        return list(set(result))


solution = Solution()
result = solution.twoSum([3,2,4],6)
print(result)

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 