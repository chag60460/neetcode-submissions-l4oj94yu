class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        output = 0

        left = 0
        max_frequency = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            #keep on shrinking the window until our frequency check passes
            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            #once we've identified a valid window, update output
            output = max(output, right - left + 1)

        return output