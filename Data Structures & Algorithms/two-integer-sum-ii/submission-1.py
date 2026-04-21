class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lft, rgt =0 , len(numbers)-1
        while lft< rgt :
            current_sum = numbers[lft]+numbers[rgt]
            if current_sum == target:
                return [lft+1,rgt+1]
            elif current_sum<target :
                lft += 1
            else:
                rgt -= 1 