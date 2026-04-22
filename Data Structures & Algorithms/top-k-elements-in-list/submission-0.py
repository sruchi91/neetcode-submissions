class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        desired_num = []

        for num in nums:  
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq_list = list(freq_map.items())
        freq_list.sort(key=lambda item: item[1], reverse=True)
        for i in range(k) :
                desired_num.append(freq_list[i][0])

        return desired_num

    