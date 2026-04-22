class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}  
        left = 0       
        max_length = 0
        max_freq = 0
        
        # Iterate with the right pointer to expand the window
        for right in range(len(s)):
            current_char = s[right]
            freq_map[current_char] = freq_map.get(current_char,0)+1
            max_freq = max(max_freq, freq_map[current_char])

            if ((right - left) + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length


