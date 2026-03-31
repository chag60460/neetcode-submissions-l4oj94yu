import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator_hash = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        num_stack = []

        for token in tokens:
            if token not in operator_hash:
                num_stack.append(int(token))
            else:
                operand2 = num_stack.pop(-1)
                operand1 = num_stack.pop(-1)
                operation = operator_hash[token]
                result = int(operation(operand1, operand2))
                num_stack.append(result)
        
        return num_stack.pop(-1)