class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp={}
        for i in nums:
            temp[i] = temp.get(i,0) +1
            if temp[i]> 1:
                return True
        return False

