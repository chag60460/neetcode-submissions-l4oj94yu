class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hash_map = {}
        max_count = 0
        left = 0

        for index, char in enumerate(s):
            if char in hash_map and hash_map[char] >= left:
                left = hash_map[char] + 1
            hash_map[char] = index
            max_count = max(max_count, index - left + 1)

        return max_count
