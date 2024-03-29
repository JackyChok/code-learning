class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1
        
        return right - left + 1

# Test cases
print(Solution().minimumLength("ca"))        # Output: 2
print(Solution().minimumLength("cabaabac"))  # Output: 0
print(Solution().minimumLength("aabccabba")) # Output: 3
print(Solution().minimumLength("aaabcabba")) # Output: 2
