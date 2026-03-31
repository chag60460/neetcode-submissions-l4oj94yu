class Solution:
    def isValid(self, s: str) -> bool:
        lookup_hash = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for char in s:
            #open - add to stack
            if char in lookup_hash:
                stack.append(char)
            
            #close - pop corresponding from stack
            else:
                
                #can't start with closed parenthesis
                if not stack:
                    return False
                
                popped = stack.pop()

                #can't have out of order parenthesis
                if lookup_hash[popped] != char:
                    return False
        
        return len(stack) == 0
                
