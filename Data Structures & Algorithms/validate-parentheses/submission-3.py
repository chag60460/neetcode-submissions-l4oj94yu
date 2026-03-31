class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_lookup_table = {"{":"}", "[":"]", "(": ")"}
        tracking_stack = []

        for char in s:
            if char in parenthese_lookup_table:
                tracking_stack.append(char)
            else:
                if not tracking_stack:
                    return False
                if char != parenthese_lookup_table[tracking_stack.pop(-1)]:
                    return False
        
        return not tracking_stack