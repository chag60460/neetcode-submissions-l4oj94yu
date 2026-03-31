import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operation_lookup_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        number_stack = []

        for token in tokens:
            if token not in operation_lookup_map:
                number_stack.append(int(token))
            else:
                operation = operation_lookup_map[token]
                operand2 = number_stack.pop(-1)
                operand1 = number_stack.pop(-1)
                result = operation(operand1, operand2)
                number_stack.append(int(result))
        
        return number_stack[-1]