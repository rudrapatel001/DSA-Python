from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)
        return False

# Example usage
nums = [1, 2, 3, 4, 4]
solution = Solution()

if solution.hasDuplicate(nums):
    print('true')
else:
    print('false')
    