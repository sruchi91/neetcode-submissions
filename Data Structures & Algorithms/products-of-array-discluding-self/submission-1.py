
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_num =[]
        # non_zero_list = []
        number = 1
        num_wo_zero = 1
        non_zero_lst = list(filter(lambda x: (x != 0), nums)) 
        zeros = len(nums)- len(non_zero_lst)
        for i in range (0, len(nums)):
            number = number*nums[i]
        for i in range (0, len(non_zero_lst)):
            num_wo_zero= num_wo_zero*non_zero_lst[i]
        if zeros >1:
            for i in range (0, len(nums)):
                prod_num.append(0)
        elif zeros == 1:
            for i in range (0, len(nums)):
                if nums[i]==0:
                    prod_num.append(num_wo_zero)
                else:
                    prod_num.append(0)
        else:
            for i in range (0, len(nums)):
                prod_num.append(number//nums[i])
        return prod_num