class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        left = 0
        max_frequency = 0
        for r in range(len(s)):
            #update the character count
            count[s[r]] = 1 + count.get(s[r], 0)
            max_frequency = max(max_frequency, count[s[r]])
            
            #check if the replace in current window is "valid" using this char as most frequent char
            #i.e. check if windowLength - char_count_in_substring <= k
            #if not valid, increase left pointer to shrink the window
            while ((r - left + 1) - max_frequency) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, r - left + 1)

        return result