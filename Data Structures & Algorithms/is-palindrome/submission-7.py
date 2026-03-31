class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_string = "".join(char for char in s.lower() if char in "abcdefghijklmnopqrstuvwxyz0123456789")
        left_pointer_index = 0
        right_pointer_index = len(raw_string) - 1

        while left_pointer_index < right_pointer_index:
            if raw_string[left_pointer_index] != raw_string[right_pointer_index]:
                return False
            left_pointer_index += 1
            right_pointer_index -= 1
        
        return True