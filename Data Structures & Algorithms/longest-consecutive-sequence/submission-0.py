class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_number = 0 
        if len(nums) == 0:
            return 0 
        for i in numbers:
            if i-1 not in numbers:
                current_number = i
                count = 1
                while current_number +1 in numbers:
                    current_number += 1
                    count += 1
                max_number = max(max_number, count)

        return max_number