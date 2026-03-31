class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hashmap = {"{": "}", "[": "]", "(": ")"}
        open_bracket_stack = []

        for char in s:
            if char in bracket_hashmap:
                open_bracket_stack.append(char)
            else:
                if not open_bracket_stack:
                    return False
                elif char != bracket_hashmap[open_bracket_stack.pop(-1)]:
                    return False
        
        return not open_bracket_stack