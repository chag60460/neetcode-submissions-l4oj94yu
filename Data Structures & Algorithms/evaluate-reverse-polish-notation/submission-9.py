import operator

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        
        num_stack = []

        operator_lookup_hash = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        
        for token in tokens:
            if token not in operator_lookup_hash:
                num_stack.append(int(token))
            else:
                operation = operator_lookup_hash[token]
                operand2 = num_stack.pop(-1)
                operand1 = num_stack.pop(-1)
                result = int(operation(operand1, operand2))
                print(result)
                num_stack.append(result)
        
        return num_stack[-1]
        