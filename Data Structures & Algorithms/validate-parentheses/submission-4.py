class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_hashmap = {"[": "]", "(": ")", "{": "}"}
        parenthesis_stack = []

        for char in s:
            if char in parenthesis_hashmap:
                parenthesis_stack.append(char)
            else:
                if not parenthesis_stack:
                    return False
                
                key = parenthesis_stack.pop(-1)
                if char != parenthesis_hashmap[key]:
                    return False
        
        if parenthesis_stack:
            return False
        
        return True