class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s_chars = [char.lower() for char in s if char.isalnum()]
        cleaned_s = "".join(cleaned_s_chars)
        return cleaned_s == cleaned_s[::-1]

        