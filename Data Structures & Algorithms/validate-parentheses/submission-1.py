class Solution:
    def isValid(self, s: str) -> bool:
        bracket_lookup_hash = {"(": ")", "{": "}", "[": "]"}
        open_bracket_stack = []

        for char in s:

            #open
            if char in bracket_lookup_hash:
                open_bracket_stack.append(char)
            
            #close
            else:
                if not open_bracket_stack:
                    return False
                
                if char != bracket_lookup_hash[open_bracket_stack.pop()]:
                    return False
            
        return not open_bracket_stack