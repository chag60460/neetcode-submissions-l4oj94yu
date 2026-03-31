class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_string = [char for char in s.lower() if char.isalnum()]
        left_pointer, right_pointer = 0, len(raw_string) - 1

        while left_pointer < right_pointer:
            if raw_string[left_pointer] != raw_string[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        
        return True