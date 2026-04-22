class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        
        for char in strs:
            sorted_key = "".join(sorted(char))
            group_map.setdefault(sorted_key, []).append(char)

        return list(group_map.values())